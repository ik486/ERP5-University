from Products.ERP5Type.XMLObject import XMLObject
from Products.ERP5Type import Permissions, PropertySheet, Constraint
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName

class BudgetItem(XMLObject):

   # CMF Type Definition
   meta_type = 'ERP5 Budget Item'
   portal_type = 'Budget Item'
   add_permission = Permissions.AddERP5Content
   isPortalContent = 1
   # this will allow me to have get/set and other facilities automatically generated
   isRADContent = 1

   # Declarative security
   security = ClassSecurityInfo()
   security.declareObjectProtected(Permissions.View)

   # Default Properties
   # note that I redeclare all propertysheets from the base classes, and my new ones - which I have to create inside the propertysheet directory
   property_sheets = ( PropertySheet.Base
                     , PropertySheet.XMLObject
                     , PropertySheet.DublinCore
                     , PropertySheet.Amount
                     , PropertySheet.BudgetItem
                     )

   # CMF Factory Type Information
   factory_type_information = \
     {    'id'             : portal_type
        , 'meta_type'      : meta_type
        , 'description'    : '''A Budget Item...'''
        , 'icon'           : 'folder_icon.gif' # should create a new budget_item.gif for the new type...and change folder_icon.gif name
        , 'product'        : 'ERP5'
        , 'factory'        : 'addBudgetItem'
        , 'immediate_view' : 'budget_item_view'
        , 'allow_discussion'     : 1
        , 'allowed_content_types': ()
        , 'filter_content_types' : 1
        , 'global_allow'   : 1
        , 'actions'        :
       ( { 'id'            : 'view'
         , 'name'          : 'View'
         , 'category'      : 'object_view'
         , 'action'        : 'budget_item_view'
         , 'permissions'   : (
            Permissions.View, )
         }
         , { 'id'            : 'list'
         , 'name'          : 'Object Contents'
         , 'category'      : 'object_action'
         , 'action'        : 'folder_contents'
         , 'permissions'   : (
             Permissions.View, )
         }
       , { 'id'            : 'print'
         , 'name'          : 'Print'
         , 'category'      : 'object_print'
         , 'action'        : 'order_print'
         , 'permissions'   : (
            Permissions.View, )
         }
       , { 'id'            : 'metadata'
         , 'name'          : 'Metadata'
         , 'category'      : 'object_view'
         , 'action'        : 'metadata_edit'
         , 'permissions'   : (
            Permissions.View, )
         }
       , { 'id'            : 'translate'
         , 'name'          : 'Translate'
         , 'category'      : 'object_action'
         , 'action'        : 'translation_template_view'
         , 'permissions'   : (
            Permissions.TranslateContent, )
         }
       )
     }

   def edit(self, **vals):
   	"""
   	EDIT fn of  Budget Item
   	"""
   	if vals.has_key('financial_year'):
   	   self.setFinancialYear(vals['financial_year'])
   	if vals.has_key('plan_type'):
   	   self.setPlanType(vals['plan_type'])
   	if vals.has_key('budget_head'):
   	   self.setBudgetHead(vals['budget_head'])
#--------------------------------------------------------------------------wed_sep_29_2010 by ch
        if vals.has_key('department'):
           self.setDepartment(vals['department'])
   	if vals.has_key('description'):
   	   self.setDescription(vals['description'])
#--------------------------------------------------------------------------wed_sep_29_2010 end
   	if vals.has_key('budget_provision'):
   	   self.setBudgetProvision(vals['budget_provision'])
   	if vals.has_key('letter_reference'):
   	   self.setLetterReference(vals['letter_reference'])
   	if vals.has_key('letter_date'):
   	   self.setLetterDate(vals['letter_date'])
   	if vals.has_key('university_order'):
   	   self.setUniversityOrder(vals['university_order'])
   	if vals.has_key('university_order_date'):
   	   self.setUniversityOrderDate(vals['university_order_date'])
	##############################################################################
	self.calAmountSpent()
	self.calBudgetAvailable()
	self.calBalanceAmount()
	return


   def isOKState(self):
        """
        """
        state = self.getState()
        if state in ['deleted', 'cancelled']: return 0
        return 1


   security.declareProtected(Permissions.AccessContentsInformation, 'getTitle')

   def getTitle(self, **kw):
      """
        Returns the title if it exists or a combination of
        first name and last name
      """
      name_list = []
      #if self.getFinancialYear() not in (None, ''):
      #    name_list.append(self.getFinancialYear()+":")
      #else:
      #	  name_list.append(":")
      if self.getPlanType() not in (None, ''):
          name_list.append(self.getPlanType())
      if self.getDepartment() not in (None, ''):
          name_list.append(self.getDepartment())
      if self.getBudgetHead() not in (None, ''):
          name_list.append(self.getBudgetHead().split('/').pop())
      out = ''.join(name_list)
      out = out.replace('-','')
      return out


   def calculateAll(self):
	self.calAmountSpent()
	self.calBudgetAvailable()
	self.calBalanceAmount()
	return 

   def setBudgetProvision(self, val):
	"""
	"""
	self.budget_provision = val
	self.calBudgetAvailable()
	self.calBalanceAmount()
	return

   def calAmountSpent(self):
	""" Amount
	"""
	uid = self.getUid()
	catalog = getToolByName(self, 'portal_catalog')
	out = 0
	############################################################################
	results = catalog(portal_type=('Bill','Simple Receipt',))
	for result in results:
		obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
		if obj.getSourceSectionUid() == uid:
			val = obj.getApprovedGrossAmount()
			if val: out += int(val)
	############################################################################
	results = catalog(portal_type='Adjustment Bill')
	for result in results:
		obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
		if obj.getSourceSectionUid() == uid:
			val = obj.getBalanceAvalibleInSr()
			if val: 
				if val < 0:
					out -= int(val)
	############################################################################
	self.setAmountSpent(out)
	return out


   def calBudgetAvailable(self):
	""" Available
	"""
	uid = self.getUid()
	out = self.getBudgetProvision()
	if not out: out = 0
	#######################################################################
	#catalog = getToolByName(self, 'portal_catalog')
	#######################################################################
	#results = catalog(portal_type=('Bill','Adjustment Bill',))
	#for result in results:
	#	obj = result.getObject()
	#	if obj is None: continue
	#	if not obj.isOKState(): continue
	#	if obj.getUid() == uid:
	#		val = obj.getRefundAmount()
	#		if val: out += int(val)
	#######################################################################
	catalog = getToolByName(self, 'portal_catalog')
	results = catalog(portal_type='Fund Diversion')
	for result in results:
		obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
		if obj.getSourceSectionUid() == uid:
			val = obj.getTransferAmount()
			if val: out -= int(val)
		if obj.getDestinationSectionUid() == uid:
			val = obj.getTransferAmount()
			if val: out += int(val)
	self.setBudgetAvailable(out)
	return out


   def calBalanceAmount(self):
	""" Balance
	"""
	a = self.getBudgetAvailable()
	b = self.getAmountSpent()
	if not a: a=0
	if not b: b=0
	out = a-b
	self.setBalanceAmount(out)
	return out

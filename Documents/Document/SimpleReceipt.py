from Products.ERP5Type.XMLObject import XMLObject

from Products.ERP5Type import Permissions, PropertySheet, Constraint

from AccessControl import ClassSecurityInfo

from Products.CMFCore.utils import getToolByName

class SimpleReceipt(XMLObject):

   # CMF Type Definition
   meta_type = 'ERP5 Simple Receipt'
   portal_type = 'Simple Receipt'
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
                     , PropertySheet.SimpleReceipt
                     )

   # CMF Factory Type Information
   factory_type_information = \
     {    'id'             : portal_type
        , 'meta_type'      : meta_type
        , 'description'    : '''A Simple Receipt...'''
        , 'icon'           : 'folder_icon.gif' # should create a new simple_receipt.gif for the new type...and change folder_icon.gif name
        , 'product'        : 'ERP5'
        , 'factory'        : 'addSimpleReceipt'
        , 'immediate_view' : 'simple_receipt_view'
        , 'allow_discussion'     : 1
        , 'allowed_content_types': ()
        , 'filter_content_types' : 1
        , 'global_allow'   : 1
        , 'actions'        :
       ( { 'id'            : 'view'
         , 'name'          : 'View'
         , 'category'      : 'object_view'
         , 'action'        : 'simple_receipt_view'
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

   ##################################################################################
   # Added on 19/03/2010
   ##################################################################################


   def edit(self, **vals):
   	"""
   	EDIT fn of  Simple Receipt
   	"""
   	if vals.has_key('bill_no'):
   	   self.setBillNo(vals['bill_no'])
   	if vals.has_key('date'):
   	   self.setDate(vals['date'])
   	if vals.has_key('budget'):
   	   self.setBudget(vals['budget'])
   	if vals.has_key('net_amount_claimed_in_this_bill'):
   	   self.setNetAmountClaimedInThisBill(vals['net_amount_claimed_in_this_bill'])
   	if vals.has_key('deduction_amount'):
   	   self.setDeductionAmount(vals['deduction_amount'])
   	if vals.has_key('forwardedto'):
   	   self.setForwardedto(vals['forwardedto'])
   	if vals.has_key('university_order_no'):
   	   self.setUniversityOrderNo(vals['university_order_no'])
   	if vals.has_key('university_order_date'):
   	   self.setUniversityOrderDate(vals['university_order_date'])
   	if vals.has_key('name_of_supplier'):
   	   self.setNameOfSupplier(vals['name_of_supplier'])
   	if vals.has_key('reasons_for_objection'):
   	   self.setReasonsForObjection(vals['reasons_for_objection'])
        if vals.has_key('voucher_no'):
           self.setVoucherNo(vals['voucher_no'])
        if vals.has_key('description'):
           self.setDescription(vals['description'])


        ###################################################################################
        self.calculateBudgetItem()
        ###################################################################################
        #self.calBalanceAvalibleInBudget()
        #self.calExpenduitureIncludingThisBill()
        #self.calApprovedGrossAmount()
        self.calDeductionCalculated()
        ###################################################################################
        ###################################################################################
        self.calApprovedGrossAmount()
        self.calExpenduitureIncludingThisBill()
        # SET VALUES IN BUDGET ITEM
        self.calBudgetItemAmountSpent()
        self.calBudgetItemBalanceAmount()
        self.calBalanceAvalibleInBudget()

        self.calDepartment()
	return



   def isOKState(self):
        """
        """
        state = self.getSimulationState()
        if state in ['deleted', 'cancelled']: return 0
        return 1


   def getRoleList(self):
       """
       """
       mt = getToolByName(self, 'portal_membership')
       if mt.isAnonymousUser(): # the user has not logged in
           return []
       else:
           member = mt.getAuthenticatedMember()
           out = member.getRolesInContext(self)
           return out



   def editAny(self, **vals):
        """
        """
        roleList = self.getRoleList()
        if 'Manager' in roleList: return 1
#------------------------------------------------------------------------for backlog entry server cijish:oct 7,12:54
        if 'Assignee' in roleList: return 1	
#------------------------------------------------------------------------for backlog entry server cijish:oct 7,12:54 end
        ############################################3
       # pobj = self.getParentValue()
        state = self.getSimulationState()
        if not vals.get(state, None): return 0
        for role in vals[state]:
                if role in roleList: return 1
        return 0

   #############################################################################

   def calculateAll(self):
	"""
	"""
	self.calculateBudgetItem()
        ########################################################
	self.calBalanceAvalibleInBudget()
	self.calExpenduitureIncludingThisBill()
	self.calApprovedGrossAmount()
	self.calDeductionCalculated()

   def setSourceSection(self, value=None):
	"""
	if self.getTitle() == 'CUSAT':
		self.setTitle('CIRM')
	else:
		self.setTitle('CUSAT')
	"""
	self.source_section = value
	self.calExpenduitureIncludingThisBill()
	self.calBalanceAvalibleInBudget()
	self.calDepartment()
	return
	
   def setNetAmountClaimedInThisBill(self, val):
	"""
	"""
	self.net_amount_claimed_in_this_bill = val
        self.calExpenduitureIncludingThisBill()
        self.calBalanceAvalibleInBudget()
        self.calDepartment()
	return

   def calBalanceAvalibleInBudget(self):
	""" Budget Balance
	"""
        catalog = getToolByName(self, 'portal_catalog')

	uid1 = self.getSourceSectionUid()
        result = catalog(uid=uid1)
	if not len(result): 
		self.setBalanceAvalibleInTheBudget(0)
		return 0 
	obj = result[0].getObject()
        if obj is None:
                self.setBalanceAvalibleInBudget(0)
                return 0
        if not obj.isOKState():
                self.setBalanceAvalibleInBudget(0)
                return 0
	val = obj.getBalanceAmount()
	if not val: 
		self.setBalanceAvalibleInTheBudget(0)
		return 0 
	out = int(val)
	self.setBalanceAvalibleInTheBudget(out)
	return out

   def getNetAmountPayable(self):
	""" Net
	"""
	a = self.getApprovedGrossAmount()
	b = self.getDeductionAmount()
	if not a: a = 0
	if not b: b = 0
	return a - b

   def calExpenduitureIncludingThisBill(self):
	""" ok
	"""
	uid1 = self.getSourceSectionUid()
        catalog = getToolByName(self, 'portal_catalog')
        result = catalog(uid=uid1)
	if not len(result): 
		out = 0
	else:
		obj = result[0].getObject()
		if obj is None:
			out = 0
		elif not obj.isOKState():
			out = 0
		else:
			val = obj.getAmountSpent()
			if not val: 
				out = 0
			else:
				out = int(val)
	self.setExpenduitureIncludingThisBill(out)
	return out


   def calculateBudgetItem(self):
        """ ok
        """
        uid1 = self.getSourceSectionUid()
        catalog = getToolByName(self, 'portal_catalog')
        result = catalog(uid=uid1)
        if len(result):
                obj = result[0].getObject()
		if obj is None: return
		if not obj.isOKState(): return
		obj.calculateAll()
        return

   def calBudgetItemAmountSpent(self):
        """ ok
        """
        uid1 = self.getSourceSectionUid()
        catalog = getToolByName(self, 'portal_catalog')
        result = catalog(uid=uid1)
        if len(result):
                obj = result[0].getObject()
		if obj is None: return
		if not obj.isOKState(): return
        	obj.calAmountSpent()
        return

   def calBudgetItemBudgetAvailable(self):
        """ ok
        """
        uid1 = self.getSourceSectionUid()
        catalog = getToolByName(self, 'portal_catalog')
        result = catalog(uid=uid1)
        if len(result):
                obj = result[0].getObject()
		if obj is None: return
		if not obj.isOKState(): return
        	obj.calBudgetAvailable()

        return

   def calBudgetItemBalanceAmount(self):
        """ ok
        """
        uid1 = self.getSourceSectionUid()
        catalog = getToolByName(self, 'portal_catalog')
        result = catalog(uid=uid1)
        if len(result):
                obj = result[0].getObject()
		if obj is None: return
		if not obj.isOKState(): return
        	obj.calBalanceAmount()
        return


   def calApprovedGrossAmount(self):
	"""
	"""
        catalog = getToolByName(self, 'portal_catalog')
	uid = self.getUid()
        results = catalog(portal_type='Sub Bill', parent_uid=uid)
	out = 0
	if not len(results): 
		out = self.getNetAmountClaimedInThisBill()
	else:
	   for result in results:
		obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
		val = obj.getAmountPassed()	
		if val: 
			out += int(val)
	self.setApprovedGrossAmount(out)
	return out

   def calDeductionCalculated(self):
	"""
	"""
        catalog = getToolByName(self, 'portal_catalog')
	uid = self.getUid()
        results = catalog(portal_type='Deduction', parent_uid=uid)
	out = 0
	if not len(results): 
		out = 0
	else:
	   for result in results:
		obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
		val = obj.getAmount()	
		if val: 
			out += int(val)
	self.setDeductionCalculated(out)
	return out

   def getBillState(self):
	"""
	"""
	return self.getSimulationStateTitle()


   def calDepartment(self):
        """
        """
        uid1 = self.getSourceSectionUid()
        catalog = getToolByName(self, 'portal_catalog')
        results = catalog(uid=uid1)
        if not len(results):
                out = None 
        else:
                obj = results[0].getObject()

		if obj is None: return
		if not obj.isOKState(): return

                out = obj.getDepartment()
		self.setDepartment(out)

		out = obj.getFinancialYear()
		self.setFinancialYear(out)

		out = obj.getPlanType()
		self.setPlanType(out)

		out = obj.getBudgetHead() 
		self.setBudgetHead(out)

                out = obj.getBudgetProvision()
                self.setBudgetProvision(out)

                out = obj.getBudgetAvailable()
                self.setBudgetAvailable(out)
        return out 


   def setRefundAmount(self, val):
	"""
	"""
	self.refund_amount = val
	self.calBudgetAvailable()
	return




   def budgetTest(self):
	"""
	"""
        self.calBudgetItemAmountSpent()
	self.calBudgetItemBalanceAmount()
	balance_avalible_in_budget = self.getBalanceAvalibleInTheBudget()
	#net_amount_claimed_in_this_bill = self.getNetAmountClaimedInThisBill()
	out = balance_avalible_in_budget
	if out < 0:
		raise "Revised Budget provision is less than  Gross amount calmed in this bill. \n Check budget head or Add fund diversion ",out 
		out = 0
	else:
	     out=1
	return out


#############################################################################






#_______________________________________________________________________________________________________
   def getHelp(self):
	""" Net
	"""
	bill_help = {
'chequenoadded': {'Cashier':'''<li style="margin: 0.5em 0em 0em 3em;">
                                 Verify if the Voucher Number entered is correct.
                               </li><li style="margin: 0.5em 0em 0em 3em;">
                                 If not, correct the same and click the 'Save' icon to register the correction.
                               </li><li style="margin: 0.5em 0em 0em 3em;">   
                                  To verify the cheque number entries, click 'Cheque'. </li>
                             '''},
 'verified': {'Auditor': '''<li style="margin: 0.5em 0em 0em 3em;">
                             Check correctness of all entries made by the Asst and verified by the SO with the actual bill.
                            </li><li style="margin: 0.5em 0em 0em 3em;"> 
                             If correction is made in any entry, immediately click the 'Save' icon to register that correction.
                            </li><li style="margin: 0.5em 0em 0em 3em;">
                             To check correctness of cheque payment instructions, click 'Cheque'. </li>
                         '''},
 'rechecked': {'Auditor2': '''<li style="margin: 0.5em 0em 0em 3em;">
                                   Verify if the Voucher Number entered is correct.
                                </li><li style="margin: 0.5em 0em 0em 3em;">
                                   If not, correct the same and click the 'Save' icon to register the correction.
                                </li><li style="margin: 0.5em 0em 0em 3em;">
                                   To verify the cheque number entries, click 'Cheque'. </li>
                            '''},
 'routed': {'Assignee':''' <li style="margin: 0.5em 0em 0em 3em;">
                              After entering the bill details in the system click the \'Save\' icon.
                              </li><li style="margin: 0.5em 0em 0em 3em;">
                              Then, to enter the cheque payment instructions select \'Add Cheque\' under "Action" If there are no \'Draft\' bills in the Table and you want to enter a new bill, click the \'New\' icon on the top of the screen.
                            </li><li style="margin: 0.5em 0em 0em 3em;">
                               If there are no more bills to be forwarded to Audit, select \'Logout\' under "My Favourites" </li>
                       '''},
 'draft': {'Associate':''' <li style="margin: 0.5em 0em 0em 3em;">
                              After entering the bill details, click the \'Save\' icon.
                            </li><li style="margin: 0.5em 0em 0em 3em;">
                              Then select \'My Comments\' under "Action" to furnish any comments (not compulsory) on the bill which may be useful for the infn of Audit / Accts Assts. </li>
                        '''},
 'audited': {'Cashier2':''' <li style="margin: 0.5em 0em 0em 3em;">
                                First enter the Voucher Number in the space provided for and then click the 'Save' icon to register the entry.
                            </li><li style="margin: 0.5em 0em 0em 3em;">
                                Then to see the cheque payment instructions given by Audit / Accts section, click 'Cheque'. </li>
                        '''},
 'previewed': {'Assignor': ''' <li style="margin: 0.5em 0em 0em 3em;">
                                Check correctness of all entries made by the Asst with the actual bill.
                              </li><li style="margin: 0.5em 0em 0em 3em;">
                                If correction is made in any entry, immediately click the 'Save' icon to register that correction.
                              </li><li style="margin: 0.5em 0em 0em 3em;">
                                In To check correctness of cheque payment instructions entered by the Asst, click 'Cheque'.  </li>
                            '''}
                    }

	help=""
	roleList = self.getRoleList()
	state = self.getSimulationState()

	if bill_help.has_key(state):
		for roll in roleList:
			if bill_help[state].has_key(roll):
				help=help + bill_help[state][roll]
	if help=="":
		help = "You have only view premission "

	return help
	#return "hello"


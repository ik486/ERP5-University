from Products.ERP5Type.XMLObject import XMLObject
from Products.ERP5Type import Permissions, PropertySheet, Constraint
from AccessControl import ClassSecurityInfo

from Products.CMFCore.utils import getToolByName

class AdjustmentBill(XMLObject):

   # CMF Type Definition
   meta_type = 'ERP5 Adjustment Bill'
   portal_type = 'Adjustment Bill'
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
                     , PropertySheet.AdjustmentBill
                     )

   # CMF Factory Type Information
   factory_type_information = \
     {    'id'             : portal_type
        , 'meta_type'      : meta_type
        , 'description'    : '''A Adjustment Bill...'''
        , 'icon'           : 'folder_icon.gif' # should create a new adjustment_bill.gif for the new type...and change folder_icon.gif name
        , 'product'        : 'ERP5'
        , 'factory'        : 'addAdjustmentBill'
        , 'immediate_view' : 'adjustment_bill_view'
        , 'allow_discussion'     : 1
        , 'allowed_content_types': ()
        , 'filter_content_types' : 1
        , 'global_allow'   : 1
        , 'actions'        :
       ( { 'id'            : 'view'
         , 'name'          : 'View'
         , 'category'      : 'object_view'
         , 'action'        : 'adjustment_bill_view'
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
   	EDIT fn of  Adjustment Bill
   	"""
   	if vals.has_key('bill_no'):
   	   self.setBillNo(vals['bill_no'])
   	if vals.has_key('date'):
   	   self.setDate(vals['date'])
   	if vals.has_key('simple_receipt_no'):
   	   self.setSimpleReceiptNo(vals['simple_receipt_no'])
   	if vals.has_key('budget'):
   	   self.setBudget(vals['budget'])
   	if vals.has_key('net_amount_claimed_in_this_bill'):
   	   self.setNetAmountClaimedInThisBill(vals['net_amount_claimed_in_this_bill'])
   	if vals.has_key('deduction_amount'):
   	   self.setDeductionAmount(vals['deduction_amount'])
   	if vals.has_key('refund_amount'):
   	   self.setRefundAmount(vals['refund_amount'])
   	if vals.has_key('forwardedto'):
   	   self.setForwardedto(vals['forwardedto'])
   	if vals.has_key('university_order_no'):
   	   self.setUniversityOrderNo(vals['university_order_no'])
   	if vals.has_key('university_order_date'):
   	   self.setUniversityOrderDate(vals['university_order_date'])
   	if vals.has_key('name_of_supplier'):
   	   self.setNameOfSupplier(vals['name_of_supplier'])
   	if vals.has_key('receipt_no'):
   	   self.setReceiptNo(vals['receipt_no'])
   	if vals.has_key('receipt_date'):
   	   self.setReceiptDate(vals['receipt_date'])
   	if vals.has_key('reasons_for_objection'):
   	   self.setReasonsForObjection(vals['reasons_for_objection'])
        if vals.has_key('voucher_no'):
           self.setVoucherNo(vals['voucher_no'])
        if vals.has_key('description'):
           self.setDescription(vals['description'])


        ############################################################################################3
	self.calSimpleReceiptAmount()
	self.calNetAmountPayable()
	#self.calApprovedGrossAmount()
	#self.calDeductionCalculated()
	#self.calExpenduitureIncludingThisBill()
   	#self.calDepartment()
        ############################################################################################3
        ###########################################################################
        self.calDeductionCalculated()
        self.calApprovedGrossAmount()
        self.calExpenduitureIncludingThisBill()
	self.calBalanceAvalibleInSr()
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


   def getBillState(self):
        """
        """
        return self.getSimulationStateTitle()


   def calculateAll(self):
	"""
	"""
	self.calSimpleReceiptAmount()
	self.calNetAmountPayable()
	self.calApprovedGrossAmount()
	self.calDeductionCalculated()
	self.calExpenduitureIncludingThisBill()
	self.calBalanceAvalibleInSr()

	return

	
   def setNetAmountClaimedInThisBill(self, val):
	"""
	"""
	self.net_amount_claimed_in_this_bill= val
	self.calculateAll()
	return


   def calSimpleReceiptAmount(self):
	uid = self.getSourceUid()
        catalog = getToolByName(self, 'portal_catalog')
        results = catalog(uid=uid)
	if not len(results): val = 0
	else:
		obj = results[0].getObject()
		if obj is None: val = 0
		elif not obj.isOKState():
			val = 0
		else:
			val = obj.getApprovedGrossAmount()
			if not val: val = 0
	out = val
	self.setSimpleReceiptAmount(out)
	return out

   def calBalanceAvalibleInSr(self):
	""" Budget Balance
	"""
	a = self.getExpenduitureIncludingThisBill()
	b = self.getSimpleReceiptAmount()
	if not a: a = 0
	if not b: b = 0
	val = b - a
	if not val: val = 0 
	out = int(val)
	self.setBalanceAvalibleInSr(out)
	return out

   def calBalanceAvalibleInBudget(self):
	""" DUMMY Function
	"""
	
	out = self.calBalanceAvalibleInSr()
	self.calNetAmountPayable()                       #ch
	##############################################################
        """catalog = getToolByName(self, 'portal_catalog')

        uid1 = self.getSourceSectionUid()
        result = catalog(uid=uid1)
        if not len(result):
                self.setBalanceAvalibleInBudget(0)
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
                self.setBalanceAvalibleInBudget(0)
                return 0
        out = int(val)
        #self.setBalanceAvalibleInBudget(out)"""
	return out

   def calNetAmountPayable(self):
	""" Net
	"""
	a = self.getApprovedGrossAmount()
	b = self.getDeductionAmount()
	if not a: a = 0
	if not b: b = 0
	out = a - b
	self.setNetAmountPayable(out)
	return out

   def calExpenduitureIncludingThisBill(self):
	""" ok
	"""
	uid1 = self.getSourceUid()
        catalog = getToolByName(self, 'portal_catalog')
        results = catalog(portal_type='Adjustment Bill')
	if not len(results): 
		out = 0
	else:
	   out = 0
	   for result in results:
		obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
		if obj.getSourceUid() == uid1:
			val = obj.getApprovedGrossAmount()
			if val: 
				out += int(val)

	self.setExpenduitureIncludingThisBill(out)
#________________________________________________________________________________________________________________________________
	self.calBalanceAvalibleInSr()
#________________________________________________________________________________________________________________________________
	return out

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



   def budgetTest(self):
	"""
	"""
	return 1
        self.calBudgetItemAmountSpent()
	self.calBudgetItemBalanceAmount()
	balance_avalible_in_budget = self.getBalanceAvalibleInBudget()
	#net_amount_claimed_in_this_bill = self.getNetAmountClaimedInThisBill()
	out = balance_avalible_in_budget
	if out < 0:
		raise "Revised Budget provision is less than  Gross amount calmed in this bill. \n Check budget head or Add fund diversion ",out 
		out = 0
	else:
	     out=1
	return out


#############################################################################

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
        #pobj = self.getParentValue()
        state = self.getSimulationState()
        if not vals.get(state, None): return 0
        for role in vals[state]:
                if role in roleList: return 1
        return 0



###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

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


   def setRefundAmount(self, val):
	"""
	"""
	self.refund_amount = val
	self.calBudgetItemBudgetAvailable()
	return

#------------------------------------

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


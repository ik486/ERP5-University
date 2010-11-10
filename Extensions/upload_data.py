from xml.dom import minidom   


class IKXML:

	def readXML(self, file = "/opt/data/cusat-finance.xml"):
		self.xmldoc = minidom.parse(file)
		return

        def xmlsafe(self,val):
		if val is None: return None
		val = str(val)
		val = val.replace('&amp;','&')
		val = val.replace('&lt;','<')
		val = val.replace('&gt;','>')
		val = val.replace('&quot;','"')
		val = val.replace("&apos;","'")
		return val

	def getNodeByTagName(self, node, tag):
		out = []
		for n in node.childNodes:
			if n.nodeType == n.ELEMENT_NODE:
				if n.nodeName == tag:
					out.append(n)
		return out
			
        def contentNode(self, mname, cname):
                m = self.getNodeByTagName(self.xmldoc,'MODULES')
                node1 = self.getNodeByTagName(m[0], mname)
                node2 = self.getNodeByTagName(node1[0],cname)
                return node2[0]

	def contentNodeItems(self, mname, cname):
		mname = mname.replace(' ','_')
		cname = cname.replace(' ','_')
		node = self.contentNode(mname, cname)
		node2 = self.getNodeByTagName(node, 'ITEM')
		print 'SIZE :', len(node2)
		return node2

	def subNodeItems(self, node, sname):
		sname = sname.replace(' ','_')
		node1 = self.getNodeByTagName(node, sname)
		node2 = self.getNodeByTagName(node1[0],'ITEM')
		return node2
		
	def node2dict(self, node):
		out = {}
		node1 = self.getNodeByTagName(node, 'VALUE')
		for node2 in node1[0].childNodes:
			if node2.nodeType == node2.ELEMENT_NODE:
				tag = node2.tagName
				for node3 in node2.childNodes:
					if node3.nodeType == node3.TEXT_NODE:
						#if tag.startswith('my_'): tag = tag[3:]
            					out[tag] = self.xmlsafe(node3.data)
		return out



class IKUpload:

        def start(self, portal, catalog, wf):
		self.portal = portal
		self.catalog = catalog
		self.workflowtool = wf
		self.xml = IKXML()
		self.xml.readXML('/opt/data/cusat-finance.xml')
		return

	def set_budget_item(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Budget Item", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		if not state == 'draft':
	        	self.workflowtool.doActionFor(obj, state, comment="")
		obj.setBudgetState(out['my_budget_state'])
		obj.setFinancialYear(out['my_financial_year'])
		obj.setDepartment(out['my_department'])
		obj.setPlanType(out['my_plan_type'])
		obj.setBudgetHead(out['my_budget_head'])
		obj.setBudgetProvision(out['my_budget_provision'])
		obj.setBudgetAvailable(out['my_budget_available'])
		obj.setAmountSpent(out['my_amount_spent'])
		obj.setBalanceAmount(out['my_balance_amount'])
		obj.setLetterReference(out['my_letter_reference'])
		obj.setLetterDate(out['my_letter_date'])
		obj.setUniversityOrder(out['my_university_order'])
		obj.setUniversityOrderDate(out['my_university_order_date'])
		return


	def set_fund_diversion(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Fund Diversion", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		if not state == 'draft':
	        	self.workflowtool.doActionFor(obj, state, comment="")
		obj.setFundDiversionState(out['my_fund_diversion_state'])
		####################################################################
		sbid = out['my_source_budget']
		results = self.catalog(portal_type='Deduction', id=sbid)
		if len(results):
			obj.setSourceBudget(results[0].getObject())

		dbid = out['my_destination_budget']
		results = self.catalog(portal_type='Deduction', id=dbid)
		if len(results):
			obj.setDestinationBudget(results[0].getObject())
		####################################################################
		obj.setTransferAmount(out['my_transfer_amount'])
		obj.setLetterReference(out['my_letter_reference'])
		obj.setLetterDate(out['my_letter_date'])
		obj.setUniversityOrder(out['my_university_order'])
		obj.setUniversityOrderDate(out['my_university_order_date'])
		return


	def set_bill(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Bill", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		obj.setHelp(out['my_help'])
		obj.setReasonsForObjection(out['my_reasons_for_objection'])
		obj.setBillType(out['my_bill_type'])
		obj.setBillNo(out['my_bill_no'])
		obj.setDate(out['my_date'])
		####################################################################
		bid = out['my_budget']
		results = self.catalog(portal_type='Budget Item', id=bid)
		if len(results):
			obj.setBudgetHead(results[0].getObject())
		####################################################################
		obj.setForwardedto(out['my_forwardedto'])
		obj.setNetAmountClaimedInThisBill(out['my_net_amount_claimed_in_this_bill'])
		obj.setApprovedGrossAmount(out['my_approved_gross_amount'])
		obj.setDeductionAmount(out['my_deduction_amount'])
		obj.setNetAmountPayable(out['my_net_amount_payable'])
		obj.setBillState(out['my_bill_state'])
		obj.setVoucherNo(out['my_voucher_no'])
		obj.setUniversityOrderNo(out['my_university_order_no'])
		obj.setUniversityOrderDate(out['my_university_order_date'])
		obj.setNameOfSupplier(out['my_name_of_supplier'])
		obj.setReasonsForObjection(out['my_reasons_for_objection'])
		obj.setFinancialYear(out['my_financial_year'])
		obj.setDepartment(out['my_department'])
		obj.setPlanType(out['my_plan_type'])
		obj.setBudgetHead(out['my_budget_head'])
		obj.setBudgetProvision(out['my_budget_provision'])
		obj.setBudgetAvailable(out['my_budget_available'])
		obj.setExpenduitureIncludingThisBill(out['my_expenduiture_including_this_bill'])
		obj.setBalanceAvalibleInTheBudget(out['my_balance_avalible_in_budget'])
		obj.setDeductionCalculated(out['my_deduction_calculated'])
		for node1 in self.xml.subNodeItems(node,'Sub Bill'):
			self.set_sub_bill(obj, node1)
		for node1 in self.xml.subNodeItems(node,'Cheque'):
			self.set_cheque(obj, node1)
		for node1 in self.xml.subNodeItems(node,'Deduction'):
			self.set_deduction(obj, node1)
		if state == 'draft':
			pass
		elif state == 'submitted':
	        	self.workflowtool.doActionFor(obj, 'submit_action', comment="")
		elif state == 'routed':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
		elif state == 'previewed':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
		elif state == 'verified':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'verify_action', comment="")
		elif state == 'audited':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
		elif state == 'chequenoadded':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
		elif state == 'rechecked':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
		elif state == 'vouchernoadded':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'addvoucherno_action', comment="")
		elif state == 'accounted':
	        	self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'preview_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'addvoucherno_action', comment="")
	        	self.workflowtool.doActionFor(obj, 'account_action', comment="")
		elif state == 'deleted':
	        	self.workflowtool.doActionFor(obj, 'delete_action', comment="")
		else:
	        	self.workflowtool.doActionFor(obj, state, comment="")
		return


	def set_simple_receipt(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Simple Receipt", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		obj.setHelp(out['my_help'])
		obj.setReasonsForObjection(out['my_reasons_for_objection'])
		obj.setBillNo(out['my_bill_no'])
		obj.setDate(out['my_date'])
		####################################################################
		bid = out['my_budget']
		results = self.catalog(portal_type='Budget Item', id=bid)
		if len(results):
			obj.setBudgetHead(results[0].getObject())
		####################################################################
		obj.setForwardedto(out['my_forwardedto'])
		obj.setNetAmountClaimedInThisBill(out['my_net_amount_claimed_in_this_bill'])
		obj.setApprovedGrossAmount(out['my_approved_gross_amount'])
		obj.setDeductionAmount(out['my_deduction_amount'])
		obj.setNetAmountPayable(out['my_net_amount_payable'])
		obj.setBillState(out['my_bill_state'])
		obj.setVoucherNo(out['my_voucher_no'])
		obj.setUniversityOrderNo(out['my_university_order_no'])
		obj.setUniversityOrderDate(out['my_university_order_date'])
		obj.setNameOfSupplier(out['my_name_of_supplier'])
		obj.setReasonsForObjection(out['my_reasons_for_objection'])
		obj.setFinancialYear(out['my_financial_year'])
		obj.setDepartment(out['my_department'])
		obj.setPlanType(out['my_plan_type'])
		obj.setBudgetHead(out['my_budget_head'])
		obj.setBudgetProvision(out['my_budget_provision'])
		obj.setBudgetAvailable(out['my_budget_available'])
		obj.setExpenduitureIncludingThisBill(out['my_expenduiture_including_this_bill'])
		obj.setBalanceAvalibleInTheBudget(out['my_balance_avalible_in_the_budget'])
		obj.setDeductionCalculated(out['my_deduction_calculated'])
		for node1 in self.xml.subNodeItems(node,'Sub Bill'):
			self.set_sub_bill(obj, node1)
		for node1 in self.xml.subNodeItems(node,'Cheque'):
			self.set_cheque(obj, node1)
		for node1 in self.xml.subNodeItems(node,'Deduction'):
			self.set_deduction(obj, node1)
                if state == 'draft':
                        pass
                elif state == 'submitted':
                        self.workflowtool.doActionFor(obj, 'submit_action', comment="")
                elif state == 'routed':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                elif state == 'previewed':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                elif state == 'verified':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verify_action', comment="")
                elif state == 'audited':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                elif state == 'chequenoadded':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                elif state == 'rechecked':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
                elif state == 'vouchernoadded':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addvoucherno_action', comment="")
                elif state == 'accounted':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addvoucherno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'account_action', comment="")
                elif state == 'deleted':
                        self.workflowtool.doActionFor(obj, 'delete_action', comment="")
                else:
                        self.workflowtool.doActionFor(obj, state, comment="")
		return


	def set_adjustment_bill(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Adjustment Bill", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		obj.setHelp(out['my_help'])
		obj.setReasonsForObjection(out['my_reasons_for_objection'])
		obj.setBillNo(out['my_bill_no'])
		obj.setDate(out['my_date'])
		#obj.setSimpleReceiptNo(out['my_simple_receipt_no'])
		####################################################################
		bid = out['my_budget']
		results = self.catalog(portal_type='Budget Item', id=bid)
		if len(results):
			obj.setBudgetHead(results[0].getObject())
		####################################################################
		obj.setForwardedto(out['my_forwardedto'])
		obj.setNetAmountClaimedInThisBill(out['my_net_amount_claimed_in_this_bill'])
		obj.setApprovedGrossAmount(out['my_approved_gross_amount'])
		obj.setDeductionAmount(out['my_deduction_amount'])
		obj.setNetAmountPayable(out['my_net_amount_payable'])
		obj.setRefundAmount(out['my_refund_amount'])
		obj.setBillState(out['my_bill_state'])
		obj.setVoucherNo(out['my_voucher_no'])
		obj.setUniversityOrderNo(out['my_university_order_no'])
		obj.setUniversityOrderDate(out['my_university_order_date'])
		obj.setNameOfSupplier(out['my_name_of_supplier'])
		obj.setReceiptNo(out['my_receipt_no'])
		obj.setReceiptDate(out['my_receipt_date'])
		obj.setReasonsForObjection(out['my_reasons_for_objection'])
		obj.setFinancialYear(out['my_financial_year'])
		obj.setDepartment(out['my_department'])
		obj.setPlanType(out['my_plan_type'])
		obj.setBudgetHead(out['my_budget_head'])
		obj.setBudgetProvision(out['my_budget_provision'])
		obj.setBudgetAvailable(out['my_budget_available'])
		obj.setSimpleReceiptAmount(out['my_simple_receipt_amount'])
		obj.setExpenduitureIncludingThisBill(out['my_expenduiture_including_this_bill'])
		obj.setBalanceAvalibleInSr(out['my_balance_avalible_in_sr'])
		obj.setDeductionCalculated(out['my_deduction_calculated'])
		for node1 in self.xml.subNodeItems(node,'Sub Bill'):
			self.set_sub_bill(obj, node1)
		for node1 in self.xml.subNodeItems(node,'Cheque'):
			self.set_cheque(obj, node1)
		for node1 in self.xml.subNodeItems(node,'Deduction'):
			self.set_deduction(obj, node1)
                if state == 'draft':
                        pass
                elif state == 'submitted':
                        self.workflowtool.doActionFor(obj, 'submit_action', comment="")
                elif state == 'routed':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                elif state == 'previewed':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                elif state == 'verified':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verify_action', comment="")
                elif state == 'audited':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                elif state == 'chequenoadded':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                elif state == 'rechecked':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
                elif state == 'vouchernoadded':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addvoucherno_action', comment="")
                elif state == 'accounted':
                        self.workflowtool.doActionFor(obj, 'submitandroute_action', comment="")
                        self.workflowtool.doActionFor(obj, 'preview_action', comment="")
                        self.workflowtool.doActionFor(obj, 'verifyandaudit_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addchequeno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'recheck_action', comment="")
                        self.workflowtool.doActionFor(obj, 'addvoucherno_action', comment="")
                        self.workflowtool.doActionFor(obj, 'account_action', comment="")
                elif state == 'deleted':
                        self.workflowtool.doActionFor(obj, 'delete_action', comment="")
                else:
                        self.workflowtool.doActionFor(obj, state, comment="")
		return


	def set_deduction(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Deduction", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		if not state == 'draft':
			pass
	        	#self.workflowtool.doActionFor(obj, state, comment="")
		obj.setDeductionState(out['my_deduction_state'])
		#obj.setDeductionType(out['my_deduction_type'])
		obj.setAmount(out['my_amount'])
		return


	def set_sub_bill(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Sub Bill", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		if not state == 'draft':
	        	self.workflowtool.doActionFor(obj, state, comment="")
		obj.setSubBillState(out['my_sub_bill_state'])
		obj.setAmountClaimed(out['my_amount_claimed'])
		obj.setAmountPassed(out['my_amount_passed'])
		return


	def set_cheque(self, pobj, node):
	        out = self.xml.node2dict(node)
	        id = out['id']
	        title = out['title']
	        state = out['state']
	        pobj.invokeFactory("Cheque", id)
	        obj = getattr(pobj, id)
	        obj.setTitle(title)
		if not state == 'draft':
	        	self.workflowtool.doActionFor(obj, state, comment="")
		obj.setChequeState(out['my_cheque_state'])
		obj.setChequeNumber(out['my_check_number'])
		obj.setAmountPayable(out['my_amount_payable'])
		obj.setBalancePayable(out['my_balance_payable'])
		obj.setDate(out['my_date'])
		obj.setChequeInFavorOf(out['my_cheque_in_favor_of'])
		obj.setChequeAmount(out['my_cheque_amount'])
		return


	def set_budget_allocations(self):
		mobj = self.portal.budget_allocations
		for node in self.xml.contentNodeItems('Budget Allocations','Budget Item'):
			self.set_budget_item(mobj, node)
		for node in self.xml.contentNodeItems('Budget Allocations','Fund Diversion'):
			self.set_fund_diversion(mobj, node)


	def set_bills(self):
		mobj = self.portal.bills
		for node in self.xml.contentNodeItems('Bills','Bill'):
			self.set_bill(mobj, node)
		for node in self.xml.contentNodeItems('Bills','Simple Receipt'):
			self.set_simple_receipt(mobj, node)
		for node in self.xml.contentNodeItems('Bills','Adjustment Bill'):
			self.set_adjustment_bill(mobj, node)


def upload_data(self):

	from Products.CMFCore.utils import getToolByName
	context = self

	urltool      = getToolByName(context, 'portal_url')
	portal       = urltool.getPortalObject()

	catalog = getToolByName(portal, 'portal_catalog')
	workflowtool = getToolByName(context, "portal_workflow")

	ik = IKUpload()
	ik.start(portal, catalog, workflowtool)
	ik.set_budget_allocations()
	ik.set_bills()
	return "ok"


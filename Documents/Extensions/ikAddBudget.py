
def ik_add_budget(self):
	from Products.CMFCore.utils import getToolByName
	urltool      = getToolByName(self, "portal_url")
	portal       = urltool.getPortalObject()
	categorytool = getToolByName(portal, "portal_categories")
	catalogtool  = getToolByName(portal, "portal_catalog")
	workflowtool = getToolByName(portal, "portal_workflow")

	#################################################
	#################################################
	#################################################
        from IK.Finance import BUDGET2010

        value = "budget_allocations"
        tree = getattr(portal, value)

        keys1 = BUDGET2010.data.keys()
        keys1.sort()
	No = 500000
	nnoo = 1
	for key1 in keys1:
		for budgets in BUDGET2010.data[key1]:
                                        if not len(budgets) == 4: 
						return nnoo, key1, budgets, BUDGET2010.data[key1]
						break
					nnoo += 1
                                        plan4 = budgets.pop()
                                        nonp4 = budgets.pop()
					key2,key3,key4 = budgets[0].split('-')

                                        head1 = key2
                                        head2 = key2 + "-" + key3
                                        head3 = key2 + "-" + key3 + "-" + key4
                                        budget_head = head1 + "/" + head2 + "/" + head3 
					department = key1
					
					nonp4 = nonp4.replace(',','')
					plan4 = plan4.replace(',','')
					try:
						nonp4 = int(nonp4)
					except:
						nonp4 = 0
					try:
						plan4 = int(plan4)
					except:
						plan4 = 0
					#--------------------------------------------------
					vvv = '1' + department +  head3
					vvv = vvv.replace("-","")
                                        object = getattr(tree, str(vvv), None)
					if object == None:
                                        	vvv = tree.invokeFactory("Budget Item", str(vvv))
                                        	object = getattr(tree, vvv)
					object.setDepartment(department)
					object.setFinancialYear('2010-11')
					object.setPlanType('1')
					object.setBudgetHead(budget_head)
					object.setBudgetProvision(plan4)
					#--------------------------------------------------
					vvv = '2' + department +  head3
					vvv = vvv.replace("-","")
                                        object = getattr(tree, str(vvv), None)
					if object == None:
                                        	vvv = tree.invokeFactory("Budget Item", str(vvv))
                                        	object = getattr(tree, vvv)
					object.setDepartment(department)
					object.setFinancialYear('2010-11')
					object.setPlanType('2')
					object.setBudgetHead(budget_head)
					object.setBudgetProvision(nonp4)

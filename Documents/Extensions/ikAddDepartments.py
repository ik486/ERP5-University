def ik_add_role_category(self):
        from Products.CMFCore.utils import getToolByName
        urltool      = getToolByName(self, "portal_url")
        portal       = urltool.getPortalObject()
        categorytool = getToolByName(portal, "portal_categories")
        catalogtool  = getToolByName(portal, "portal_catalog")
        workflowtool = getToolByName(portal, "portal_workflow")
        ########################################################################
        tree1 = old_category = 'function'
        data = ["AR:assistant_registrar", "SO:section_officer", "AS:assistant"]
        #------------------------------------------------------------------------
        #tree1 = categorytool.invokeFactory('Base Category',old_category)
        tree1 = getattr(categorytool, tree1)
        for kk in data:
		code, k = kk.split(":")
                v = k.replace('_',' ')
                v = v.title()
                key1 = k
                value1 =v
                vvv = tree1.invokeFactory("Category", key1)
                tree2 = getattr(tree1, vvv)
                tree2.setTitle(value1)
                tree2.setShortTitle(value1)
		tree2.setCodification(code)
                tree2.setDescription(value1)
        ########################################################################
        tree1 = old_category = 'group'
        data = ["C1:cash_one", "C2:cash_two", "AU:audit", "A1:accounts_one", "A2:Accounts_two"]
        #------------------------------------------------------------------------
        #tree1 = categorytool.invokeFactory('Base Category',old_category)
        tree1 = getattr(categorytool, tree1)
        for kk in data:
                code, k = kk.split(":")
                v = k.replace('_',' ')
                v = v.title()
                key1 = k
                value1 =v
                vvv = tree1.invokeFactory("Category", key1)
                tree2 = getattr(tree1, vvv)
                tree2.setTitle(value1)
                tree2.setShortTitle(value1)
                tree2.setCodification(code)
                tree2.setDescription(value1)
        ########################################################################
        tree1 = old_category = 'site'
        data = ["MC:main_campus", "LC:lakeside_campus", "KC:kuttanad_campus"]
        #------------------------------------------------------------------------
        #tree1 = categorytool.invokeFactory('Base Category',old_category)
        tree1 = getattr(categorytool, tree1)
        for kk in data:
                code, k = kk.split(":")
                v = k.replace('_',' ')
                v = v.title()
                key1 = k
                value1 =v
                vvv = tree1.invokeFactory("Category", key1)
                tree2 = getattr(tree1, vvv)
                tree2.setTitle(value1)
                tree2.setShortTitle(value1)
                tree2.setCodification(code)
                tree2.setDescription(value1)
        ########################################################################






def ik_add_category(self):
        from Products.CMFCore.utils import getToolByName
        urltool      = getToolByName(self, "portal_url")
        portal       = urltool.getPortalObject()
        categorytool = getToolByName(portal, "portal_categories")
        catalogtool  = getToolByName(portal, "portal_catalog")
        workflowtool = getToolByName(portal, "portal_workflow")
        ########################################################################
        new_category = 'bill_type'
        data = ["contigent_bill", "fellowship", "others", "provident_fund", "salary_bill", "scholarship", "travel_allowance",]
        #------------------------------------------------------------------------
        #tree1 = getattr(categorytool, new_category)
        #if not tree1: return
        vvv = categorytool.invokeFactory('Base Category', new_category)
        tree1 = getattr(categorytool, vvv)
        for k in data:
                v = k.replace('_',' ')
                v = v.title()
                key1 = k
                value1 =v
                vvv = tree1.invokeFactory("Category", key1)
                tree2 = getattr(tree1, vvv)
                tree2.setTitle(value1)
                tree2.setShortTitle(value1)
                tree2.setDescription(value1)
        ########################################################################
	data = {
		"ar_accounts_two":{
			"accounts_b": ['accounts_b1', 'accounts_b2', 'accounts_b3', 'accounts_b4', 'accounts_b5'],
			"audit_c": ['audit_c1', 'audit_c2', 'audit_c3', 'audit_c4', 'audit_c5']},
		"ar_audit":{
			"audit_a": ['audit_a1', 'audit_a2', 'audit_a3', 'audit_a4', 'audit_a5'],
			"audit_b": ['audit_b1', 'audit_b2', 'audit_b3', 'audit_b4', 'audit_b5']}
	}

        #------------------------------------------------------------------------
        new_category = 'forwardedto'
        vvv = categorytool.invokeFactory('Base Category', new_category)
        tree1 = getattr(categorytool, vvv)
	keys1 = data.keys()
	keys1.sort()
        for key1 in keys1:
                value1 = key1.replace('_',' ')
                value1 = value1.title()
                vvv = tree1.invokeFactory("Category", key1)
                tree2 = getattr(tree1, vvv)
                tree2.setTitle(value1)
                tree2.setShortTitle(value1)
                tree2.setDescription(value1)

		keys2 = data[key1].keys()
		keys2.sort()
        	for key2 in keys2:
                	value2 = key2.replace('_',' ')
	                value2 = value2.title()
        	        vvv = tree2.invokeFactory("Category", key2)
	                tree3 = getattr(tree2, vvv)
	                tree3.setTitle(value2)
	                tree3.setShortTitle(value2)
        	        tree3.setDescription(value2)
        		for key3 in data[key1][key2]:
                		value3 = key3.replace('_',' ')
		                value3 = value3.title()
        		        vvv = tree3.invokeFactory("Category", key3)
	        	        tree4 = getattr(tree3, vvv)
	                	tree4.setTitle(value3)
		                tree4.setShortTitle(value3)
	        	        tree4.setDescription(value3)
        ########################################################################

def ik_add_departments(self):
	from Products.CMFCore.utils import getToolByName
	urltool      = getToolByName(self, "portal_url")
	portal       = urltool.getPortalObject()
	categorytool = getToolByName(portal, "portal_categories")
	catalogtool  = getToolByName(portal, "portal_catalog")
	workflowtool = getToolByName(portal, "portal_workflow")

	#################################################
	#################################################
        from IK.Finance import departments

	vvv = categorytool.invokeFactory('Base Category','department')
	tree = getattr(categorytool, vvv)
	keys = departments.DEPARTMENTS.keys()
	keys.sort()
	for key in keys:
		objValue = key
		value = departments.DEPARTMENTS[key]
		tree.invokeFactory("Category", objValue)
		object = getattr(tree, objValue)
		object.setTitle(key + " : " + value) 	
		object.setShortTitle(value)
		object.setDescription(key + " : " + value)

	#################################################
	#################################################
        from IK.Finance import budgetheads

	keys1 = budgetheads.MAJORHEADS.keys()
	keys1.sort()
	keys2 = budgetheads.MINORHEADS.keys()
	keys2.sort()
	keys3 = budgetheads.SUBHEADS.keys()
	keys3.sort()
	vvv = categorytool.invokeFactory('Base Category','budget_head')
	tree1 = getattr(categorytool, vvv)
	for key1 in keys1:
		value1 = budgetheads.MAJORHEADS[key1]
		vvv = tree1.invokeFactory("Category", key1)
		tree2 = getattr(tree1, vvv)
		tree2.setTitle(key1 + " : " + value1) 	
		tree2.setShortTitle(value1)
		tree2.setDescription(key1 + " : " + value1)
		for key2 in keys2:
			if not key2.startswith(key1): continue
			value2 = budgetheads.MINORHEADS[key2]
			vvv = tree2.invokeFactory("Category", key2)
			tree3 = getattr(tree2, vvv)
			tree3.setTitle(key2 + " : " + value2) 	
			tree3.setShortTitle(value2)
			tree3.setDescription(key2 + " : " + value2)
			for key3 in keys3:
				if not key3.startswith(key2): continue
				value3 = budgetheads.SUBHEADS[key3]
				vvv = tree3.invokeFactory("Category", key3)
				tree4 = getattr(tree3, vvv)
				tree4.setTitle(key3 + " : " + value3) 	
				tree4.setShortTitle(value3)
				tree4.setDescription(key3 + " : " + value3)
	#################################################
	tree1 = categorytool.invokeFactory('Base Category','plan_type')
	tree1 = getattr(categorytool, tree1)
	key1 = "1"
	value1 = "Plan"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(value1)
	tree2.setDescription(key1 + " : " + value1)
	key1 = "2"
	value1 = "Non Plan"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(value1)
	tree2.setDescription(key1 + " : " + value1)
	#################################################
	tree1 = categorytool.invokeFactory('Base Category','financial_year')
	tree1 = getattr(categorytool, tree1)
	key1 = "2008-09"
	value1 = "2008-09"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(key1)
	tree2.setDescription("Year 2008 March 1 to 2009 February 28")
	key1 = "2009-10"
	value1 = "2009-10"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(key1)
	tree2.setDescription("Year 2009 March 1 to 2010 February 28")
	key1 = "2010-11"
	value1 = "2010-11"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(key1)
	tree2.setDescription("Year 2010 March 1 to 2011 February 28")
	key1 = "2011-12"
	value1 = "2011-12"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(key1)
	tree2.setDescription("Year 2011 March 1 to 2012 February 28")
	#################################################
        #tree1 = categorytool.invokeFactory('Base Category','gender')
        tree1 = getattr(categorytool, 'gender')
	key1 = "Male"
	value1 = "Male"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(key1)
	tree2.setDescription(value1)

	key1 = "Female"
	value1 = "Female"
	vvv = tree1.invokeFactory("Category", key1)
	tree2 = getattr(tree1, vvv)
	tree2.setTitle(value1) 	
	tree2.setShortTitle(key1)
	tree2.setDescription(value1)
	#################################################

	#################################################
	#ch________________________________________________________
	#################################################
	from IK.Finance import deductions

	vvv = categorytool.invokeFactory('Base Category','deduction_type')
	tree = getattr(categorytool, vvv)
	keys = deductions.DEDUCTIONS.keys()
	keys.sort()
	for key in keys:
		objValue = key
#		value = deductions.DEDUCTIONS[key]
		stitle = deductions.DEDUCTIONS[key][0]
		descrip = deductions.DEDUCTIONS[key][1]

		tree.invokeFactory("Category", objValue)
		object = getattr(tree, objValue)
		object.setTitle(key) 	
		object.setShortTitle(key)
		object.setDescription(stitle+",  "+descrip)

	#################################################
	#ch________________________________________________________
	#################################################
      



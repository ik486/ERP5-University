def finance_fns(self):
        from Products.ExternalMethod.ExternalMethod import manage_addExternalMethod

        context = self
	#############################################################################
        fn_name = "ik_add_departments"
	module  = "ikAddDepartments"
	notes   = "Add Departments"
	name = fn_name
        if not name in context.objectIds():
                manage_addExternalMethod(self, name, notes, module, fn_name)
	#############################################################################
        fn_name = "ik_add_category"
	module  = "ikAddDepartments"
	notes   = "Add Forwarded to, Bill Type"
	name = fn_name
        if not name in context.objectIds():
                manage_addExternalMethod(self, name, notes, module, fn_name)
	#############################################################################
        fn_name = "ik_add_role_category"
	module  = "ikAddDepartments"
	notes   = "Add function, group and site"
	name = fn_name
        if not name in context.objectIds():
                manage_addExternalMethod(self, name, notes, module, fn_name)
	#############################################################################
        #fn_name = "ik_add_persons"
	#module  = "ikAddPersons"
	#notes   = "Add Persons"
	#name = fn_name
        #if not name in context.objectIds():
        #        manage_addExternalMethod(self, name, notes, module, fn_name)
	#############################################################################
        fn_name = "ik_add_budget"
	module  = "ikAddBudget"
	notes   = "Add Budget"
	name = fn_name
        if not name in context.objectIds():
                manage_addExternalMethod(self, name, notes, module, fn_name)
	#############################################################################
        fn_name = "ik_add_role_information"
	module  = "ikAddRoleInformation"
	notes   = "Add Role Informations"
	name = fn_name
        if not name in context.objectIds():
                manage_addExternalMethod(self, name, notes, module, fn_name)
	#############################################################################

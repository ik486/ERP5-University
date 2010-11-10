def ik_add_role_information(self):
        from Products.CMFCore.utils import getToolByName
        urltool      = getToolByName(self, "portal_url")
        portal       = urltool.getPortalObject()
        categorytool = getToolByName(portal, "portal_categories")
        catalogtool  = getToolByName(portal, "portal_catalog")
        workflowtool = getToolByName(portal, "portal_workflow")
        ########################################################################
        tree1 = portal.portal_types.Bill
        data  = [
                        ['Assistant Cash One','Associate', 'assistant' ,'cash_one','main_campus'],
			['Assistant Audit', 'Assignee', 'assistant', 'audit','main_campus'],
			['Assistant Accounts Two', 'Assignee', 'assistant', 'accounts_two','main_campus'],
			['SO Audit', 'Assignor', 'section_officer', 'audit','main_campus'],
			['SO Accounts two', 'Assignor', 'section_officer', 'accounts_two','main_campus'],
			['AR Audit', 'Auditor', 'assistant_registrar', 'audit','main_campus'],
			['AR Accounts Two', 'Auditor', 'assistant_registrar', 'accounts_two','main_campus'],
			['Assistant Cash two', 'Cashier2', 'assistant', 'cash_two','main_campus'],
			['SO Cash Two', 'Cashier', 'assistant', 'cash_two','main_campus'],
			['AR Cash Two', 'Auditor2', 'assistant', 'cash_two','main_campus'],
			['Assistant Accounts One', 'Accountant', 'assistant', 'accounts_one','main_campus']
                ]
        cc = ['function', 'group', 'site']
        #------------------------------------------------------------------------
        i = 0
        for kk in data:
                title, role, fn1, group1, site1 = kk
                dd = [ cc[0]+'/'+fn1, cc[1]+'/'+group1, cc[2]+'/'+site1]
                i += 1
                key1 = "role" + "%03d" % (i)
                key1 = tree1.invokeFactory('Role Information',key1)

                tree2 = getattr(tree1, key1)
                tree2.setTitle(title)
                tree2.setRoleNameList([role])
                tree2.setRoleCategoryList(dd)
                tree2.setRoleBaseCategoryList(cc)


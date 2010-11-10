
def ik_add_persons(self):
	from Products.CMFCore.utils import getToolByName
	urltool      = getToolByName(self, "portal_url")
	portal       = urltool.getPortalObject()
	categorytool = getToolByName(portal, "portal_categories")
	catalogtool  = getToolByName(portal, "portal_catalog")
	workflowtool = getToolByName(portal, "portal_workflow")

	#################################################
	#################################################
        from IK.Finance import cusatemploies

	tree = portal.person_module
	data = cusatemploies.data
	for d in data:
		vvv = d['employ_number']
                object = getattr(tree, str(vvv), None)
                if object == None:
			vvv = tree.invokeFactory("Person", str(vvv))
		object = getattr(tree, str(vvv))

		vvv = d['first_name']
		object.setFirstName(vvv) 	

		vvv = d['last_name']
		object.setLastName(vvv) 	

		vvv = d['street_address']
		object.setDefaultAddressStreetAddress(vvv) 	

		vvv = d['telephone']
		object.setDefaultTelephoneText(vvv) 	

		vvv = d['email']
		object.setDefaultEmailText(vvv) 	

		vvv = d['gender']
		if vvv == 'M': 
			vvv = 'Male'
			object.setDefaultEmailText(vvv) 	
		elif vvv == 'F': 
			vvv = 'Female'
			object.setDefaultEmailText(vvv) 	


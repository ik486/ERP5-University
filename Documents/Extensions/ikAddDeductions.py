
def ik_add_deductions(self):
	from Products.CMFCore.utils import getToolByName
	urltool      = getToolByName(self, "portal_url")
	portal       = urltool.getPortalObject()
	categorytool = getToolByName(portal, "portal_categories")
	catalogtool  = getToolByName(portal, "portal_catalog")
	workflowtool = getToolByName(portal, "portal_workflow")

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
      


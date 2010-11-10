from Products.ERP5Type.XMLObject import XMLObject

from Products.ERP5Type import Permissions, PropertySheet, Constraint

from AccessControl import ClassSecurityInfo

from Products.CMFCore.utils import getToolByName

class Cheque(XMLObject):

   # CMF Type Definition
   meta_type = 'ERP5 Cheque'
   portal_type = 'Cheque'
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
                     , PropertySheet.Cheque
                     )

   # CMF Factory Type Information
   factory_type_information = \
     {    'id'             : portal_type
        , 'meta_type'      : meta_type
        , 'description'    : '''A Cheque...'''
        , 'icon'           : 'folder_icon.gif' # should create a new cheque.gif for the new type...and change folder_icon.gif name
        , 'product'        : 'ERP5'
        , 'factory'        : 'addCheque'
        , 'immediate_view' : 'cheque_view'
        , 'allow_discussion'     : 1
        , 'allowed_content_types': ()
        , 'filter_content_types' : 1
        , 'global_allow'   : 1
        , 'actions'        :
       ( { 'id'            : 'view'
         , 'name'          : 'View'
         , 'category'      : 'object_view'
         , 'action'        : 'cheque_view'
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
   	EDIT fn of  Cheque
   	"""
   	if vals.has_key('check_number'):
   	   self.setCheckNumber(vals['check_number'])
   	if vals.has_key('date'):
   	   self.setDate(vals['date'])
   	if vals.has_key('cheque_in_favor_of'):
   	   self.setChequeInFavorOf(vals['cheque_in_favor_of'])
   	if vals.has_key('cheque_amount'):
   	   self.setChequeAmount(vals['cheque_amount'])
        if vals.has_key('description'):
           self.setDescription(vals['description'])

	#######################################################################
	return



   def isOKState(self):
        """
        """
        state = self.getSimulationState()
        if state in ['deleted', 'cancelled']: return 0
        return 1


   def getAmountPayable(self):
        """
        """
	obj = self.getParentValue()
	if obj is None: return 0
	out = obj.getNetAmountPayable()
	if out is None: return 0
	return out


   def getBalancePayable(self):
        """
        """
        catalog = getToolByName(self, 'portal_catalog')
        uid = self.getParentUid()
        results = catalog(portal_type='Cheque', parent_uid=uid)
        out = 0
        if not len(results):
                out = 0
        else:
           for result in results:
                obj = result.getObject()
		if obj is None: continue
		if not obj.isOKState(): continue
                val = obj.getChequeAmount()
                if not val is None:
                        out += int(val)
	
	bal = self.getAmountPayable() - out
	return	bal
	
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
        pobj = self.getParentValue()
        state = pobj.getSimulationState()
        if not vals.get(state, None): return 0
        for role in vals[state]:
                if role in roleList: return 1
        return 0


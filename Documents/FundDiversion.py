from Products.ERP5Type.XMLObject import XMLObject

from Products.ERP5Type import Permissions, PropertySheet, Constraint

from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName

class FundDiversion(XMLObject):

   # CMF Type Definition
   meta_type = 'ERP5 Fund Diversion'
   portal_type = 'Fund Diversion'
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
                     , PropertySheet.FundDiversion
                     )

   # CMF Factory Type Information
   factory_type_information = \
     {    'id'             : portal_type
        , 'meta_type'      : meta_type
        , 'description'    : '''A Fund Diversion...'''
        , 'icon'           : 'folder_icon.gif' # should create a new fund_diversion.gif for the new type...and change folder_icon.gif name
        , 'product'        : 'ERP5'
        , 'factory'        : 'addFundDiversion'
        , 'immediate_view' : 'fund_diversion_view'
        , 'allow_discussion'     : 1
        , 'allowed_content_types': ()
        , 'filter_content_types' : 1
        , 'global_allow'   : 1
        , 'actions'        :
       ( { 'id'            : 'view'
         , 'name'          : 'View'
         , 'category'      : 'object_view'
         , 'action'        : 'fund_diversion_view'
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
   	EDIT fn of  Fund Diversion
   	"""
   	if vals.has_key('source_budget'):
   	   self.setSourceBudget(vals['source_budget'])
   	if vals.has_key('destination_budget'):
   	   self.setDestinationBudget(vals['destination_budget'])
   	if vals.has_key('transfer_amount'):
   	   self.setTransferAmount(vals['transfer_amount'])
   	if vals.has_key('letter_reference'):
   	   self.setLetterReference(vals['letter_reference'])
   	if vals.has_key('letter_date'):
   	   self.setLetterDate(vals['letter_date'])
   	if vals.has_key('university_order'):
   	   self.setUniversityOrder(vals['university_order'])
   	if vals.has_key('university_order_date'):
   	   self.setUniversityOrderDate(vals['university_order_date'])
	##########################################################################
        self.calBudgetAvailable()
	return



   def isOKState(self):
        """
        """
        state = self.getState()
        if state in ['deleted', 'cancelled']: return 0
        return 1




   def calBudgetAvailable(self):
        """ Available
        """
        catalog = getToolByName(self, 'portal_catalog')

        suid = self.getSourceSectionUid()
	if not suid is None:
	        results = catalog(uid=suid)
		if len(results):
			results[0].calBudgetAvailable()

        duid = self.getDestinationSectionUid()
	if not duid is None:
	        results = catalog(uid=duid)
		if len(results):
			results[0].calBudgetAvailable()

        return 


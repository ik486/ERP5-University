
#############################################################################################################
#############################################################################################################

class Test:
	def __init__(self):
		self.fields=["CategoryField", "StringField","LinesField","IntegerField","BooleanField",
			"DateTimeField","ImageField","FileField","FixedPointField",
			"RelationField","CMFObjectField","ComputedField","TextField","DataGridField"]

		self.widgets = {'StringField' : ['LabelWidget','StringWidget','SelectionWidget','PasswordWidget',
						'IdWidget','RequiredIdWidget','VisualWidget','EpozWidget'],
    				'LinesField' : ['KeywordWidget','LinesWidget','LabelWidget',
						'MultiSelectionWidget','PickSelectionWidget','InAndOutWidget'],
    				'IntegerField' : ['LabelWidget','IntegerWidget'],
    				'BooleanField' : ['LabelWidget','BooleanWidget'],
    				'DateTimeField' : ['CalendarWidget'],
				'DataGridField' : ['DataGridWidget'],
    				'ImageField' : ['LabelWidget','ImageWidget'],
    				'FileField' : ['LabelWidget','FileWidget'],
    				'FixedPointField' : ['LabelWidget','DecimalWidget'],
    				'RelationField' : ['StringWidget','ReferenceWidget','ReferenceBrowserWidget','LabelWidget','InAndOutWidget'],
    				'CMFObjectField' : ['LabelWidget','FileWidget'],
    				'ComputedField' : ['LabelWidget','ComputedWidget'],
    				'CategoryField' : ['CategoryWidget'],
    				'TextField' : ['LabelWidget','TextAreaWidget','RichWidget','StringWidget']}
	def fieldTest(self, objs):
		out = True
		for obj in objs:
			for fld in obj.ikfields:
				no = self.fields.count(fld[1])
				if no != 1:
					print "Field Error in %s field %s" % (obj.type_name, fld[1]) 
					out = False
		return out

	def widgetTest(self, objs):
		out = True
		return out

	def ok(self, objs):
		if self.fieldTest(objs):
			if self.widgetTest(objs):
				print "ALL Tests Done"

#############################################################################################################
#############################################################################################################
contents = []
#############################################################################################################
class Content:
	def __init__(self, name):
		self.project_head = 'Uty'
		self.public = False
		self.type_name = name
		self.ikfields = []
		self.allowed_content_types = []
		self.tab_types = []
		self.content_type = True

#############################################################################################################
#-----------------------------------------------------------------------------------------------------------#
#------------------------------------Begin of Code Block----------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
#############################################################################################################


#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
obj = Content('Budget Allocations')
obj.public = True
contents.append(obj)


obj.allowed_content_types = ['Budget Item', 'Fund Diversion']
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
obj = Content('Budget Item')
contents.append(obj)
# E=EDIT, L=LEFT, R=RIGHT, B=BOTTOM, C=CENTER,	To=TOP

obj.ikfields.append(['Budget State', 'StringField', 'StringWidget','Budget State',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Financial Year', 'CategoryField', 'CategoryWidget','Financial Year',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Department', 'CategoryField', 'CategoryWidget','Department',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':1}])
obj.ikfields.append(['Plan Type', 'CategoryField', 'CategoryWidget','Plan Type',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Budget Head', 'CategoryField', 'CategoryWidget','Budget Head',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Budget Provision', 'IntegerField', 'IntegerWidget', 'Original Budget Provision',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Budget Available', 'IntegerField', 'IntegerWidget', 'Revised Budget Provision', {'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':1}])
obj.ikfields.append(['Amount Spent', 'IntegerField', 'IntegerWidget','Amount Spent',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':1}])
obj.ikfields.append(['Balance Amount', 'IntegerField', 'IntegerWidget','Balance Amount',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':1}])
obj.ikfields.append(['Letter Reference', 'StringField', 'StringWidget','Letter Reference', {'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0}])
obj.ikfields.append(['Letter Date', 'DateTimeField', 'CalendarWidget','Letter Date',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0}])
obj.ikfields.append(['University Order', 'StringField', 'StringWidget','University Order',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0}])
obj.ikfields.append(['University Order Date', 'DateTimeField', 'CalendarWidget','University Order Date',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0}])

obj.allowed_content_types = []

################################################################################################################ new add by ch 
obj = Content('Fund Diversion')
contents.append(obj)

obj.ikfields.append(['Fund Diversion State', 'StringField', 'StringWidget','Fund Diversion State',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Source Budget', 'RelationField', 'source_section','Budget Item','Source Budget',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Destination Budget', 'RelationField', 'destination_section','Budget Item','Destination Budget',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Transfer Amount', 'FixedPointField', 'DecimalWidget','Transfer Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Letter Reference', 'StringField', 'StringWidget','Letter Reference',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['Letter Date', 'DateTimeField', 'CalendarWidget','Letter Date', {'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['University Order', 'StringField', 'StringWidget','University Order',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])
obj.ikfields.append(['University Order Date', 'DateTimeField', 'CalendarWidget','University Order Date',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1}])


obj.allowed_content_types = []

#############################################################################################################                  Bills
#############################################################################################################
#############################################################################################################
#############################################################################################################
obj = Content('Bills')
obj.public = True
contents.append(obj)
obj.ikfields.append(['Help', 'TextField', 'TextAreaWidget',{'R' :0, 'C' :0, 'To':1,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Voucher No', 'StringField', 'StringWidget',{'R' :0, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])  
obj.allowed_content_types = ['Bill','Simple Receipt','Adjustment Bill']

#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
obj = Content('Bill')
contents.append(obj)
#--------------------------------------------------------------------------------------------top
obj.ikfields.append(['Help', 'TextField', 'TextAreaWidget',{'R' :0, 'C' :0, 'To':1,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Objection', 'TextField', 'TextAreaWidget','Objection', {'R' :1, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])
 #for showing the reson of objection 2nd or 3ed time bill recycle  
#--------------------------------------------------------------------------------------------left
obj.ikfields.append(['Bill Type', 'CategoryField', 'CategoryWidget',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Bill No', 'StringField', 'StringWidget','Bill No',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Date', 'DateTimeField', 'CalendarWidget','Date', {'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor']])"}])
obj.ikfields.append(['Budget', 'RelationField', 'source_section', 'Budget Item','Budget Head',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Forwardedto','CategoryField', 'CategoryWidget','Forwarded To',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'], routed=['Associate'])"}])
obj.ikfields.append(['Net Amount Claimed in this bill', 'IntegerField', 'IntegerWidget','Gross Amount Claimed In This Bill',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Approved Gross Amount', 'IntegerField', 'IntegerWidget','Approved Gross Amount',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Deduction Amount', 'FixedPointField', 'DecimalWidget','Deduction Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Net Amount Payable', 'IntegerField', 'IntegerWidget','Net Amount Payable',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])


#--------------------------------------------------------------------------------------------right
obj.ikfields.append(['Bill State', 'StringField', 'StringWidget','Bill State',{'R' :1, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Voucher No', 'StringField', 'StringWidget','Voucher No',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(rechecked=['Auditor2'], chequenoadded=['Cashier'],audited=['Cashier2'])"}])  
obj.ikfields.append(['University Order No', 'StringField', 'StringWidget','University Order No', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])   
obj.ikfields.append(['University Order Date', 'DateTimeField', 'CalendarWidget','University Order Date',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Name of Supplier', 'StringField', 'StringWidget','Advance Drawn By',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Reasons for Objection', 'TextField', 'TextAreaWidget','Reasons for Objection', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])

#--------------------------------------------------------------------------------------------center
obj.ikfields.append(['Financial Year', 'CategoryField', 'CategoryWidget','Financial Year',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Department', 'CategoryField', 'CategoryWidget','Department',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Plan Type', 'CategoryField', 'CategoryWidget','Plan Type',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Head', 'CategoryField', 'CategoryWidget','Budget Head',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Provision', 'IntegerField', 'IntegerWidget','Budget Provision',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Available', 'IntegerField', 'IntegerWidget','Budget Available',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Expenduiture including this bill', 'IntegerField', 'IntegerWidget','Expenduiture including this bill',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Balance Avalible in the budget', 'IntegerField', 'IntegerWidget','Balance Avalible in the budget', {'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Deduction Calculated', 'FixedPointField', 'DecimalWidget','Deduction Calculated',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
#--------------------------------------------------------------------------------------------bottom

obj.allowed_content_types = ['Sub Bill','Cheque','Deduction']



#############################################################################################################
obj = Content('Simple Receipt')
contents.append(obj)

#--------------------------------------------------------------------------------------------top
obj.ikfields.append(['Help', 'TextField', 'TextAreaWidget','Help',{'R' :0, 'C' :0, 'To':1,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Objection', 'TextField', 'TextAreaWidget','Objection', {'R' :1, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])

#--------------------------------------------------------------------------------------------left
obj.ikfields.append(['Bill No', 'StringField', 'StringWidget','Bill No',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Date', 'DateTimeField', 'CalendarWidget','Date', {'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Budget', 'RelationField', 'source_section', 'Budget Item','Budget Head',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Forwardedto','CategoryField', 'CategoryWidget','Forwarded To',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'], routed=['Associate'])"}])
obj.ikfields.append(['Net Amount Claimed in this bill', 'IntegerField', 'IntegerWidget','Gross Amount Claimed In This Bill ',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Approved Gross Amount', 'IntegerField', 'IntegerWidget','Approved Gross Amount',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Deduction Amount', 'FixedPointField', 'DecimalWidget','Deduction Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Net Amount Payable', 'IntegerField', 'IntegerWidget','Net Amount Payable',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])


#--------------------------------------------------------------------------------------------right
obj.ikfields.append(['Bill State', 'StringField', 'StringWidget','Bill State',{'R' :1, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Voucher No', 'StringField', 'StringWidget','Voucher No',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(rechecked=['Auditor2'], chequenoadded=['Cashier'],audited=['Cashier2'])"}])  
obj.ikfields.append(['University Order No', 'StringField', 'StringWidget','University Order No', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])   
obj.ikfields.append(['University Order Date', 'DateTimeField', 'CalendarWidget','University Order Date',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Name of Supplier', 'StringField', 'StringWidget','Advance Drawn By',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Reasons for Objection', 'TextField', 'TextAreaWidget','Reasons for Objection', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])

#--------------------------------------------------------------------------------------------center
obj.ikfields.append(['Financial Year', 'CategoryField', 'CategoryWidget','Financial Year',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Department', 'CategoryField', 'CategoryWidget','Department',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Plan Type', 'CategoryField', 'CategoryWidget','Plan Type',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Head', 'CategoryField', 'CategoryWidget','Budget Head',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Provision', 'IntegerField', 'IntegerWidget','Budget Provision',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Available', 'IntegerField', 'IntegerWidget','Budget Available',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Expenduiture including this bill', 'IntegerField', 'IntegerWidget','Expenduiture including this bill',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Balance Avalible in the budget', 'IntegerField', 'IntegerWidget','Balance Avalible in the budget', {'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Deduction Calculated', 'FixedPointField', 'DecimalWidget','Deduction Calculated',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
#--------------------------------------------------------------------------------------------bottom

obj.allowed_content_types = ['Sub Bill','Cheque','Deduction']



#############################################################################################################
obj = Content('Adjustment Bill')
contents.append(obj)
#--------------------------------------------------------------------------------------------top
obj.ikfields.append(['Help', 'TextField', 'TextAreaWidget','Help',{'R' :0, 'C' :0, 'To':1,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Objection', 'TextField', 'TextAreaWidget','Objection', {'R' :1, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])

#--------------------------------------------------------------------------------------------left
obj.ikfields.append(['Bill No', 'StringField', 'StringWidget','Bill No',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Date', 'DateTimeField', 'CalendarWidget','Date',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Simple Receipt No', 'RelationField', 'source', 'Simple Receipt','Simple Receipt No',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Budget', 'RelationField', 'source_section', 'Budget Item','Budget Head',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Forwardedto','CategoryField', 'CategoryWidget','Forwarded To',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Associate'])"}])
obj.ikfields.append(['Net Amount Claimed in this bill', 'IntegerField', 'IntegerWidget','Gross Amount Claimed In This Bill ',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(draft=['Associate'],routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Approved Gross Amount', 'IntegerField', 'IntegerWidget','Approved Gross Amount',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Deduction Amount', 'FixedPointField', 'DecimalWidget','Deduction Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Net Amount Payable', 'IntegerField', 'IntegerWidget','Net Amount Payable',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Refund Amount', 'FixedPointField', 'DecimalWidget','Refund Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])

#--------------------------------------------------------------------------------------------right
obj.ikfields.append(['Bill State', 'StringField', 'StringWidget','Bill State',{'R' :1, 'C' :0, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Voucher No', 'StringField', 'StringWidget','Voucher No',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(rechecked=['Auditor2'], chequenoadded=['Cashier'],audited=['Cashier2'])"}])  
obj.ikfields.append(['University Order No', 'StringField', 'StringWidget','University Order No',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])   
obj.ikfields.append(['University Order Date', 'DateTimeField', 'CalendarWidget','University Order Date',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Name of Supplier', 'StringField', 'StringWidget','Advance Drawn By', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Receipt No', 'StringField', 'StringWidget','Receipt No', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Receipt Date', 'DateTimeField', 'CalendarWidget','Receipt Date',{'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Reasons for Objection', 'TextField', 'TextAreaWidget','Reasons for Objection', {'R' :1, 'C' :0, 'To':0,'E':1,'L':0,'B':0,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
#--------------------------------------------------------------------------------------------center

obj.ikfields.append(['Financial Year', 'CategoryField', 'CategoryWidget','Financial Year',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Department', 'CategoryField', 'CategoryWidget','Department',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Plan Type', 'CategoryField', 'CategoryWidget','Plan Type',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Head', 'CategoryField', 'CategoryWidget','Budget Head',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Provision', 'IntegerField', 'IntegerWidget','Budget Provision',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Budget Available', 'IntegerField', 'IntegerWidget', 'Revised Budget Provision', {'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Simple Receipt Amount','IntegerField', 'IntegerWidget','Simple Receipt Amount',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}]) 
obj.ikfields.append(['Expenduiture including this bill', 'IntegerField', 'IntegerWidget','Expenduiture including this bill', {'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':1}])
obj.ikfields.append(['Balance Avalible in SR', 'IntegerField', 'IntegerWidget','Balance Avalible in SR',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])
obj.ikfields.append(['Deduction Calculated', 'FixedPointField', 'DecimalWidget', 'Deduction Calculated',{'R' :0, 'C' :1, 'To':0,'E':0,'L':0,'B':0}])

#--------------------------------------------------------------------------------------------bottom

obj.allowed_content_types = ['Sub Bill','Cheque','Deduction']


###############################################################################################
###############################################################################################
###############################################################################################
obj = Content('Deduction')

contents.append(obj)

obj.ikfields.append(['Deduction State', 'StringField', 'StringWidget','Deduction State',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Deduction Type', 'CategoryField', 'CategoryWidget','Deduction Type',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(routed=['Assignee'])"}])
#obj.ikfields.append(['Deduction Type', 'RelationField', 'source_section', 'Budget Item'])
obj.ikfields.append(['Amount', 'IntegerField', 'IntegerWidget','Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(routed=['Assignee'])"}])

obj.allowed_content_types = []
###############################################################################################

obj = Content('Sub Bill')

contents.append(obj)

obj.ikfields.append(['Sub Bill State', 'StringField', 'StringWidget','Sub Bill State',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Amount Claimed', 'IntegerField', 'IntegerWidget','Amount Claimed',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.ikfields.append(['Amount Passed', 'IntegerField', 'IntegerWidget','Amount Passed',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])

obj.allowed_content_types = []
#############################################################################################################
obj = Content('Cheque')

contents.append(obj)

obj.ikfields.append(['Cheque State', 'StringField', 'StringWidget','Cheque State',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':0}])
obj.ikfields.append(['Cheque Number', 'StringField', 'StringWidget','Cheque Number',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(rechecked=['Auditor2'], chequenoadded=['Cashier'],audited=['Cashier2'])"}])
obj.ikfields.append(['Amount Payable', 'IntegerField', 'IntegerWidget','Amount Payable',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':1}])
obj.ikfields.append(['Balance Payable', 'IntegerField', 'IntegerWidget','Balance Payable',{'R' :0, 'C' :0, 'To':0,'E':0,'L':1,'B':1}])
obj.ikfields.append(['Date', 'DateTimeField', 'CalendarWidget','Date',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(rechecked=['Auditor2'], chequenoadded=['Cashier'],audited=['Cashier2'])"}])
obj.ikfields.append(['Cheque In Favor Of','TextField', 'TextAreaWidget','Cheque In Favor Of',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'],rechecked=['Auditor2'], chequenoadded=['Cashier'],audited=['Cashier2'])"}])
obj.ikfields.append(['Cheque Amount', 'IntegerField', 'IntegerWidget','Cheque Amount',{'R' :0, 'C' :0, 'To':0,'E':1,'L':1,'B':1,'T':"python:context.editAny(routed=['Assignee'],previewed=['Assignor'],verified=['Auditor'])"}])
obj.allowed_content_types = []
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################


#############################################################################################################
#-----------------------------------------------------------------------------------------------------------#
#------------------------------------END of Code Block------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
#############################################################################################################



def list_names(objs):
	print "============================================================================"
	for obj in objs:
		out = "%24s -> %s" % (obj.type_name, str(obj.allowed_content_types))
		print out


def list_fields(objs):
	print "============================================================================"
	for obj in objs:
		out = "%12s -> %s" % (obj.type_name, str(obj.allowed_content_types))
		print out
		for fld in obj.ikfields:
			out = "%24s: %16s: %s" % (fld[0], fld[1], fld[2])
			print out
		print "-------------------------"
	print "============================================================================"

def list_fieldsch(objs):
	print "============================================================================"
	for obj in objs:
		out = "%12s -> %s" % (obj.type_name, str(obj.allowed_content_types))
		print out
		for fld in obj.ikfields:
			#out = "%s " % (fld[0])
			
			print fld[0]
		print "-------------------------"
	print "============================================================================"



def reftest(objs):
        names = []
        for obj in objs:
                names.append(obj.type_name)
        for obj in objs:
                for val in obj.allowed_content_types:
                        if val in names:
                                print obj.type_name, val, 'OK'
                        else:
                                print obj.type_name, val, 'ERROR'
				


if __name__ == '__main__':
        list_names(contents)
        list_fields(contents)

        test = Test()
        reftest(contents)
        test.ok(contents)

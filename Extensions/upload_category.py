from xml.dom import minidom   

from Products.CMFCore.utils import getToolByName


class IKXML:
	def readXML(self, file = "/opt/data/cusat-finance-categories.xml"):
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
				if n.tagName == tag:
					out.append(n)
		return out
			
        def getBaseCategoryNodes(self):
                m = self.getNodeByTagName(self.xmldoc,'categories')
                node = self.getNodeByTagName(m[0], 'item')
                return node

		
	def node2dict(self, node):
		out = {}
		for node2 in node.childNodes:
			if node2.nodeType == node2.ELEMENT_NODE:
				tag = node2.tagName
				if tag == 'item': continue
				out[tag] = ""
				for node3 in node2.childNodes:
					if node3.nodeType == node3.TEXT_NODE:
            					out[tag] = node3.data
		return out

	def createBaseCategory(self, node, obj=None):
		vv = self.node2dict(node)

		id = vv['id']
		title = vv['title']

                id = self.xmlsafe(id)
                title = self.xmlsafe(title)

		tree = getattr(self.category, id, None)
		if tree is None:
			self.category.invokeFactory('Base Category', id)
			tree = getattr(self.category, id)
		tree.setTitle(title)
		self.createCategory(node, tree)
		return

	def createCategory(self, node, obj=None, tab = 1):
                nodeList = self.getNodeByTagName(node, 'item')
		for node1 in nodeList:
			vv = self.node2dict(node1)
			id = vv['id']
			title = vv['title']
			short_title = vv['short_title']
			codification = vv['codification']

                        id = self.xmlsafe(id)
                        title = self.xmlsafe(title)
                        short_title = self.xmlsafe(short_title)
                        codification = self.xmlsafe(codification)
			tree = getattr(obj, id, None)
			if tree is None:
				obj.invokeFactory("Category", id)
				tree = getattr(obj, id)
			tree.setTitle(title)
			if len(short_title.strip()):
				tree.setShortTitle(short_title)
			if len(codification.strip()):
				tree.setCodification(codification)
			self.createCategory(node1, tree, tab+1)
		return
			

	def run1(self, category):
		self.category = category
		self.readXML()
		for node in self.getBaseCategoryNodes():
			self.createBaseCategory(node)


def upload_category(self):

	from Products.CMFCore.utils import getToolByName
	context = self
	urltool = getToolByName(context, "portal_url")
	portal = urltool.getPortalObject()
	catalogtool = getToolByName(context, "portal_catalog")
	workflowtool = getToolByName(context, "portal_workflow")
	category = getToolByName(context, "portal_categories")
	ik = IKXML()
	ik.run1(category)
	return 'OK'


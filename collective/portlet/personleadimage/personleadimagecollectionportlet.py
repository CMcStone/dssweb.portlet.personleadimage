from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner

from collective.portlet.personleadimage import PersonLeadImageCollectionPortletMessageFactory as _

from plone.portlet.collection import collection
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from Products.FacultyStaffDirectory import vocab

from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.contentleadimage.config import IMAGE_CAPTION_FIELD_NAME


class IPersonLeadImageCollectionPortlet(collection.ICollectionPortlet):
    """A portlet which renders the results of a collection object, but
    displaying the personleadimages.
    """
   
    show_title = schema.Bool(
        title=_(u"Show person's title information"),
        description=_(u'this will show title'),
        default=True,
        required=False)
        
    contact_info = schema.Bool(
        title=_(u"Show Contact Information"),
        description=_(u'this will show phone and office address'),
        default=False,
        required=False)
    
    email = schema.Bool(
        title=_(u"Show Email Information"),
        description=_(u'this will show email address'),
        default=False,
        required=False)
        
    office_hours = schema.Bool(
        title=_(u"Show Office Hours"),
        description=_(u'this will show office hours'),
        default=False,
        required=False)

    scale = schema.Choice(
        title=_(u"Image scale"),
        description=_(u"The size of the images in the portlet."),
        default='thumb',
        vocabulary = u"collective.contentleadimage.scales_vocabulary")


class Assignment(collection.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IPersonLeadImageCollectionPortlet)

    contact_info = False
    office_hours = False
    email = False
    show_title = False
    scale = 'thumb'

    def __init__(self, header=u"", target_collection=None, limit=None,
            random=False, show_more=False, contact_info=False, email=False, show_title=False,
            office_hours=False, show_dates=False, scale='thumb', **kwargs):
        super(Assignment, self).__init__(header, target_collection, limit,
                                             random, show_more, show_dates, **kwargs)
        self.contact_info = contact_info
        self.office_hours = office_hours
        self.email = email
        self.show_title = show_title
        self.scale = scale
        

class Renderer(collection.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    #_template = ViewPageTemplateFile('personleadimagecollectionportlet.pt')
    render = ViewPageTemplateFile('personleadimagecollectionportlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        

    def tag(self, obj, css_class='tileImage'):
        context = aq_inner(obj)
        field = context.getField(IMAGE_FIELD_NAME)
        titlef = context.getField(IMAGE_CAPTION_FIELD_NAME)
        if titlef is not None:
            title = titlef.get(context)
        else:
            title = ''
        if field is not None:
            if field.get_size(context) != 0:
                return field.tag(context, scale=self.data.scale, css_class=css_class, title=title)
        return ''
        
    def getObjectByUID(self, UID):
        """
            find the object with this UID
        """
        catalog = getToolByName(self, 'portal_catalog')
        brains = catalog(UID=UID)
        return brains[0].getObject()

    def getQueryDepartment(self):
        target_collection = self.collection()
        results = target_collection.getRawQuery()
        for s in results:
            if 'getRawDepartments' in s['i']:
                dept_uid = s['v']
                if dept_uid:
                    return self.getObjectByUID(dept_uid)
                return None

class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    
    form_fields = form.Fields(IPersonLeadImageCollectionPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget
    form_fields.omit('show_dates')

    label = _(u"Add PersonLeadImage Collection Portlet")
    description = _(u"This portlet displays a listing of people from a collection with various metadata.")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IPersonLeadImageCollectionPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label = _(u"Edit PersonLeadImage Collection Portlet")
    description = _(u"This portlet displays a listing of people from a collection with various metadata.")
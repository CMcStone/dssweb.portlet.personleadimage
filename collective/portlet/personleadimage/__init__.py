from zope.i18nmessageid import MessageFactory
PersonLeadImageCollectionPortletMessageFactory = MessageFactory('collective.portlet.personleadimage')

from Products.CMFCore.permissions import setDefaultRoles
from plone.portlet.collection import DEFAULT_ADD_CONTENT_PERMISSION 
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

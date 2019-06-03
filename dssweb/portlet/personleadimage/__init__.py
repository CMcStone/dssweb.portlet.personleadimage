from zope.i18nmessageid import MessageFactory
PersonLeadImageCollectionPortletMessageFactory = MessageFactory('dssweb.portlet.personleadimage')

from Products.CMFCore.permissions import setDefaultRoles
from plone.portlet.collection import DEFAULT_ADD_CONTENT_PERMISSION 

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Site Administrator', 'Contributor',))


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

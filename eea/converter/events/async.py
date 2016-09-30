""" Async events
"""

from zope.interface import implementer
from eea.converter.events.interfaces import IAsyncExportFail
from eea.converter.events.interfaces import IAsyncEventFail
from eea.converter.events.interfaces import IAsyncExportSuccess
from eea.converter.events.interfaces import IAsyncEventSuccess
from eea.converter.events import AsyncEvent

@implementer(IAsyncEventFail)
class AsyncEventFail(AsyncEvent):
    """ Event triggered when an async export job failed
    """

@implementer(IAsyncExportFail)
class AsyncExportFail(AsyncEvent):
    """ Event triggered when an async export job failed
    """


@implementer(IAsyncExportSuccess)
class AsyncExportSuccess(AsyncEvent):
    """ Event triggered when an async export job succeeded
    """

@implementer(IAsyncEventSuccess)
class AsyncEventSuccess(AsyncEvent):
    """ Event triggered when an async export job succeeded
    """

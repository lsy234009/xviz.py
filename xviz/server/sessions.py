import logging

class XVIZBaseSession:
    def __init__(self, socket, request, logger=None):
        self._socket = socket
        self._request = request
        self._logger = logger or logging.getLogger('xviz-server')

    def on_connect(self):
        '''
        This method is called when server is connected and session is generated.
        '''
        raise NotImplementedError("Derived class should implement this method")

class XVIZProviderSession(XVIZBaseSession):
    '''
    This class holds a `provider` session, where the provider handles data I/O
    '''
    def __init__(self, socket, request, provider, logger=None, **options):
        super().__init__(socket, request, logger)
        self._provider = provider
        
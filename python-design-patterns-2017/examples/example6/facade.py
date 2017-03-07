# Imagine a badly designed old system with many classes and methods
# Performing even the simplest operations means instantiating several objects
# and calling methods with unintuitive names.

class SystemFacade:
    def __init__(self, connection_info):
        self.connection_info = connection_info
    def _create_connector(self):
        state = ConnectorState()
        return ConnectorObject(state)
    def send_data(self, data):
        connector = self._create_connector()
        connector.prepareForDataReception()
        connector.receiveData(data)
        connector.releaseLockedConnection()
    def get_data(self):
        connector = self._create_connector()
        connector.getReadyForSending()
        data = connector.get()
        connector.releaseLock()
        return self._scrubData(data)
 
system = SystemFacade('asdf://10.10.10.10:1234')
system.send_data(b'\x01')
system.get_data()


# The facade allows us to:
# - Unify the access to several objects/methods to simplify
# - Prevent access to some parts of the old system
# - Make it easier to use
# - Hide badly designed APIs

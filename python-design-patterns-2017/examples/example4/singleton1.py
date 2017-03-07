connection_url = "https://example.com"
connection_user = "admin"
connection_password = "secret!"

def get_data():
    return request.get(connection_url, ...)

def send_data(data):
    return request.post(connection_url, ...)




# In other module
from abc import get_data, send_data

...

# Python modules are singletons! You can take advantage of that.

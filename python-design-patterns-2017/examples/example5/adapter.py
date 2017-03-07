class HTTPAPI:
    def __init__(self, url, ...):
        ...
    def post(data):
        ...
    def get():
        ...

# We have some library code that wants a file object with read/write methods
# We don't want to or can't modify HTTPAPI


class HTTPAPIFileAdapter:
    def __init__(self, api):
        self._api = api
    def read():
        return self._api.get()
    def write(data):
        self._api.post(data)


api = HTTPAPI('https://example.com...', ...)
adapter = HTTPAPIFileAdapter(api)

library.set_file(adapter)
library.start_processing()

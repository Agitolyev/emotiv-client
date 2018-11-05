class Request(object):

    def __init__(self, method, params, id, jsonrpc="2.0"):
        assert isinstance(params, dict)
        self.jsonrpc = jsonrpc
        self.method = method
        self.params = params
        self.id = id

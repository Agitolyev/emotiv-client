class Request(object):

    def __init__(self, method: str, params: dict, id: int, jsonrpc: str="2.0"):
        assert isinstance(params, dict)
        self.jsonrpc = jsonrpc
        self.method = method
        self.params = params
        self.id = id

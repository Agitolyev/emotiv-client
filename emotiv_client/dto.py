import sys
import json
import random


class Request(object):

    def __init__(self, method: str, id: int, jsonrpc: str="2.0", **kwargs):
        self.id = id
        self.jsonrpc = jsonrpc
        self.method = method
        self.params = kwargs

    def to_string(self, pretty=False):
        return json.dumps(self.__dict__) if not pretty else json.dumps(self.__dict__, indent=4)

    @classmethod
    def of(cls, method: str, params: dict):
        return cls(method,  random.randint(0, sys.maxsize), **params)


class Response(object):

    def __init__(self, id: int, result=None, error=None, jsonrpc: str="2.0"):
        self.id = id
        self.jsonrpc = jsonrpc
        self.result = result
        self.error = error

    def to_string(self, pretty=False):
        return json.dumps(self.__dict__) if not pretty else json.dumps(self.__dict__, indent=4)

    @classmethod
    def of_json(cls, resp: dict):
        return cls(resp.get('id'), resp.get('result'), resp.get('error'), resp.get('jsonrpc'))

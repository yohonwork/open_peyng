

from functools import wraps
from .proxy import create_peyng_proxy

def peygn_client(base_url):
    def decorator(cls):
        return create_peyng_proxy(cls, base_url)
    return decorator

def api_mapping(method, path):
    method = method.upper()
    if method is not "GET" or method is not "POST" or method is not "PUT" or method is not "DELETE":
        raise ValueError

    def decorator(func):
        func._api_method = method
        func._api_path   = path
        return func

    return decorator

def get_mapping(method, path):
    def decorator(func):
        func._api_method = "GET"
        func._api_path   = path
        return func

    return decorator

def post_mapping(path):
    def decorator(func):
        func._api_method = "POST"
        func._api_path   = path
        return func

    return decorator

def put_mapping(path):
    def decorator(func):
        func._api_method = "PUT"
        func._api_path   = path
        return func

    return decorator

def delete_mapping(path):
    def decorator(func):
        func._api_method = "DELETE"
        func._api_path   = path
        return func

    return decorator
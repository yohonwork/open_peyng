

from functools import wraps
from .proxy import create_peyng_proxy

def peygn_client(base_url):
    def decorator(cls):
        return create_peyng_proxy(cls, base_url)
    return decorator

def api_mapping(method, path):
    def decorator(func):
        func._api_method = method
        func._api_path   = path
        return func

    return decorator

def get_mapping(method, path):
    if method is None:
        method = "GET"

    def decorator(func):
        func._api_method = method
        func._api_path   = path
        return func

    return decorator

def post_mapping(method, path):
    if method is None:
        method = "POST"

    def decorator(func):
        func._api_method = method
        func._api_path   = path
        return func

    return decorator

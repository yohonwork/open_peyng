import inspect
from functools import wraps

from .requestor import invoke_request

def create_peyng_proxy(cls, base_url):
    methods = {
        name: func for name, func in cls.__dict__.items()
        if callable(func) and hasattr(func, "_api_method")
    }

    class PeygnProxy:
        def __init__(self):
            self.base_url = base_url

        def __getattr__(self, name):
            if name in methods:
                func = methods[name]
                @wraps(func)
                def wrapper(*args, **kwargs):
                    sig = inspect.signature(func)
                    bound = sig.bind(self, *args, **kwargs)
                    bound.apply_defaults()
                    params = bound.arguments
                    return invoke_request(
                        method=func._api_method,
                        path=func._api_path,
                        base_url=self.base_url,
                        args=params
                    )
                return wrapper
            raise AttributeError(f"{name} not found")
    return PeygnProxy()
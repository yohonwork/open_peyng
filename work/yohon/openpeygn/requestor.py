
import requests
import re

def resolve_path(path, args: dict):
    for key, value in args.items():
        path = re.sub(rf"\{{{key}}}", str(value), path)

    return path

def invoke_request(method, path, base_url, args: dict):
    url = f"{base_url}{resolve_path(path, args)}"
    method = method.upper()

    print(f"url:[{url}]")
    print(f"method:[{method}]")
    if method == "GET":
        return requests.get(url)
    elif method == "POST":
        body = args.get("user") or args.get("body")
        return requests.post(url, json=body).json()
    elif method == "PUT":
        return requests.put(url)
    elif method == "DELETE":
        return requests.delete(url)
    else:
        raise NotImplementedError(f"{method} not implemented")
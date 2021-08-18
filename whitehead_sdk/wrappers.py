import pkgutil
import importlib
from gql.client import Client
from . import api


def wrapper(self, func):    
    def inner(*args, **kwargs):
        return func(self, *args, **kwargs)

    return inner


class GraphqlClient(Client):
    _api_map = {
        m.name: getattr(
            getattr(importlib.import_module(f"{api.__name__}.{m.name}"), m.name),
            "execute",
        )
        for m in pkgutil.iter_modules(api.__path__)
        if not m.ispkg
    }

    def __getattr__(self, name):
        try:
            return wrapper(self, self._api_map[name])
        except KeyError:
            raise AttributeError(name)

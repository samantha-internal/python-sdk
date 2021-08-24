import pkgutil
import importlib
from base64 import b64encode, b64decode
from functools import partial
from gql.client import Client
from . import api
from .api.input.turn import Turn


def wrapper(self, func):
    def inner(*args, **kwargs):
        result = func(self, *args, **kwargs)
        if hasattr(result, "result"):
            result = result.result
        return result

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_wrappers = {
            name.split("_")[-1]: partial(method, self)
            for name, method in self.__class__.__dict__.items()
            if name.startswith("_wrap_")
        }

    def _wrap_similarity(self, orig_method):
        def wrapper(*args, **kwargs):
            result = orig_method(*args, **kwargs)
            if not result:
                return
            return [s.to_dict() for s in result]

        return wrapper

    _wrap_sentiment = _wrap_similarity
    _wrap_topics = _wrap_similarity

    def _wrap_chitchat(self, orig_method):
        def wrapper(input, history):
            return orig_method(input, [Turn.from_dict(h) for h in history])

        return wrapper

    def _wrap_sensibility(self, orig_method):
        def wrapper(input, history):
            return [
                alt.to_dict()
                for alt in orig_method(input, [Turn.from_dict(h) for h in history])
            ]

        return wrapper

    def _wrap_speak(self, orig_method):
        def wrapper(input, stream):
            return stream.write(b64decode(orig_method(input)))

        return wrapper

    def _wrap_transcribe(self, orig_method):
        def wrapper(input):
            return orig_method(b64encode(input.read()).decode())

        return wrapper

    def __getattr__(self, name):
        try:
            custom_wrapper = self.custom_wrappers.get(name)
            method = self._api_map[name]
            if not custom_wrapper:
                return wrapper(self, method)
            else:
                return custom_wrapper(wrapper(self, method))
        except KeyError:
            raise AttributeError(name)

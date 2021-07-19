import os
import hashlib
import tempfile
import portalocker
from contextlib import contextmanager, suppress
from datetime import datetime


class TokenCache:
    def __init__(self, dev_id, api_key):
        self._hash = hashlib.md5(f"{dev_id}:{api_key}".encode()).hexdigest()

    @property
    def cache_path(self):
        ts = int(
            datetime.now()
            .replace(minute=0)
            .replace(second=0)
            .replace(microsecond=0)
            .timestamp()
        )
        return os.path.join(tempfile.gettempdir(), f"whitehead-{self._hash}-{ts}")

    def read(self):
        with suppress(FileNotFoundError):
            with portalocker.Lock(self.cache_path, "r") as f:
                return f.read()

    def write(self, data):
        with portalocker.Lock(self.cache_path, "a") as f:
            f.seek(0)
            f.truncate(0)
            f.write(data)

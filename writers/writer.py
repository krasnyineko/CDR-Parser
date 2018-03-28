from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def write(self, item, row):
        pass

    @abstractmethod
    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


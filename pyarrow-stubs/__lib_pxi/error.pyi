import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

class ArrowException(Exception): ...
class ArrowInvalid(ValueError, ArrowException): ...
class ArrowMemoryError(MemoryError, ArrowException): ...
class ArrowKeyError(KeyError, ArrowException): ...
class ArrowTypeError(TypeError, ArrowException): ...
class ArrowNotImplementedError(NotImplementedError, ArrowException): ...
class ArrowCapacityError(ArrowException): ...
class ArrowIndexError(IndexError, ArrowException): ...
class ArrowSerializationError(ArrowException): ...

class ArrowCancelled(ArrowException):
    signum: int | None
    def __init__(self, message: str, signum: int | None = None) -> None: ...

ArrowIOError = IOError

class StopToken: ...

def enable_signal_handlers(enable: bool) -> None: ...

have_signal_refcycle: bool

class SignalStopHandler:
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type, exc_value, exc_tb) -> None: ...
    def __dealloc__(self) -> None: ...
    @property
    def stop_token(self) -> StopToken: ...

__all__ = [
    "ArrowException",
    "ArrowInvalid",
    "ArrowMemoryError",
    "ArrowKeyError",
    "ArrowTypeError",
    "ArrowNotImplementedError",
    "ArrowCapacityError",
    "ArrowIndexError",
    "ArrowSerializationError",
    "ArrowCancelled",
    "ArrowIOError",
    "StopToken",
    "enable_signal_handlers",
    "have_signal_refcycle",
    "SignalStopHandler",
]

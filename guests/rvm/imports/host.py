from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from types import TracebackType
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some



def multiply(a: float, b: float) -> float:
    raise NotImplementedError

def client_secret() -> str:
    raise NotImplementedError


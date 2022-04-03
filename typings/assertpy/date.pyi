from typing import Any

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class DateMixin:
    def is_before(self, other: Any) -> AssertionBuilder:
        ...

    def is_after(self, other: Any) -> AssertionBuilder:
        ...

    def is_equal_to_ignoring_milliseconds(self, other: Any) -> AssertionBuilder:
        ...

    def is_equal_to_ignoring_seconds(self, other: Any) -> AssertionBuilder:
        ...

    def is_equal_to_ignoring_time(self, other: Any) -> AssertionBuilder:
        ...

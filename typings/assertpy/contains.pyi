from typing import Any

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class ContainsMixin:
    def contains(self, *items: Any) -> AssertionBuilder:
        ...

    def does_not_contain(self, *items: Any) -> AssertionBuilder:
        ...

    def contains_only(self, *items: Any) -> AssertionBuilder:
        ...

    def contains_sequence(self, *items: Any) -> AssertionBuilder:
        ...

    def contains_duplicates(self) -> AssertionBuilder:
        ...

    def does_not_contain_duplicates(self) -> AssertionBuilder:
        ...

    def is_empty(self) -> AssertionBuilder:
        ...

    def is_not_empty(self) -> AssertionBuilder:
        ...

    def is_in(self, *items: Any) -> AssertionBuilder:
        ...

    def is_not_in(self, *items: Any) -> AssertionBuilder:
        ...

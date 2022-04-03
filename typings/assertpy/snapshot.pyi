from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class SnapshotMixin:
    def snapshot(
        self, id: str | None = ..., path: str | None = ...
    ) -> AssertionBuilder:
        ...

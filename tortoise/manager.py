from typing import Type, Optional

from tortoise.queryset import MODEL, QuerySet


class Manager:
    """
    A Manager is the interface through which database query operations are provided to tortoise models.

    There is one default Manager for every tortoise model.
    """

    def __init__(self, model: Optional[Type[MODEL]] = None) -> None:
        self._model = model

    def get_queryset(self) -> QuerySet:
        return QuerySet(self._model)

    def __getattr__(self, item):
        return getattr(self.get_queryset(), item)

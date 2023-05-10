from typing import Iterable

from main.models import SearchHistory


def search_history_list() -> Iterable[SearchHistory]:
    searches = SearchHistory.objects.all().order_by('created')
    return searches
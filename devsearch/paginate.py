from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from typing import List


def paginate(content: List, current_page: str, elements_on_page: int, pages_at_once: int):
    paginator = Paginator(content, elements_on_page)
    try:
        paginator.page(current_page)
    except PageNotAnInteger:
        current_page = 1
    except EmptyPage:
        current_page = paginator.num_pages
    finally:
        current_page = int(current_page)
    
    def pages_limited(pages_at_once):
        start = min(max(1, current_page - pages_at_once//2), max(1, paginator.num_pages - pages_at_once + 1))
        end = min(max(pages_at_once, current_page + pages_at_once//2), paginator.num_pages)
        return range(start, end + 1)

    return paginator.page(current_page), pages_limited(pages_at_once)


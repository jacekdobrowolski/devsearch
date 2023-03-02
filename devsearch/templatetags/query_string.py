from django import template


register = template.Library()

@register.simple_tag
def build_query_string(query='?', **kwargs):
    if not query:
        query = '?'
    else:
        query = f'{query}&'
    if kwargs:
        queries = [f'{keyword}={value}' for keyword, value in kwargs.items() if value]
        query = query + '&'.join(queries)
    return query

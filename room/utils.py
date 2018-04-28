
# Graphos doesn't like the Queryset result from .values, so turn it into a list it will swallow.
def mung_table(table):
    data = []
    data.append(['title', 'num_title'])
    for i, v in enumerate(table):
        data.append([v['title'], v['num_title']])

    return data


# Graphos doesn't like the Queryset result from .values, so turn it into a list it will swallow.
# expect headers to match column names
def listify_table_with_headers(headers, table):
    data = []
    data.append(headers)

    for i, v in enumerate(table):
        data.append([v[headers[0]], v[headers[1]]])

    return data

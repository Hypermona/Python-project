items = [
    ("bende", 20),
    ("thonde", 40),
    ("kadle", 10),
    ("kothambari", 13),
    ('beeja', 30)
]


def sort_i(item):
    return item[1]


items.sort(key=sort_i, reverse=True)
print(items)

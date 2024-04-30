def pageCount(total_pages, page_to_visit):
    from_front = page_to_visit // 2
    from_back = (total_pages // 2) - from_front
    return min(from_front, from_back)


total_pages = 6
page_to_visit = 2

print(pageCount(total_pages, page_to_visit))

class SimplePagination(PageNumberPagination):
    page_size = 14
    page_size_query_param = 'page_size'
    max_page_size = 40

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('item_count', self.page.paginator.count),
            ('page_count', self.page.paginator.num_pages),
            ('current', self.page.number),
            ('next', self.page.next_page_number() if self.page.has_next() else None),
            ('previous', self.page.previous_page_number() if self.page.has_previous() else None),
            ('results', data),
        ]))


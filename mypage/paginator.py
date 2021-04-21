from paginate_sqlalchemy import SqlalchemyOrmPage


class Paginator(SqlalchemyOrmPage):

    def __init__(self, *args, radius=3, **kwargs):
        super(Paginator, self).__init__(*args, **kwargs)
        self.radius = radius
        self.page_range = self._make_page_range()

    def _make_page_range(self):
        if self.page_count < self.radius:
            return [p for p in range(1, self.page_count + 1)]

        if self.page - self.radius > 2:
            page_range = [self.first_page, None] + [p for p in range(self.page - self.radius, self.page)]
        else:
            page_range = [p for p in range(1, self.page)]

        if self.page + self.radius < self.last_page - 1:
            page_range += [p for p in range(self.page, self.page + self.radius + 1)]
            page_range += [None, self.last_page]
        else:
            page_range += [p for p in range(self.page, self.last_page + 1)]

        return page_range


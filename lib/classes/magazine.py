class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list(set(a.author for a in self.articles()))

    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for a in self.articles():
            author_count[a.author] = author_count.get(a.author, 0) + 1
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        from .article import Article
        if not Article.all:
            return None
        mag_count = {}
        for a in Article.all:
            mag_count[a.magazine] = mag_count.get(a.magazine, 0) + 1
        return max(mag_count, key=mag_count.get)
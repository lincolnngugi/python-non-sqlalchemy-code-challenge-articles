class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list(set(a.magazine for a in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        return list(set(m.category for m in mags)) if mags else None

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
        if not Article.all:
            return None
        mag_count = {}
        for a in Article.all:
            mag_count[a.magazine] = mag_count.get(a.magazine, 0) + 1
        return max(mag_count, key=mag_count.get)
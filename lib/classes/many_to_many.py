class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        # validate type
        if not isinstance(title, str):
            raise Exception("Title must be a string")

        # validate length
        if not (5 <= len(title) <= 50):
            raise Exception(
                "Titles must be between 5 and 50 characters, inclusive")

        # prevent reassignment if already set
        if hasattr(self, "_title"):
            raise Exception("Title cannot be changed after initialization")

        self._title = title

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        # validate type
        if not isinstance(name, str):
            raise Exception("Name must be a string")

        # validate length
        if len(name) < 1:
            raise Exception("Name must be longer than 0 characters")

        # prevent reassignment
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed after initialization")

        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return set([magazine.magazine for magazine in self.articles()])

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass


class Magazine:
    def __init__(self, name, category):
        self._category = category
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # validate type
        if not isinstance(name, str):
            raise Exception("name must be a string")

        # validate length
        if not (2 <= len(name) <= 16):
            raise Exception(
                "Names must be between 2 and 16 characters, inclusive")

        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        # validate type
        if not isinstance(category, str):
            raise Exception("category must be a string")

        # validate length
        if len(category) < 1:
            raise Exception("category must be longer than 0 characters")

        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return set([magazine.author for magazine in self.articles()])

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

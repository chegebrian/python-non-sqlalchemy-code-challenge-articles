class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
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
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = [
            article for article in Article.all if article.author == self]
        if not articles:
            return None
        categories = {article.magazine.category for article in articles}
        return list(categories)


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
        articles = [
            article for article in Article.all if article.magazine == self]
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        articles = [
            article for article in Article.all if article.magazine == self]
        if not articles:
            return None
        # count how many articles each author has
        counts = {}
        for article in articles:
            author = article.author
            counts[author] = counts.get(author, 0) + 1
        # return authors with more than 2 articles
        result = [author for author, count in counts.items() if count > 2]
        return result if result else None

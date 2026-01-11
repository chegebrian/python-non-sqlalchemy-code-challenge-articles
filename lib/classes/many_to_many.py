class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and (5 <= len(title) <= 50):
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine


class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # validate type
        # if isinstance(name, str) and len(name) > 0:
        #     self._name = name
        pass

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
        if isinstance(name, str) and (2 <= len(name) <= 16):
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        # validate type
        if isinstance(category, str) and len(category) > 0:
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

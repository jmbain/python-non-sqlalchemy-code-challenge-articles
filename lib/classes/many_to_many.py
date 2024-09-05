class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, "_title"):
            self._title = new_title
        
class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16 and not hasattr(self, "_name"):
            self._name = new_name
        
    
    def articles(self):
        article_list = []
        for a in Article.all:
            if a.author is self:
                article_list.append(a)
        return article_list

    def magazines(self):
        magazine_set = set()
        for m in self.articles():
            magazine_set.add(m.magazine)
        return list(magazine_set)


    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        

    def topic_areas(self):
        topic_set = set()
        for m in self.magazines():
            topic_set.add(m.category)
        if len(list(topic_set)) > 0:
            return list(topic_set)
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name   
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
    

    def articles(self):
        article_list = []
        for a in Article.all:
            if a.magazine is self:
                article_list.append(a)
        return article_list

    def contributors(self):
        contributor_set = set()
        for a in self.articles():
            contributor_set.add(a.author)
        return list(contributor_set)

    def article_titles(self):
        titles = []
        for a in self.articles():
            titles.append(a.title)
        if len(titles) > 0:
            return titles
        else:
            return None

    def contributing_authors(self):
        author_list = []
        contributing_a_list = set()
        for a in self.articles():
            author_list.append(a.author)
            if author_list.count(a.author) > 1:
                contributing_a_list.add(a.author)
        if len(contributing_a_list) > 0:
            return list(contributing_a_list)
        else:
            return None


        # if len(contributing_a_list) > 0:
        #     return contributing_a_list
        # else:
        #     return None
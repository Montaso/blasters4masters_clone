class Category:
    def __init__(self):
        self.parent_category = None
        self.name = None
        self.products = []
        self.link = None

    def __init__(self, parent_category: object, name: str, link: str):
        self.parent_category = parent_category
        self.name = name
        self.link = link
        self.products = []

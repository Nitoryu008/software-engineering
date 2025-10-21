class Book:
    def __init__(self, author: str, title: str):
        self._author = author
        self._title = title

    def print_author(self):
        print(self.author)

    def print_title(self):
        print(self.title)

    @property
    def author(self) -> str:
        return self._author

    @property
    def title(self) -> str:
        return self._title

    @property
    def pages(self) -> int:
        return self._pages

    def print_pages(self):
        print(self.pages)

    def print_details(self):
        self.print_author()
        self.print_title()
        self.print_pages()

    @pages.setter
    def pages(self, p: int):
        self._pages = p


if __name__ == "__main__":
    b1 = Book("Charles Dickens", "A Christmas Carol")
    b1.pages = 92
    b1.print_details()
    b2 = Book("Osamu Dazai", "No Longer Human")
    b2.pages = 154
    b2.print_details()

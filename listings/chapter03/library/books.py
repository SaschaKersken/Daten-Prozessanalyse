class Book:

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f'{self.author}: "{self.title}"'


class EBook(Book):
    def __init__(self, author, title, e_format):
        # Konstruktor der Elternklasse aufrufen
        super().__init__(author, title)
        if self.is_format(e_format):
            self.e_format = e_format
        else:
            self.e_format = None

    # Neue Methode
    def is_format(self, e_format):
        return e_format in ['PDF', 'EPub', 'Mobi']

    # Überschriebene Methode
    def __str__(self):
        result = super().__str__()
        if self.e_format is not None:
            result += f" [{self.e_format}]"
        return result


if __name__ == '__main__':
    b1 = Book("J.R.R. Tolkien", "The Lord of the Rings")
    b2 = Book("Suzanne Collins", "The Hunger Games")
    e1 = EBook("Emily St. John Mandel", "Station Eleven", "EPub")
    e2 = EBook("Isaac Asimov", "Foundation", "Mobi")
    print(b1)
    print(b2)
    print(e1)
    print(e2)

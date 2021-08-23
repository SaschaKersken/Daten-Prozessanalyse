class Album:

    def __init__(self, artist, title, year, remarks = None):
        self.artist = artist
        self.title = title
        self.year = year
        self.remarks = remarks

    def __eq__(self, other):
        return self.artist == other.artist and self.title == other.title

    def __lt__(self, other):
        return self.artist < other.artist or (self.artist == other.artist and self.title < other.title)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return self == other or self > other

    def __str__(self):
        result = f"{self.artist}: {self.title} ({self.year})"
        if self.remarks:
            result += f" [{self.remarks}]"
        return result


if __name__ == '__main__':
    album1 = Album('Radiohead', 'OK Computer', 1997)
    album2 = Album('Muse', 'Absolution', 2003)
    album3 = Album('Radiohead', 'In Rainbows', 2007)
    album4 = Album(
        'Radiohead', 'OK Computer', 2017, 'Remastered anniversary edition')

    print(album1 == album4)
    print(album1 <= album4)
    print(album1 > album2)
    print(album1 > album3)
    for album in sorted([album1, album2, album3, album4]):
        print(album)

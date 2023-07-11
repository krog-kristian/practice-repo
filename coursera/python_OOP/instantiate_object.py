class MyFirstClass:
    print('Who wrote this?')
    index = 'Author-Book'

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + ' wrote the book: ' + book)

whodunnit= MyFirstClass()
whodunnit.hand_list('Sun Tzu', 'The Art of War')

#alt way to instiate objects

class ContructorClass:
    def __init__(self, book_name, author, year):
        self.name = book_name
        self.author = author
        self.year = year

    def define_book(self):
      print('The book ' + self.name + ' written by ' + self.author + ' was written in ' + str(self.year))

new_book = ContructorClass('Lord of the Rings', 'Tolkien', 1922)
new_book.define_book()
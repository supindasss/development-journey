"""Task 28 || OOP – Constructor || 10-03-2026
8. Create a class Book with a constructor that initializes title and author. Display the book details."""

class Book:

    def __init__(self,title,author):

        self.title=title

        self.author=author

    def display(self):

        print(self.title,self.author)  

book_instance=Book("the greatgatsby","F.scott")          
book_instance.display()
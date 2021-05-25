# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#class Dog:
 #   species = "Canis Familiaris"

  #  def __init__(self, name, age):
 #       self.name = name
 #       self.age = age

  #  name = input('Enter your name: ')
 #   age = input('Enter the age ')

    # Instance method
#    def description(self):
#        print("{self.name} is {self.age} years old")

    # Another instance method
 #   def speak(self, sound):
#        print(f"{self.name} says {sound}")


class Book:


    favorites = [] #This is an Class-level attribute *see line 40-48*

    def __init__(self, title, pages):
        print("Creating book")
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    # This is how to overriding a method
    def __str__(self):
        return f"{self.title} is {self.pages} pages long."

    # Overriding equal
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False


    #How to Hash: **line 55-56, 64-68**
    # Rules for hashing:
    # - Hashes shouldn't change an object hash should remain the same for the whole code
    # - If at least two objects consider equal, hashes should also be the same
    # - if at least two objects are different,  hashes do not have to be the same. its ideal though

    # __hash__ == None: mutable types

    def __hash__(self):
            return hash(self.title) ^ hash(self.pages)


    #This format is called invoking.
book = Book("Can of Worms", 72)
book2 = Book("Green Eggs and Ham", 72)

# For hashing *Line 64-68*
books = {book, book2}
print(hash(book))

book.title = "Something else"
print(hash(book))

#Book.favorites.append(book)
#Book.favorites.append(book2)

for b in Book.favorites:
    print(b.title)

#This is how to call a function

#print (book.title)
#print(book.is_long())

#book2 = Book("test", 200)
#print(book2.is_long())
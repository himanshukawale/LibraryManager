
class Library:
    def __init__(self, list_of_books, name_of_library):
        self.record = {}
        self.list_of_books = list_of_books
        self.name_of_library = name_of_library
        for books in self.list_of_books:
            self.record[books] = None

    def display_book(self):
        for books in self.list_of_books:
            print(f"{books}")

    def lend(self, user_name, book_name):
        if self.record.get(book_name) == None:
            self.record[book_name] = user_name
            print(
                f"The book '{book_name}' is issued to you, please return it after the use")
        else:
            print(
                f"Sorry the book {book_name} is already issued by {self.record.get(book_name)}")

    def return_book(self, r_book_name):
        self.record[r_book_name] = None
        print(f"You returned the book named '{r_book_name}' to the library")

    def donate_book(self, d_book_name):
        self.list_of_books.append(d_book_name)
        self.record[d_book_name] = None


lab = Library(["book1", "book2", "book3", "book4", "book5",
              "book6", "book7", "book8", "book9", "book10"], "himanshu")


if __name__ == "__main__":

    print(f"Welcome to the {lab.name_of_library} library")
    lab.display_book()

    while True:
        print("\nPlease enter your choice\n(1) Lend a book\n(2) Return a book\n(3) Donate a book\n")

        user_input=int(input())

        if user_input==1:
            user_name=input("Enter your user name\n")
            book_name=input("Enter a book name\n")
            lab.lend(user_name, book_name)
        elif user_input==2:
            r_book_name=input("Enter the name of a book you want to return")
            lab.return_book(r_book_name)
        elif user_input==3:
            d_book_name=input("Please enter the name of a book you want to Donate to the library")
            lab.donate_book(d_book_name)
            lab.display_book()
        else:
            print("You entered a wrong choice, Please choose the correct option")

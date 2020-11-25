# library
import random
uniquecode = random.randint(1000000, 5000000)
time = random.randint(0, 24)


class library:
    def __init__(self, books):
        self.books = books

    def displayavailablebooks(self):
        print('books in this library are: ')
        for index, book in enumerate(self.books):
            print((index+1), '\t', book)

    def borrowbooks(self, bookname):
        if bookname in self.books:
            print(
                f'you have been issued the book {bookname}, please return in 30 days')
            self.books.remove(bookname)
        else:
            print('book isnt avilable, please wait for some time')

    def returnbook(self, bookname):
        print(f'thank you for returning book {bookname}')
        self.books.append(bookname)

    def donatebook(self, bookname):
        print(
            f'thank you for donatng book {bookname}, hope you have a good day')
        self.books.append(bookname)

    def IdCardApplication(self, IdNumber):
        print(
            f'your id card with id number {IdNumber} is applied, we will send you an email when we recieve your card')

    def Appointment(self):
        print(
            f'your appointment with library head is scheduled at {time}.00 hrs ist and your unique code is: {uniquecode}, show this code when you meet him')

    def complaint(self, complain):
        print(
            f'your complaint of {complain} has been sucessfully registered and we will keep you updated about this')


class student:
    def requestbook(self):
        self.book = input('Please enter the book name you want to borrow : ')
        return self.book

    def returnthebook(self):
        self.book = input('Please enter the book you want to return : ')
        return self.book

    def donate(self):
        self.book = input(
            'Please enter the book name that you want to donate: ')
        return self.book

    def idCard(self):
        self.idnumber = input('Please enter your Id number : ')
        return self.idnumber

    def comp(self):
        self.complain = input('what is your complaint ?')
        return self.complain


if __name__ == "__main__":
    mainlibrary = library(['nikhil', 'sharath', 'niharika', 'something',
                           'rigveda', 'yajurveda', 'samaveda', 'adarvana vedha'])
    nikhil = student()

    while(True):  # i can add students list and say hello student, welcome to library
        commonmessage = (''' ======Hello, welcome to the Nikhils library======
                             1.Show Avalablebooks
                             2.Borrow a book
                             3.Return a book
                             4.Donate a book
                             5.Apply for a Id card
                             6.Appointment to meet library head
                             7.File a complaint
                             8.Exit the library 
                             Please choose from the above options   ''')

        print(commonmessage)
        try:
            a = int(input('Plese enter your choice  :'))
            if a == 1:
                mainlibrary.displayavailablebooks()
            elif a == 2:
                mainlibrary.borrowbooks(nikhil.requestbook())
            elif a == 3:
                mainlibrary.returnbook(nikhil.returnthebook())
            elif a == 4:
                mainlibrary.donatebook(nikhil.donate())
            elif a == 5:
                mainlibrary.IdCardApplication(nikhil.idCard())
            elif a == 6:
                mainlibrary.Appointment()
            elif a == 7:
                mainlibrary.complaint(nikhil.comp())
            elif a == 8:
                print("Thankyou for using Nikhil's library")
                exit()
            else:
                print('Choose the correct choice ')
        except Exception as e:
            print(e)

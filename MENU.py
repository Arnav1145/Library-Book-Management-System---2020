import BOOK


def MenuBook():
          while True:
                    print("\t\t\t Book Record Management\n " )
                    print("===================================")
                    print("1.Add Book Record            ")
                    print("2.Display Book Records     ")
                    print("3.Search Book Record        ")
                    print("4.Delete Book Record         ")
                    print("5.Update Book Record        ")
                    print("6.Exit                                  ")
                    print("===================================")
                    choice=int(input("Enter choice between 1 to 5------->:"))
                    if choice==1:
                              BOOK.insertData()
                    elif choice==2:
                              BOOK.display()
                    elif choice==3:
                              BOOK.SearchBookRec()
                    elif choice==4:
                              BOOK.deleteBook()
                    elif choice==5:
                              BOOK.UpdateBook()
                    elif choice==6:
                              break
                    else:
                              print("Wrong Choice.................Enter your choice again ")
                              x=input("Enter any key to continue ")

MenuBook()

                    
                    

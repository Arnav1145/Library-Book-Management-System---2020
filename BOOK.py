import mysql.connector as ms
def display():
          cnx=ms.connect(user='root',passwd='dxn@9452710927',host='localhost',database='library')
          cursor=cnx.cursor()
          query=("SELECT * FROM bookrecord")
          cursor.execute(query)
          for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in cursor:
                    print("============================================")
                    print("BOOK CODE                                 :",Bno)
                    print("BOOK NAME                                 :",Bname)
                    print("AUTHOR OF BOOK                            :",Author)
                    print("PRICE OF BOOK                             :",price)
                    print("PUBLISHER                                 :",publ)
                    print("TOTAL QUANTITY IN HAND                    :",qty)
                    print("PURCHASED ON                              :",d_o_purchase)
                    print("=============================================")
          print("YOU HAVE DONE IT!!!!!!")
          cnx.close()

          
           

def insertData():
          cnx=ms.connect(user="root",passwd="dxn@9452710927",host="localhost",database="library")
          cursor=cnx.cursor()
          bno=int(input("ENTER BOOK CODE  :"))
          bname=input("ENTER BOOK NAME  :")
          Auth=input("ENTER BOOK AUTHOR'S NAME  :")
          price=float(input("ENTER BOOK PRICE  :"))
          publ=input("ENTER PUBLISHER OF BOOK  :")
          qty=int(input("ENTER QUANTITY PURCHASED  :"))
          print("ENTER DATE OF PURCHASE (DATE,MONTH AND YEAR SEPARATELY:")
          DD=input("ENTER DATE  :")
          MM=input("ENTER MONTH  :")
          YY=input("ENTER YEAR  :")
          dop=YY+'-'+MM+'-'+DD
          Qry=("INSERT INTO BookRecord VALUES (%s,%s,%s,%s,%s,%s,%s)")
          data=(bno,bname,Auth,price,publ,qty,dop)
          cursor.execute(Qry,data)
          cnx.commit()
          cnx.close()
          print("RECORD INSERTED.........")



def deleteBook():
          cnx=ms.connect(user="root",passwd="dxn@9452710927",host="localhost",database="library")
          cursor=cnx.cursor()
          bno=int(input("ENTER BOOK CODE OF BOOK TO BE DELETED FROM THE LIBRARY  :"))
          Qry=("DELETE FROM BookRecord WHERE Bno=%s ")
          del_rec=(bno,)
          cursor.execute(Qry,del_rec)
          cnx.commit()
          cursor.close()
          cnx.close()
          print(cursor.rowcount,"RECORD(S) DELETED SUCCESSFULLY..........")

def SearchBookRec():
          cnx=ms.connect(user="root",passwd="dxn@9452710927",host="localhost",database="library")
          cursor=cnx.cursor()
          bno=int(input("ENTER BOOK TO BE SEARCHED FROM THE LIBRARY  :"))
          Qry=("SELECT * FROM BookRecord WHERE Bno=%s")
          rec_srch=(bno,)
          cursor.execute(Qry,rec_srch)
          rec_count=0
          for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in cursor:
                    rec_count+=1
                    print("===============================================")
                    print("BOOK CODE                                  :",Bno)
                    print("BOOK NAME                                  :",Bname)
                    print("AUTHOR OF BOOK                        :",Author)
                    print("PRICE OF BOOK                              :",price)
                    print("PUBLISHER                                      :",publ)
                    print("TOTAL QUANTITY IN HAND          :",qty)
                    print("PURCHASED ON                             :",d_o_purchase)
                    print("=============================================  ")
                    if rec_count%2==0:
                              input("PRESS ANY KEY TO CONTINUE")
                              print(rec_count,"RECORD(S) FOUND")
          cnx.commit()
          cursor.close()
          cnx.close()

def UpdateBook():
          cnx=ms.connect(user="root",passwd="dxn@9452710927",host="localhost",database="library")
          cursor=cnx.cursor()
          bno=int(input("ENTER BOOK CODE OF BOOK TO BE UPDATED FROM THE LIBRARY  :"))
          Qry=("SELECT * FROM BookRecord WHERE Bno=%s")
          rec_srch=(bno,)
          print("ENTER NEW DATA")
          bname=input("ENTER BOOK NAME  :")
          Auth=input("ENTER BOOK AUTHOR'S NAME  :")
          price=float(input("ENTER BOOK PRICE  :"))
          publ=input("ENTER PUBLISHER OF BOOK  :")
          qty=int(input("ENTER QUANTITY PURCHASED  :"))
          print("ENTER DATE OF PURCHASE (DATE,MONTH AND YEAR SEPARATELY:")
          DD=input("ENTER DATE  :")
          MM=input("ENTER MONTH  :")
          YY=input("ENTER YEAR  :")
          dop=YY+'-'+MM+'-'+DD
          Qry=("UPDATE BookRecord SET Bname=%s,Author=%s,price=%s,publ=%s,qty=%s,d_o_purchase=%s WHERE Bno=%s")
          data=(bname,Auth,price,publ,qty,dop,bno)
          cursor.execute(Qry,data)
          cnx.commit()
          cursor.close()
          cnx.close()
          print(cursor.rowcount,"RECORD(S) UPDATED SUCCESSFULLY...............")
        

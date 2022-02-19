from posixpath import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox
import os, sys, csv
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import ( NavigationToolbar2QT  as  NavigationToolbar )
from matplotlib.figure import Figure
from PyQt5.uic import loadUi


class Greet(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("Greet.ui", self)

        #If the button is pushed
        self.button1.clicked.connect(self.loginbtn)
        self.button2.clicked.connect(self.signupbtn)
    
    def loginbtn(self):
        print("Login Button")
        login.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupbtn(self):
        print("Sign up Button") 
        signup.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()+2)

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.co = 1
    
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.login)
        self.createaccbutton.clicked.connect(self.signup) 
        self.visiblebutton.clicked.connect(self.visible)
        self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")
        
        #SET PASSWORD
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet('lineedit-password-character: 9679')

    def clear(self):
        print("test clear")
        self.username.clear()
        self.password.clear()
        self.cond.clear()

    def visible(self):
        self.co +=1
        if (self.co%2 == 0): #Cek Ganjil Genap
            print("Visible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visiblebutton.setStyleSheet("background-image : url(img/visible.png);")

        else:
            print("Invisible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password.setStyleSheet('lineedit-password-character: 9679')      
            self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")

    def login(self):
        print("Login Button")
        counter = 0
        user = self.username.text()
        password = self.password.text()
        self.cond.setStyleSheet("color: red;")
        count = 0
        for i in rows :
            count += 1
            if i[0] == user:
                print("Username is correct")
                counter += 1
                if i[1] == password:
                    print("Access Granted")
                    self.cond.setStyleSheet("color: green;")
                    
                    self.cond.setText("Login Succesfull!")
                    self.month = []
                    self.date = []
                    self.inc = []
                    self.exp =[]
                    self.suminc = []
                    self.sumexp = []
                    self.main  = Main(count-1)
                    widget.addWidget(self.main)
                    self.finstat = Finstat()
                    balance = self.finstat.balance
                    self.main.start()
                    widget.addWidget(self.finstat)
                    exin = Exin(balance)
                    widget.addWidget(exin)
                    break
                    
                else:
                    self.cond.setText("Password is incorrect")
                    break         
        if counter == 0:
            self.cond.setText("Username or Password is incorrect")
        
        if self.cond.text() == "Login Succesfull!":
                
                widget.setFixedHeight(686)
                widget.setFixedWidth(660)
                widget.setCurrentIndex(widget.currentIndex()+2)
        
        
    def signup(self):
        print("Sign up Button") 
        signup.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Signup(QtWidgets.QMainWindow): #QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("signup.ui", self)
        self.mainbutton.clicked.connect(self.main)
        self.signupbutton.clicked.connect(self.Signup)
        self.visiblebutton.clicked.connect(self.visible)
        self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")
        self.visiblebutton_2.clicked.connect(self.visible_cpw)
        self.visiblebutton_2.setStyleSheet("background-image : url(img/invisible.png);")
        self.co = 1

        #SET PASSWORD
        self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwsignup.setStyleSheet('lineedit-password-character: 9679')
        self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpwsignup.setStyleSheet('lineedit-password-character: 9679')

    def clear(self):
        print("test clear")
        self.unsignup.clear()
        self.pwsignup.clear()
        self.cpwsignup.clear()
        self.cond.clear()

    def visible(self):
            self.co +=1
            if (self.co%2 == 0):
                print("Invisible")
                self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.visiblebutton.setStyleSheet("background-image : url(img/visible.png);")

            else:
                print("Visible")
                self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
                self.pwsignup.setStyleSheet('lineedit-password-character: 9679')         
                self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")

    def visible_cpw(self):
            self.co +=1
            if (self.co%2 == 0):
                print("Visible")
                self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.visiblebutton_2.setStyleSheet("background-image : url(img/visible.png);")

            else:
                print("Invisible")
                self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
                self.cpwsignup.setStyleSheet('lineedit-password-character: 9679')      
                self.visiblebutton_2.setStyleSheet("background-image : url(img/invisible.png);")

    def Signup(self):
        print("Signup Button")
        user = self.unsignup.text()
        password = self.pwsignup.text()
        password2 =self.cpwsignup.text()
        self.cond.setStyleSheet("color: red;")

        with open('database.csv',mode='a', newline='') as file:
            Writer = csv.writer(file,delimiter=",")
            self.signcounter = 0
            for line in rows : 
                if line[0] != user:
                    print("Username allowed")
                    self.signcounter += 1
                else:
                    print("Username existed!")
                    self.cond.setStyleSheet("color: red;")
                    self.cond.setText("Username already existed!")
                    break

            if (self.signcounter == len(rows)):
                if password == password2:
                    self.cond.setStyleSheet("color : green")
                    self.cond.setText("Account Created!")
                    Writer.writerow([user,password])
                    rows.append([user,password])
                else:
                    self.cond.setStyleSheet("color: red;")
                    self.cond.setText("Confirm Error!")
        file.close()
    def main(self):
        print("Back to main")        
        widget.setFixedHeight(201)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()-2)

class Main(QtWidgets.QMainWindow):
    
    def __init__(self,logincounter):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("main.ui", self)
        self.finstatbtn.clicked.connect(self.finstatwin)
        self.finstatbtn2.clicked.connect(self.finstatwin)
        self.finstatbtn3.clicked.connect(self.finstatwin)
        self.transbtn.clicked.connect(self.transwin)
        self.transbtn2.clicked.connect(self.transwin)
        self.logincounter = logincounter

        if len(transrows)-1 > self.logincounter:       
            for i in transrows[self.logincounter]:
                if i != '':
                    y = i.split(";")
                    y[1] = int(y[1])
                    trans.append(y)
                else:
                    trans.append(i) 
    def start(self):
        self.balance = login.finstat.balance
        blnmoney = "Rp.%d" % self.balance
        self.balancemoney.setText(blnmoney)
        if login.finstat.suminc != []:
            incmoney = "Rp.%d" % login.finstat.suminc[0]
            expmoney = "Rp.%d" % login.finstat.sumexp[0]
            a = login.finstat.suminc[0] - login.finstat.sumexp[0]
            profit = "Rp.%d" % a
            self.incomelbl.setText(incmoney)
            self.explbl.setText(expmoney)
            self.profitlbl.setText(profit)
        else:
            self.incomelbl.setText("0")
            self.explbl.setText("0")
            self.profitlbl.setText("0")    
    def transwin(self):
        print("Add Trans Button")
        widget.setCurrentIndex(widget.currentIndex()+2)
    
    def finstatwin(self):
        print("Finstat Button")
        login.finstat.start()
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def loaddata(self):
        # Load Database
        return self.logincounter
        
class Finstat(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("finstat.ui", self)
        self.graphbutton.clicked.connect(self.graphbtnclicked)  #Graph Button Callback    
        self.homebutton.clicked.connect(self.homebtnclicked)  #Graph Button Callback
        self.addbutton.clicked.connect(self.addbtnclicked)  #Graph Button Callback   
        self.start()
        self.monthselector.currentIndexChanged.connect(self.disp)

    def start(self):
        count = 0
        tempdate = []
        tempinc = []
        tempexp = []
        tempsuminc = 0
        tempsumexp = 0
        login.date.clear()
        login.month.clear()
        login.inc.clear()
        login.exp.clear()
        login.suminc.clear()
        login.sumexp.clear()
        
        self.monthselector.clear()
        
        for i in trans:
            if i != '':
                count += 1
                moncounter = i[0][0:7]

                mon = monthlist[int(moncounter[5:7])-1] + " "
                mon += moncounter[0:4]
                datelbl = i[0][8:10] + " " + mon
                if count == 1:
                    if mon not in login.month:
                        login.month.append(mon)      
                if login.month[len(login.month)-1] == mon:
                    tempdate.append(datelbl)  
                    if i[1] > 0:
                        tempinc.append(i[1])
                        tempexp.append(0)
                        tempsuminc += i[1]
                    elif i[1] < 0:
                        expe = i[1] * -1
                        tempinc.append(0)
                        tempexp.append(expe)
                        tempsumexp += expe
                else:
                    if mon not in login.month:
                        login.month.append(mon) 
                    login.inc.append(tempinc[:])
                    login.exp.append(tempexp[:])
                    login.suminc.append(tempsuminc)
                    login.sumexp.append(tempsumexp)

                    login.date.append(tempdate[:])
                    tempdate.clear()
                    tempinc.clear()
                    tempexp.clear()
                    tempsuminc = 0
                    tempsumexp = 0
                    tempdate.append(datelbl)
                    
                    if i[1] > 0:
                        tempinc.append(i[1])
                        tempexp.append(0)
                        tempsuminc += i[1]
                    
                    elif i[1] < 0:
                        expe = i[1] * -1
                        tempinc.append(0)
                        tempexp.append(expe)
                        tempsumexp += expe
            else:
                break
        if login.month != []:
            for a in login.month:
                self.monthselector.addItem(a)            
            self.monthselector.setCurrentIndex(0)
            #Add data to global variable 
        else:
            self.monthlabel.setText("-")
            self.monthincome.setText("-")
            self.monthexpen.setText("-")
        login.date.append(tempdate[:])
        login.inc.append(tempinc)
        login.exp.append(tempexp)
        login.suminc.append(tempsuminc)
        login.sumexp.append(tempsumexp)
        
        #First initialize on UI
        self.balance = sum(login.suminc) - sum(login.sumexp)
        balancelbl = "Rp.%d" % self.balance
        self.balancemoney.setText(balancelbl)

        self.date = login.date[:]
        self.inc = login.inc[:]
        self.exp = login.exp[:]
        self.suminc = login.suminc[:]
        self.sumexp = login.sumexp[:]
        self.month = login.month[:]
        self.disp(0)

    def disp(self,co):
        print("Initiating Display Financial Status Sequence")
        tempsumoth = 0
        tempexpoth = 0
        self.co = co    #Month Selector
        count = 1
        a = 1 
        for i in range(len(self.date[co])):  #Displaying 7 latest transactions on month GUI
            a = i+1
            if count < 7:
                datelbl = "top%dlabel" % a
                if self.inc[co][i] != 0:
                    inclbl = "Rp.%d" % self.inc[co][i]
                else:
                    inclbl = "-"
                if self.exp[co][i] != 0:
                    explbl = "Rp.%d" % self.exp[co][i]
                else:
                    explbl = "-"
                
                #Initiating for exec command    
                incomelbl = "top%dlabelinc" % a
                expenlbl = "top%dlabelexp" % a
                transdate = "self.%s.setText(self.date[co][i])" % datelbl
                transinc = "self.%s.setText(inclbl)" % incomelbl
                transexp = "self.%s.setText(explbl)" % expenlbl 
                #Call exec
                exec(transdate)
                exec(transinc)
                exec(transexp)
            else:
                if len(self.date[co]) == 7:
                    datelbl = "top%dlabel" % a
                    if self.inc[co][i] != 0:
                        inclbl = "Rp.%d" % self.inc[co][i]
                    else:
                        inclbl = "-"
                    if self.exp[co][i] != 0:
                        explbl = "Rp.%d" % self.exp[co][i]
                    else:
                        explbl = "-"
                    
                    #Initiating for exec command    
                    incomelbl = "top%dlabelinc" % a
                    expenlbl = "top%dlabelexp" % a
                    transdate = "self.%s.setText(self.date[co][i])" % datelbl
                    transinc = "self.%s.setText(inclbl)" % incomelbl
                    transexp = "self.%s.setText(explbl)" % expenlbl 

                    #Call exec
                    exec(transdate)
                    exec(transinc)
                    exec(transexp)
                else:
                    tempsumoth += self.inc[co][i] 
                    tempexpoth += self.exp[co][i]   
                    if len(self.date[co]) == count:

                        if tempsumoth != 0:
                            inclbl = "Rp.%d" % tempsumoth
                        else:
                            inclbl = "-"
                        if tempexpoth != 0:
                            explbl = "Rp.%d" % tempexpoth
                        else:
                            explbl = "-"
                        self.top7label.setText("Other")
                        
                        self.top7labelinc.setText(inclbl)
                        self.top7labelexp.setText(explbl)   
            count += 1
            a += 1
        while a <= 7:
                #Initiating for exec command    
                datelbl = "top%dlabel" % a
                incomelbl = "top%dlabelinc" % a
                
                expenlbl = "top%dlabelexp" % a
                n = "-"
                transdate = "self.%s.setText(n)" % datelbl
                transinc = "self.%s.setText(n)" % incomelbl
                transexp = "self.%s.setText(n)" % expenlbl 

                #Call exec
                exec(transdate)
                exec(transinc)
                exec(transexp)
                a += 1
        #Income and Expenditure

        suminclbl= "Rp.%d" % self.suminc[co]
        sumexplbl = "Rp.%d" % self.sumexp[co]
        
        #Set month label on GUI
        if self.month != []:
            self.monthlabel.setText(self.month[co])
            self.monthincome.setText(suminclbl)
            self.monthexpen.setText(sumexplbl)
        else:
            self.monthlabel.setText("-")
            self.monthincome.setText("-")
            self.monthexpen.setText("-")

    def graphbtnclicked(self):  #Started Graph GUI
        self.graphwin = Graph(self.co)
        self.graphwin.show()

    def addbtnclicked(self):
        print("Trans Button")
        widget.setCurrentIndex(widget.currentIndex()+1)
    def homebtnclicked(self):
        print("Home Button")
        login.finstat.start()
        login.main.start()
        widget.setCurrentIndex(widget.currentIndex()-1)

class Graph(QtWidgets.QMainWindow):
    def __init__(self,co):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("graph.ui", self)
        self.co = co
        self.graph.canvas.axes.clear()

        if len(login.finstat.inc[co]) != 0:   #Initiating First Display on GUI
            y = np.array(login.finstat.inc[co])
            if max(y) < 100000:
                y = y / 10000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Puluh Ribu Rupiah)")                
            elif max(y) < 1000000:
                y = y / 100000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Ratus Ribu Rupiah)")    
            else:
                y = y / 1000000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Juta Rupiah)")

            self.datetemp =[]
            for i in login.finstat.date[co]:
                self.datetemp.append(i[0:6])
            
            #Plot the Graph
            self.graph.canvas.axes.bar(self.datetemp,y, color = "#90ee90")
            self.graph.canvas.axes.set_xlabel("Transactions")
            self.graph.canvas.axes.set_title("Income")
            self.graph.canvas.axes.figure.tight_layout()
            self.graph.canvas.draw()
        self.graphselector.currentIndexChanged.connect(self.disp)
    
    def disp(self,select):
        print("Starting Graph Display Sequence")
        
        if select == 0:  #Income
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.set_title("Income")
            y = np.array(login.finstat.inc[self.co])
            if max(y) < 100000:
                y = y / 10000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Puluh Ribu Rupiah)")                
            elif max(y) < 1000000:
                y = y / 100000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Ratus Ribu Rupiah)")    
            else:
                y = y / 1000000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Juta Rupiah)")
            self.graph.canvas.axes.bar(self.datetemp,y, color = "#90ee90")
        
        elif select == 1: #Expenditure
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.set_title("Expenditure")
            y = np.array(login.finstat.exp[self.co])
            if max(y) < 100000:
                y = y / 10000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Puluh Ribu Rupiah)")                
            elif max(y) < 1000000:
                y = y / 100000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Ratus Ribu Rupiah)")    
            else:
                y = y / 1000000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Juta Rupiah)")
            self.graph.canvas.axes.bar(self.datetemp,y, color = "red")
        
        elif select == 2: #Total Balance
            self.graph.canvas.axes.clear()
            self.graph.canvas.axes.set_title("Balance")
            y = np.array(login.finstat.inc[self.co] + (np.array(login.finstat.exp[self.co])) * -1) 
            count = 0
            for i in y:
                if i != y[0]:
                    y[count] += y[count-1]
                count += 1
            if max(y) < 100000:
                y = y / 10000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Puluh Ribu Rupiah)")                
            elif max(y) < 1000000:
                y = y / 100000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Ratus Ribu Rupiah)")    
            else:
                y = y / 1000000
                self.graph.canvas.axes.set_ylabel("Rupiah(dalam Juta Rupiah)")
            
            self.graph.canvas.axes.bar(self.datetemp,y, color = "blue")
        
        self.graph.canvas.axes.set_xlabel("Transactions")
        self.graph.canvas.axes.figure.tight_layout()
        self.graph.canvas.draw()

class Exin(QtWidgets.QMainWindow):
    def __init__(self, balance):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("transaction.ui", self)
        self.balance = balance
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.transactData = []
        self.dateselected = QDate.currentDate().toPyDate()
        self.date.setDisplayFormat("d MMM yyyy")
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.balancemoney.setText(str(balance))
        self.savebutton.clicked.connect(self.Save)
        self.confirmbutton1.clicked.connect(self.conf1)
        self.confirmbutton2.clicked.connect(self.conf2)
        self.date.dateChanged.connect(self.set_date)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.homebutton.clicked.connect(self.home)
        self.statementbutton.clicked.connect(self.statement)

    def home(self):
        login.finstat.start()
        login.main.start()
        widget.setCurrentIndex(widget.currentIndex()-2)
    def statement(self):
        login.finstat.start()
        widget.setCurrentIndex(widget.currentIndex()-1)
    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.expline.clear()
            self.note.clear()
            self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        elif self.tabWidget.currentIndex() == 1:
            self.incline.clear()
            self.note.clear()
            self.date.setDateTime(QtCore.QDateTime.currentDateTime())

    def conf1(self):
        income = self.incline.text()
        try:
            income = int(income)
            self.trans = int(income)
            self.savebutton.setEnabled(True)
            self.savebutton.setStyleSheet("background-color: rgb(85, 255, 0);border-width: 2px;border-radius: 20px;padding: 4px;")
        except:
            warn = QMessageBox()
            warn.setWindowFlag(Qt.FramelessWindowHint)
            #warn.setStyleSheet("background-color:white;")
            warn.setText("Invalid Input!")
            warn.setIcon(QMessageBox.Warning)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setDefaultButton(QMessageBox.Ok)
            x = warn.exec_()
            pass
        
    def conf2(self): 
        expenditure = self.expline.text()
        try:
            expenditure = int(expenditure)
            self.trans = int(expenditure)*-1
            self.savebutton.setEnabled(True)
            self.savebutton.setStyleSheet("background-color: rgb(85, 255, 0);border-width: 2px;border-radius: 20px;padding: 4px;")
        except:
            warn = QMessageBox()
            warn.setWindowFlag(Qt.FramelessWindowHint)
            #warn.setStyleSheet("background-color:white;")
            warn.setText("Invalid Input!")
            warn.setIcon(QMessageBox.Warning)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setDefaultButton(QMessageBox.Ok)
            x = warn.exec_()
            pass
    
    def set_date(self):
        self.dateselected = self.date.date().toPyDate()

    def Save(self):
        note = self.note.text()
        if note == '':
            note = '-'  
        self.balance += self.trans 
        self.datepicked = str(self.dateselected)
        self.balancemoney.setText(str(self.balance))
        '''
        if self.trans < 0:
            trans =  "'" + str(self.trans)
        else:
            trans = str(self.trans)
            
        self.transactData.append(self.datepicked)
        self.transactData.append(trans)
        self.transactData.append(note)
        #transactData = self.datepicked+';'+trans+';'+note
        print(self.transactData)
        '''
        if trans == []:
            rowsadded = []
            rowsadded = [str(self.dateselected)]
            rowsadded.append(int(self.trans))
            rowsadded.append(note)
            trans.append(rowsadded[:])
        else:
            rowsadded = []
            rowsadded = [str(self.dateselected)]
            rowsadded.append(int(self.trans))
            rowsadded.append(note)          
            trans.append(rowsadded[:])
        count = 0
        for a in trans:
            if a == '':
                trans[count] = ['']
            count += 1

        trans.sort()
        trans.reverse()
        count = 0 
        for a in trans:
            if a == ['']:
                trans[count] = ''
            count += 1
        self.datepicked = None
        self.trans = 0
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.popup()
        
    def popup(self):
        msg = QMessageBox()
        msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setText("Transaksi Anda Telah Disimpan!")
        #msg.setStyleSheet("background-color:white;")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()        

if __name__ == "__main__":        
    #Load Database
    file = open('database.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    alldata = []
    rows = []
    transrows = []

    monthlist = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Des"]
    for row in csvreader:
        alldata.append(row)
    file.close()
    
    for a in alldata:
        rows.append(a[0:2][:])
    for a in alldata:
        transrows.append(a[2:len(a)][:])
    
    
    trans = []
    
    #Call Qt
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    greet= Greet()
    login = Login()
    signup = Signup()

    widget.addWidget(greet)
    widget.addWidget(login)
    widget.addWidget(signup)
    widget.setFixedHeight(308)
    widget.setFixedWidth(421)
    widget.show()
   
    try :
        sys.exit(app.exec_())
    except:
        if len(trans) != 0:
            count = 0
            newrows = []
            for transitem in trans:
                if transitem != '':
                    transitem[1] = str(transitem[1])
                    string1 = ""
                    string1 = ';'.join(transitem)
                    newrows.append(string1[:])
                else:
                    newrows.append('')   
                count +=1
            # for i in transrows:
            #     for endtrans in i:           
            count = 0
            logincount = login.main.logincounter
            file = rows[logincount]

            for i in newrows:
                file.append(i)

            alldata[logincount] = file
            with open('database.csv',mode='w', newline = '') as file:
                writer = csv.writer(file,delimiter=",")
                writer.writerow(header)
                for row in alldata:
                    writer.writerow(row)
        print("Exiting")
#class decleration with methods and veriables 
class pythontraning: #class decleration
 board = "white board" #class variable
 def bookwriting(self,name): #instance method decleration
      print("i am writing of book"+str(name));
 def listening(self,name):
      print('i am listening the class perfectly'+str(name));
 def understanding(self,name):
       print('i am understandning the class '+str(name));
 @staticmethod #static method decleration
 def boardreading():
     print("all of the plz read  board")
 @classmethod # class method decleration
 def boardreading1(cls):
     print("plz read board")
     
x = pythontraning(); # constructor creation with class name 
x.pen="marker" # instance  variable creation
x.bookwriting(x.pen) # object variable calling in  method by 
x.understanding("90%, x ")

y = pythontraning()
y.pen = "santoor"
y.bookwriting(y.pen)

print(pythontraning.board)
pythontraning.boardreading1(); #static method calling 
pythontraning.boardreading();# class method calling 

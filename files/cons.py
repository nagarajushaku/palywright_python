class pythontraning: # class decelaration 
    def __init__(self,a,b): # init method is decelare the constractor object by using self variable 
        print("this is constructor method");
        self.book = a; # assign the a value in book 
        self.pen =b;#assign the b value in pen 
    def dispaly(self): #decalre the  method with self argument 
        print("my book is " + self.book);# Print the book 
        print("my  pen is " + self.pen);#print the pen
x = pythontraning('white note book ' , 'marker pen');# create the object with constructor 
x.dispaly()#initilise the method 
y=pythontraning("white note book 2 " , 'marker pen 2 ');
y.dispaly();

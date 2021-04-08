class grandparent:
    def __init__(self,h):
        self.house= h;
    def grandparenthousepro(self):
        print("grandparent house is :"+ self.house)

class parent(grandparent):
    def __init__(self,c):
       self.car = c;
       super().__init__(h);
    def parenthousepro(self):
        print("parent house properties"+self.house);
        print("parent car is "+self.car)

class child(parent):
    def __init__(self,h,c,b):
        self.bike=b;
        super(). __init__(h,c);

    def childpro(self):
        print("child house i s:"+slef.house)
        print("child house i s:"+slef.car)
        print("child house i s:"+slef.bike)

sub1 = parent("doublexhouse ","hondacity","pleasure");
sub1.childpro();
sub1.parenthousepro();
sub1.grandparenthousepro();

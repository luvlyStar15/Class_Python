class Food:
    Cal = 0
    Price = 0

    def __str__(self):
        rep = "{0} Cal {1} Won".format(self.Cal, self.Price)
        return rep

chicken = Food()
print(chicken)

class Burger(Food):
    def __init__(self,patty,cheese=0):
        self.patty = patty
        self.cheese = cheese
        if (self.patty == 'beef'):
            self.Cal += 200
        elif (self.patty == 'chicken'):
            self.Cal += 300 

        if (self.cheese >= 1):
            self.Cal += cheese*100

    def computeprice(self,discount):
        if (self.patty == 'beef'):
            self.Price += 3000
        elif (self.patty == 'chicken'):
           self.Price += 2000
        if (self.cheese >= 1):
            self.Price += self.cheese*300
        self.discount = discount
        self.Price = round(self.Price*(100-self.discount)/100)

    def __str__(self):
        member_string = super().__str__()
        rep = "{0} burger ".format(self.patty) + member_string
        return rep

b1 = Burger('beef')
b2 = Burger('chicken',1)
b3 = Burger('beef',2)
b1.computeprice(0)
b2.computeprice(10)
b3.computeprice(20)
print(b1)
print(b2)
print(b3)

class Coffee(Food):
    def __init__(self,size,shot,milk='none'):
        self.size = size
        self.shot = shot
        self.milk = milk
        if(self.milk == 'none'):
            self.name = 'americano'
        else:
            self.name = 'cafelatte'
        
        if(self.size == 'short'):
            if(self.milk == 'regular'):
                self.Cal = (200-30*self.shot)*2+3*self.shot
            elif(self.milk == 'lowfat'):
                self.Cal = (200-30*self.shot)*1+3*self.shot
            else:
                self.Cal = 3*self.shot
        elif(self.size == 'tall'):
            if(self.milk == 'regular'):
                self.Cal = (300-30*self.shot)*2+3*self.shot
            elif(self.milk == 'lowfat'):
                self.Cal = (300-30*self.shot)*1+3*self.shot
            else:
                self.Cal = 3*self.shot
        elif(self.size == 'grandle'):
            if(self.milk == 'regular'):
                self.Cal = (400-30*self.shot)*2+3*self.shot
            elif(self.milk == 'lowfat'):
                self.Cal = (400-30*self.shot)*1+3*self.shot
            else:
                self.Cal = 3*self.shot

    def computeprice(self,discount):
        self.discount = discount
        if(self.milk == 'none'):
            if(self.size == 'short'):
                self.Price = 2500
            elif(self.size == 'tall'):
                self.Price = 3000
            elif(self.size == 'grandle'):
                self.Price = 3500
        else:
            if(self.size == 'short'):
                self.Price = 3000
            elif(self.size == 'tall'):
                self.Price = 3500
            elif(self.size == 'grandle'):
                self.Price = 4000
        if(self.size == 'short'):
            if(self.shot >=2):
                self.Price += (self.shot-1)*500
        elif(self.size == 'tall'):
            if(self.shot >=3):
                self.Price += (self.shot-2)*500
        elif(self.size == 'grandle'):
            if(self.shot >=4):
                self.Price += (self.shot-3)*500
        self.Price = round(self.Price*(100-self.discount)/100)

    def __str__(self):
        member_string = super().__str__()
        rep = "{0} {1} ".format(self.name,self.size) + member_string
        return rep

c1 = Coffee('short',2,'none')
c2 = Coffee('tall',2,'regular')
c3 = Coffee('grandle',4,'lowfat')
c1.computeprice(0)
c2.computeprice(10)
c3.computeprice(20)
print(c1)
print(c2)
print(c3)

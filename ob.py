from bs4 import BeautifulSoup
from bisect import bisect_right


with open('orders.xml', 'r') as f:
    data = f.read()
 

Bs_data = BeautifulSoup(data, "xml")

#print(Bs_data.find('AddOrder',{'book':'book-2'}).get('price'))



    

class book():

    def __init__(self,buy_in,sell_in,name):
        self.name = name
        self.buy = buy_in
        self.sell = sell_in

    def add_order(self,ordertype,price,vol):
        b = self.buy
        s = self.sell
        if(ordertype=='buy'):
            s_keys = s.keys()
            s_keys.sort(reverse=True)
            fou = False
            i = 0
            while(i<len(s_keys) and fou==False):
                if(s_keys[i]<=price):
                    if(s[s_keys[i]]>vol):
                        s[s_keys[i]] = s[s_keys[i]]-vol
                        fou = True
                    else:
                        vol = vol - s[s_keys[i]]
                        del s[s_keys[i]]
                i=i+1
            if(fou==False):
                if(b.has_key(price)):
                    b[price] = b[price]+vol
                else:
                    b[price] = vol
            self.buy= b
            self.sell = s
        else:
            s_keys = b.keys()
            s_keys.sort(reverse=True)
            fou = False
            i = 0
            while(i<len(s_keys) and fou==False):
                if(s_keys[i]>=price):
                    if(b[s_keys[i]]>vol):
                        b[s_keys[i]] = b[s_keys[i]]-vol
                        fou = True
                    else:
                        vol = vol - b[s_keys[i]]
                        del b[s_keys[i]]
                i=i+1
            if(fou==False):
                if(s.has_key(price)):
                    s[price] = s[price]+vol
                else:
                    s[price] = vol
            self.buy= b
            self.sell = s
        self.show()
        return

    def show(self):
        print("Buy ")
        b = self.buy
        s = self.sell
        b_keys = b.keys()
        s_keys = s.keys()
        b_keys.sort(reverse=True)
        s_keys.sort(reverse=True)
        for i in range(len(b_keys)):
            print(str(b[b_keys[i]])+"@"+str(b_keys[i]))
        print("Sell ")
        for i in range(len(s_keys)):
            print(str(s[s_keys[i]])+"@"+str(s_keys[i]))
        return

orderbook = {} #to store name as key and object book as value
orders= []# to store  orders details as list of lists [orderid,ordertype,book_name,price,vol]
for i in range(len(orders)):
    if(orderbook.has_key(orders[i][2])):
        orderbook[orders[i][2]].add_order(orders[i][1],orders[i][3],orders[i][4])
    else:
        book2 = book({},{},orders[i][2])
        book2.add_order(orders[i][1],orders[i][3],orders[i][4])
        orderbook[orders[i][2]]=book2



            


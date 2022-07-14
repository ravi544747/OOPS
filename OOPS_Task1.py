
import logging
logging.basicConfig(filename="test4.log", level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class String:
    try:
        def letter_extract(self,s):
            logging.info('now we are in letter extract method' )
            return s[0:300:3]
    except Exception as e:
        logging.exception(e)

    try:
        def str_rev(self,s):
            logging.info('now we are in letter reverse method' )
            return s[::-1]
    except Exception as e:
        logging.exception(e)

    try:
        def upper_rev(self,s):
            logging.info('now we are in  method reverse method after the conversion of uppercase' )
            s1=s.upper()
            return s1.split()

        def lower(self,s):
            logging.info('now we are in  method to convert a string in lower case' )
            return s.lower()

    except Exception as e:
        logging.exception(e)

class List:
    try:
        def list_rev(self, l):
            '''String reverseing with out using rev function'''
            logging.info('now we are in list rev method')
            return l[::-1]
        def Listcollection_extract(self,l):
            '''extraction of the list from given list'''
            l1=[]
            logging.info('your in the list extract method from a list')
            for i in l:
                if type(i)==list:
                    l1.append(i)
            return
        def Tuplecollection_extract(self,l):
            '''extraction of the tuple from given list'''
            l1=[]
            logging.info('your in the tuple extract method from a list')
            for i in l:
                if type(i)==tuple:
                    l1.append(i)
            return l1
        def dictcollection_extract(self,l):
            '''extraction of the dict from given list'''
            l1=[]
            logging.info('your in the dict extract method from a list')
            for i in l:
                if type(i)==dict:
                    l1.append(i)
            return l1
        def Dict_keys_extract(self,l):
            '''extraction of key elimnets of dict from a list'''
            l1=[]
            logging.info('extraction of dict keys from a list.....')
            for i in l:
                if type(i)==dict:
                    l1.append(i.keys())
            return l1
            logging.info(l1)

        def dict_values_extract(self,l):
            '''extraction of dict values from a given list'''
            l1 = []
            logging.info('extraction of dict values from a list')
            for i in l:
                if type(i) == dict:
                    l1.append(i.values())
            return l1
            logging.info(l1)
        def Num_extract(self,l):
            l1 = []
            '''extracting the numarical values from a given list'''
            logging.info('extracting the numerical values in a givnen list')
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            return l1

        def Num_extract_sum_prod(self, l):
            Sum , Prod= 0, 1
            '''extracting the numarical values and getting sum and product from a given list'''
            logging.info('extracting the numerical values in a givnen list')
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            Sum+=j
                            Prod*=j
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                Sum += g
                                Prod *= g
            return Sum, Prod


    except Exception as e:
        logging.exception(e)



s=String()
st="this is My First Python programming class and i am learNING python string and its function"
print(s.letter_extract(st))
logging.info(s.letter_extract(st))
logging.info('letter extraction in string has been done')
print(s.str_rev(st))
logging.info(s.str_rev(st))

print(s.upper_rev(st))
logging.info(s.upper_rev(st))

print(s.lower(st))
logging.info(s.lower(st))

l=List()
l1= [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
l2= [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


print(l.list_rev(l1))
logging.info(l.list_rev(l1))

print(l.Listcollection_extract(l1))
logging.info(l.Listcollection_extract(l1))

print(l.Dict_keys_extract(l1))
logging.info(l.Dict_keys_extract(l1))

print(l.dict_values_extract(l1))
logging.info(l.dict_values_extract(l1))

print(l.dictcollection_extract(l2))
logging.info(l.dict_values_extract(l2))

print(l.Tuplecollection_extract(l2))
logging.info(l.Tuplecollection_extract(l2))


print(l.Num_extract(l2))
logging.info(l.Num_extract(l2))

print(l.Num_extract_sum_prod(l2))
logging.info(l.Num_extract_sum_prod(l2))
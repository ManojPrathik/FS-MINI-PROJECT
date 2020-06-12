# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:13:20 2020

@author: krupa
"""


import csv
import time
import pandas

#variables
source_file_path = "C:\\Users\\krupa\\Downloads\\salespro.csv"
destination_file_path = "C:\\Users\\krupa\\res\\final.txt"

class HashTable:  
    def __init__(self):
        self.MAX = 100000
        self.arr = [[] for i in range(self.MAX)]
       
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
   
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
           
    def __setitem__(self, key, val, val1, val2):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==3 and element[0] == key:
                self.arr[h][idx] = (key,val,val1,val2)
                found = True
        if not found:
            self.arr[h].append((key,val,val1,val2))
       
    


def hashAndPrint():
    mini = {}              
    t = HashTable()      
    print("start hash \n")
    start3=time.time()
    with open(source_file_path,"r") as f:
           for line in f:
            tokens = line.split(',')
            OrderID =tokens[0].rstrip("\n")
            Country = tokens[1].rstrip("\n")
            Region = tokens[2].rstrip("\n")
            Itemtype = tokens[3].rstrip("\n")
            mini[OrderID] = Country,Region,Itemtype
            t.get_hash(OrderID)
            t.__getitem__(OrderID)
            t.__setitem__(OrderID,Country,Region,Itemtype)
   
    

    with open(destination_file_path, 'w') as f:
        for a in t.arr:
            values = ''
            #str.split("")
            for k in a:
                values = values + '(' + k[0].rstrip("\n") + ',' + k[1].rstrip("\n") + ',' + k[2].rstrip("\n") + ',' + k[3].rstrip("\n") +'),'
            f.write(values)
            f.write("\n")
   
   
    print("The file is hashed successfully")
    end3=time.time()
    print('Process completed in',end3-start3,'seconds \n')

def append():
    
    with open(source_file_path,'a+', newline='') as f:
        fieldnames=['Order ID','Region','Country','Item Type']
        tgwrite=csv.DictWriter(f,fieldnames=fieldnames)
        orderid=input('Enter unique ID\n')
        country=input('Enter the name of the country\n')
        region=input('Enter the region\n')
        item=input('Enter type of item\n')
        start=time.time()
        add={'Order ID': orderid,
             'Country':country,
             'Region':region,
             'Item Type':item}
        tgwrite.writerow(add)
        end=time.time()
        print('process completed in',end-start,'seconds')
    hashAndPrint()
    f.close()
def delete():
    start1=time.time()
    a=pandas.read_csv(source_file_path, index_col=0)
    deleteID=input('Enter the ID you want to delete\n')
    start1=time.time()
    a.drop(deleteID,axis=0,inplace=True)
    a.to_csv('C:\\Users\\krupa\\Downloads\\salespro.csv')
    print('Record deleted successfully \n')
    end1=time.time()
    print('Process completed in',end1-start1,'seconds \n')
    hashAndPrint()
    
def searchByKey():
    
    key=(input("Enter the key you want to search \n"))
    start2=time.time()
    keyfound=False
    t = HashTable()
    hashkey = t.get_hash(key)
    with open(destination_file_path) as f:
        for i, line in enumerate(f):
            if( i ==  int(hashkey)):
                e = line.split('),')
                for s in e:
                    r = s.split(',')
                    k = r[0].replace('(', '')
                    if k==key:
                        keyfound=True
                        print('key found at:' + str(hashkey))
                        res='Order ID:'+k+', \nRegion:'+r[1]+', \nCountry:'+r[2]+', \nItem Type:'+r[3]
                        print(res)
       
   
    if(keyfound==False):
        print('Key entered is incorrect')
    end2=time.time()
    print('Process completed in',end2-start2,'seconds')
   
           
def main():
     while True:
        print('1.Insert a record \n2.Delete a record \n3.Hash the file \n4.Search a record \n5.Exit')
        Choice=int(input('Enter your choice\n'))
        if Choice==1:
            append()
        elif Choice==2:
            delete()
        elif Choice==3:
            hashAndPrint()
        elif Choice==4:
            searchByKey()
        elif Choice==5:
            print('Thank you')
            break
        else:
            print('Invalid choice \nPlease try again \n')
           
main()

import numpy as np 
import pandas as pd
from collections import Counter
from itertools import combinations
from itertools import permutations 


print("Minimum Support: ")
minSup = input()
minSup = str(minSup)
print("Minimum confidence: ")
minCon = input()
minCon = str(minCon)

if minSup[-1]=="%":
    minSup=minSup[:-1]
    minSup=float(minSup)/100
else: minSup = float(minSup)
if minCon[-1]=="%":
    minCon=minCon[:-1]
    minCon=float(minCon)/100
else:minCon = float(minCon)


data = pd.read_excel('CoffeeShopTransactions.xlsx',usecols = ['Item 1','Item 2','Item 3'])
data.drop
data.values

transactions = []
for i in range(0,len(data)):
    transactions.append([str(data.values[i,j])for j in range (0,3)])
print(transactions)
minSupCount = (minSup*len(data))

def ord_comb(l,n):
    return list(combinations(l,n))

def getSupportCount(x):
        ctr=0
        for j in range(0,len(data)):
            set1 = set(transactions[j])
            set2 = set(x) 
            if(set2.issubset(set1)):
                ctr += 1
        return int(ctr)     
print("-----------------------All Items and its support count----------------------------")

items = dict()
support=0
x=0

lsup=list()

for i in range(0,len(data)):
    for j in range (0,data.columns.size):
        lsup.append(transactions[i][j])
        if transactions[i][j] not in items:
            items[transactions[i][j]] = getSupportCount(lsup)
        lsup.clear()
print(items)


print("--------------------filteration the items less than min support---------------------")

for key in list(items.keys()):   
    if items[key] < minSupCount:
        del items[key]
  
print(items)      


print("-------------------------------------------------------------------------------------")
sets=2    
itemset=dict()
freqitems=dict()
x=0
o=1
while True :   
    l= ord_comb(items,sets)  
    for i in range(0,len(l)):     
        ctr=getSupportCount(l[i])     
        if sets>2 and x>0:             
            for k in range(len(l)):       
              previous = list(prev)   
              comb = ord_comb(l[k],sets-1) 
              for b in range(len(comb)):
                if comb[b] not in previous and o==0 :
                    o-=1
                    del l[k]      
        if ctr >= minSupCount:
            itemset[l[i]]= ctr            
    if (len(itemset)==0):break
    else:
        sets+=1
        prev=dict()
        prev=freqitems
        freqitems.clear()
   
    print('*************',sets-1,'itemset *********************')        
    print(itemset)
    for key in list(itemset.keys()): 
        freqitems[key]=itemset[key]                   
    itemset.clear()
    x+=1
print('#################-Association Rules with their Confidene-######################')
freqitemslist=list(freqitems)
l=list()
for i in range (len(freqitemslist)):
    for j in range(sets-1):
        for k in range (sets-1):
          
            if(sets-1!=2):
                comb = list(combinations(freqitemslist[i], (sets-2)))
                if freqitemslist[i][k] not in comb[j]:   
                    conf1=getSupportCount(freqitemslist[i])/items[freqitemslist[i][k]]
                    print(freqitemslist[i][k],'->', comb[j])
                    print('conf = ',conf1,'=',conf1*100,'%')
                    if conf1>=minCon:
                        print('strong')
                    conf2=getSupportCount(freqitemslist[i])/getSupportCount(comb[j])
                    print(comb[j],'->',freqitemslist[i][k] )
                    print('conf =',conf2,'=',conf2*100,'%')
                    if conf2>=minCon:
                        print('strong')

                    if comb[j] not in l: l.append(comb[j])
                        

if sets-1==2: l=freqitemslist

for i in range (len(l)):

                            conf1 = getSupportCount(l[i])/items[l[i][0]]
                            print(l[i][0],'->',l[i][1])
                            print('conf =',conf1,'=',conf1*100,'%')
                            if conf1>=minCon:
                                print('strong')
                            conf2=getSupportCount(l[i])/items[l[i][1]]
                            print(l[i][1],'->',l[i][0] ) 
                            print('conf =', conf2 ,'=',conf2*100,'%' )
                            if conf2>=minCon:
                                print('strong')


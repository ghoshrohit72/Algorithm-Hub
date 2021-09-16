'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
from itertools import permutations
def isPrime(n):
    i=2
    while i <= n**0.5:
        if n%i==0:
            return False
        i=i+1
    return True     

def primePermutations(n):
    permutationList=[]
    perms= permutations(str(n))
    for ele in perms:
        if isPrime(int(''.join(ele))):
           permutationList.append(int(''.join(ele)))
    return  permutationList     


Number=1001
primeList=[]

while Number < 10000:
    if isPrime(Number):
        if sorted(str(Number)) not in primeList:
            primeList.append(sorted(str(Number)))
            lst=sorted(primePermutations(Number))
            for i in range(len(lst)-2):
                desired=[]  
                for j in range(i+1,len(lst)-1):  
                    for k in range (j+1,len(lst)):
                        if lst[k]-lst[j]==lst[j]-lst[i] > 0:
                            desired.append(lst[i])  
                            desired.append(lst[j]) 
                            desired.append(lst[k])
                            print(desired)
                            break
                    if len(desired)==3:
                        break  
                if len(desired)==3:
                    break
    Number=Number+1            

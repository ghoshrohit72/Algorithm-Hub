'''
Write a program that prints the longest substring of s in which
the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print..
Longest substring in alphabetical order is: beggh
'''

s= input("Enter your string: ")
alphabet='abcdefghijklmnopqrstuvwxyz'
longest_substring_list=[]

for i in range(len(s)):
    temp=[s[i]]
    for j in range(i+1,len(s)):
           if alphabet.index(s[j-1]) > alphabet.index(s[j]):
                 if len(temp) > len(longest_substring_list):
                     longest_substring_list=temp
                     break
                 break
           else:
                 temp.append(s[j])
                 if len(temp) > len(longest_substring_list):
                     longest_substring_list=temp
          
print("Longest substring in alphabetical order is: "+''.join(map(str,longest_substring_list)))        

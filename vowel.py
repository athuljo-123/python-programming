n=input("enter the word:")
vowels=['a','e','i','o','u']
list=[]
for x in n:
    if(x in vowels and x not in list):
     list.append(x)
print("vowels present in the given word are:",list)

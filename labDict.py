"""# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0568323222 |
| Mohammed | 0522222232 |
| Khadijah | 0532335983 |
| Abdullah  | 0545341144 |
| Rawan    | 0545534556 |
| Faisal   | 0560664566 |
| Layla    | 0567917077 |


- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".

## Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.


"""

nubmers={
    '0568323222':"Amal",
    '0522222232':"Mohamed",
    '0532335983':"Khadija",
    '0545341144':"Abduallh",
    '0545534556':'Rawan',
    '0560664566':"Faisal",
    '0567917077': 'Layla'
}
print("Welcome to phone number book : ")

user_input=input("Enter a phone number u would like to search for : ")

if len(user_input) <10  or not user_input.isdigit():
    print("This is invalid number")
else:
    print(nubmers.get(user_input,"Sorry, the number is not found"))

def rearrange_list(arr : list ) -> list:
    for index ,number in enumerate (arr) :
        if number==0:
            arr.pop(index)
            arr.append(0)
            print()
    print(arr)

rearrange_list([5, 0, 34, 9, 0, 13, 8])
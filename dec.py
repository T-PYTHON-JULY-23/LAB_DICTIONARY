"""
    
    Build a phone book program that receives the phone number 
    (Use Input to let the user provide the number),
    and returns the name of the owner.
"""
phone_book={"Amal":"0568323222",
            "Mohammed":"0522222232",
            "Khadijah":"0532335983",
            "Abdullah":"0545341144",
            "Rawan":"0545534556",
            "Faisal":"0560664566",
            "Layla":"0567917077"}

number=str(input("enter the number you lock for: "))

def get_key(val):
    if len(number) != 10:
     return "This is invalid number",
    elif number.isalnum()==False:
     return "This is invalid number",
    
    for key, value in phone_book.items():
        if val == value:
            return "the name for the number is " ,key
 
    return "Sorry, the number is not found",

print(*get_key(number))

"""
Q2:Write a function that receives a list containing the following numbers :

[5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
"""
def arrange_list(list1):
    count = 0
    n= len(list1)
    for i in range(n):
        if list1[i] != 0:
            list1[count] = list1[i]
            count+=1
    while count < n:
        list1[count] = 0
        count += 1
list1=[5, 0, 34, 9, 0, 13, 8]

print("list befor arranged",list1)
arrange_list(list1)

print("list after arranged",list1)
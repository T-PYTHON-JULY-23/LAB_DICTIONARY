# Q1:Build a phone book program that receives the phone number 
#(Use Input to let the user provide the number), and returns the name of the owner. 
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

number = input("Enter the phone number: ")
if len(number) != 10 or not number.isnumeric():
    print("This is an invalid number")
elif number in phone_book:
    print(f"The owner of the number {number} is {phone_book[number]}")
else:
    print("Sorry, the number is not found")

# Q2:Write a function that receives a list containing the following numbers : 

def zeros_to_end(lst):
    
    non_zero_lst = []
    zero_lst = []
    for x in lst:
        if x != 0:
            non_zero_lst.append(x)
        else:
            zero_lst.append(x)
    
    return non_zero_lst + zero_lst


mylsit = [5, 0, 34, 9, 0, 13, 8]
arranged_lst = zeros_to_end(mylsit)
print(arranged_lst)


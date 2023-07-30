phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

number = input("Please enter the phone number: ")

if not number.isdigit():
    print("This is invalid number")
elif len(number) != 10:
    print("This is invalid number")
else:
    for name, num in phone_book.items():
        if num == number:
            print(f"The owner of this number is {name}")
            break
    else:
        print("Sorry, the number is not found")
        

def rearrange_list(lst):
    zeros = lst.count(0)
    lst = [num for num in lst if num != 0]
    lst += [0] * zeros
    return lst
my_list = [5, 0, 34, 9, 0, 13, 8]
new_list = rearrange_list(my_list)
print(new_list)
    

phone_number = {
    "0568323222" : "Amal",
    "0522222232" : "Mohammed",
    "0532335983" : "Khadijah",
    "0545341144" : "Abdullah",
    "0545534556" : "Rawan" ,
    "0560664566" : "Faisal",
    "0567917077" : "Layla"
}



number = input("enter a phone number: ")

def  phone_book_program():
    entered_number = phone_number.get(number, "Sorry, the number is not found")
    print(f"The owner of the {number} is: {entered_number} ")


    if len(number) < 10 or not number.isdigit()   :
        print("this is invalid number")
    return 




phone_book_program()



##Q2:Write a function that receives a list containing the following numbers : 


def rearrange_list(): 
    my_list = [5, 0, 34, 9, 0, 13, 8]
    for num in my_list:
        if num==0:
            my_list.append(0)
            my_list.remove(0)
    print(my_list)

rearrange_list()







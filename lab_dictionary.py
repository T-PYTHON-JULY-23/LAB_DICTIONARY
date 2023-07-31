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











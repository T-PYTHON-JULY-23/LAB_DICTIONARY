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


def rearrange_list(num_list): 
    k= 0
    for i in num_list:  
        if i:  
            num_list[k] = i  
            k = k + 1  
    for i in range(k, len(num_list)):  
        num_list[i] = 0


    return num_list  

num_list = [5, 0, 34, 9, 0, 13, 8] 
order_list = rearrange_list(num_list)  
print(order_list)







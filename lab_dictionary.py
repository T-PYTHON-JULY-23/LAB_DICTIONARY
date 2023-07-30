phone_number= {
    "Amal":"05683232222",
    "Mohammed":"0522222232",
    "Khadijah":"0532335983",
    "Abdullah":"0545341144" ,
    "Rawan ":"0545534556" ,
    "Faisal":"0560664566",
    "Layla":"0567917077" 
    }

number = input (" please enter phone number: ")

if len(number) < 10 or number.isdigit() != True:
     print ("this is invalid number")
else:
    user = phone_number.get(number,"Sorry, the number not found ")
    print(f"The owner for the {number} is: {user}")
   




#Q2
def new_list():
    num_list = [5,0,34,9,0,13,8]
    for i in num_list:
        if i == 0:
            list.remove(0)
            list.append(0) 
        return num_list

print(new_list())



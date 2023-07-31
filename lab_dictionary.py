phone_number= {
    "05683232222":"Amal",
    "0522222232":"Mohammed",
   "0532335983":"Khadijah",
    "0545341144":"Abdullah" ,
    "0545534556":"Rawan" ,
    "0560664566":"Faisal",
    "0567917077" :"Layla"
    }

number = input (" please enter phone number: ")

if len(number) < 10 or not number.isdigit() :
     print ("this is invalid number")
else:
    user = phone_number.get(number,"Sorry, the number not found ")
    print(f"The owner for the {number} is: {user}")
   




#Q2

def new_list():
    num_list=[5,0,34,9,0,13,8]
    for i in num_list:
        if i == 0:
            num_list.remove(0)
            num_list.append(0)
    print(num_list)
        
new_list()



print(new_list())



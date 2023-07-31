phone_number= {"0568323222":"Amal",
               "0522222232":"Mohammed",
               "0532335983":"Khadijah",
               "0545341144":"Abdullah",
               "0545534556":"Rawan",
               "0560664566":"Faisal",
               "0567917077":"Layla"}
user_number = input("please enter the number : ")
if len(user_number) == 10 and user_number.isdigit() :
    phone_owner = phone_number.get(user_number,"Sorry, the number is not found")
    print(f"this number ( {user_number} ) is for : {phone_owner}")
else :
    print("This is invalid number")

#------------------------------------------------------------------------------------------
###Q2:
my_list = [5, 0, 34, 9, 0, 13, 8]
def arrangment_function(list):
   list.sort(reverse= True)
   return list


print(arrangment_function(my_list))
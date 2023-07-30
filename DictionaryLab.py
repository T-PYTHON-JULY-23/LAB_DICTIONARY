phone_book = {
    "0568323222":"Amal",          
    "0522222232":"Mohammed" ,
    "0532335983":"Khadijah" ,
    "0545341144":"Abdullah" ,
    "0545534556":"Rawan"    ,
    "0560664566":"Faisal"  ,
    "0567917077"  :"Layla" 
    }


print("Number book app \n" )

user_choice = input("fill in the number: ")
if not user_choice.isdigit() :
    print("This is invalid number")
elif len(user_choice)<10:
    print("This is invalid number")
elif len(user_choice)>10:
  print("This is invalid number")
else:
    phone_number = phone_book.get(user_choice,"Sorry, the number is not found")
    print(f"The name of the owner of {user_choice} is: {phone_number} ")


#Q2

print("Qustion number 2: ")
list=[5, 0, 34, 9, 0, 13, 8]

def rearranges(list):
  zeros = []
  non_zeros = []
  for number in list:
    if number == 0:
      zeros.append(number)
    else:
      non_zeros.append(number)

  return non_zeros + zeros

rearranged_list = rearranges(list)
print("The rearranged list is:", rearranged_list)
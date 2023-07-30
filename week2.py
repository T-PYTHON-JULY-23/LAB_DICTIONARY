

#q1


phoneBook = {
    "0568323222":"Amal",          
    "0522222232":"Mohammed" ,
    "0532335983":"Khadijah" ,
    "0545341144":"Abdullah" ,
    "0545534556":"Rawan"    ,
    "0560664566":"Faisal"  ,
    "0567917077"  :"Layla" 
    }


print("phone book program \n" )

user_input = input("Enter the number to know his owner: ")
if not user_input.isdigit() :
    print("This is invalid number")
elif len(user_input)<10:
    print("This is invalid number")
elif len(user_input)>10:
  print("This is invalid number")

else:
  phone_number = phoneBook.get(user_input,"Sorry, the number is not found")
  print(f"The name of the owner of {user_input} is: {phone_number} ")

  
#q2


list=[5, 0, 34, 9, 0, 13, 8]

def rearranges(list):
  zeros = []
  rearrangeList = []
  
  for number in list:
     if number == 0:
       zeros.append(number)
     else:
       rearrangeList.append(number)
  
  rearrangeList.extend(zeros)
  print("The rearranged list is:", rearrangeList)

 
    

rearranges(list)

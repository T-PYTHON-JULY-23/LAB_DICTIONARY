phoneNum= input("Enter the phone number:")

num_dict = {"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah","0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}

name= num_dict.get(phoneNum,"Sorry, the number is not found")


if len(phoneNum) <10 or len(phoneNum) >10 :
    print("This is invalid number")
elif phoneNum.isnumeric() == False:
    print("This is invalid number")
else:
     print (f"The phone number: {phoneNum} belongs to: {name}")



number_list=[5, 0, 34, 9, 0, 13, 8]
def numbers_list(number_list)-> list:
    
  number_list.sort(reverse=True)
  return number_list



print(numbers_list(number_list))

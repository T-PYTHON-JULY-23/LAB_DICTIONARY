#lab dictionary 
#q1
  
keyNumber = input ("Enter the phone number: ")

my_dictionary = {"0568323222" : "amal",
                 "0522222232": "mohammed",
                 "0532335983" : "Khadijah" ,
                 "0545341144" : "Abdullah",
                 "0545534556" : "Rawan",
                 "0560664566" : "Faisal" ,
                 "0567917077" : "Layla"}

elment_value = my_dictionary.get("key")
if len(keyNumber) != 10:
    print("This is invalid number")

else:
    if keyNumber in my_dictionary:
        print("Owner: " + my_dictionary[keyNumber])
    else:
        print("Sorry, the number is not found")


#q2
myList = [5, 0, 34, 9, 0, 13, 8]
def move_zeros(myList):
    zeros = []
    newList = []
    for num in myList:
        if num == 0:
            zeros.append(num)
        else:
            newList.append(num)
    newList.extend(zeros)
    return newList

newList = move_zeros(myList)
print(newList) 





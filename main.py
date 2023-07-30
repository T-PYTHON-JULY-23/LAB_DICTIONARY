
numberBook={'Amal':'0568323222','Mohammed':'0522222232','Khadijah':'0532335983','Abdullah':'0545341144',
            'Rawan':'0545534556','Faisal':'0545534556','Layla':'0567917077'}
phoneNumber = input("Enter phone number: ")
if not len(phoneNumber) ==10 or not phoneNumber.isnumeric():
    print('This is invalid number')
for key, value in numberBook.items():
    if value == phoneNumber:
        print(key)
        break
else:
    print('Sorry, the number is not found')
print('-------Q2-------')
myList = [5, 0, 34, 9, 0, 13, 8]
newList=[]
count =0
for value in myList:
    if value != 0:
        newList.append(value)
    else:
        count=count+1
while count !=0:
    newList.append(0)
    count =count-1
print(newList)

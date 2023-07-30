phone_book= {
    "Amal":'0568323222',
    "Mohammed":'0522222232',
    "Khadijah":'0532335983',
    "Abdullah":'0545341144',
    "Rawan":'0545534556',
    "Faisal":'0560664566',
    "Layla":'0567917077',
    "Naif": '0533835115'
    }
user_num = input("Enter the number : ")
if len(user_num) != 10 or not user_num.isdigit():
    print("This is invalid number")
else:
    for key, Value in phone_book.items():
        if Value==user_num:
            print(key,Value,"is found")
            break
    else:
        if Value !=user_num:
            print("Sorry, the number is not found")


def rearranges(list_num):
    for i in list_num:
        if i==0:
            list_num.remove(0)
            list_num.append(0)
    print(list_num)
    
rearranges([5, 0, 34, 9, 0, 13, 8])
        






            


        





        
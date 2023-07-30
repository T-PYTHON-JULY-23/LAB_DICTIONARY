Number_book= {
    "Amal":'0568323222',
    "Mohammed":'0522222232',
    "Khadijah":'0532335983',
    "Abdullah":'0545341144',
    "Rawan":'0545534556',
    "Faisal":'0560664566',
    "Layla":'0567917077',
    }


n = (input("what is the number?"))
if not n.isdigit() or len(n) != 10:
    print("This is an invalid number")
else:
    for key,value in Number_book.items():
        if n == value:  
         print(key,value)
         break
        
    else:
        print("Sorry, the number is not found")

           
print("=================================================")
lst = [5, 0, 34, 9, 0, 13, 8]
new_lst = lst
new_lst.sort(reverse=True)
print(new_lst)
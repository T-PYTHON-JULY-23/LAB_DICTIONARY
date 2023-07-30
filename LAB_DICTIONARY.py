#Q1
def phoneB():
    phone_book={
        "0568323222":"Amal",
        "0522222232":"Mohammed",
        "0532335983":"Khadijah",
        "0545341144":"Abdullah",
        "0545534556":"Rawan",
        "0560664566":"Faisal",
        "0567917077":"Layla",
        }#why i can't use int start with 0????????
    
    print("Phone Book  App")
    user_Pname = input("Fill in the  phone number : ")
    userlen = len(user_Pname)
    if userlen < 10 or userlen > 10:
        print("This is invalid number more or less then 10 numbers")
    elif user_Pname.isdigit() != True:
        print("This is invalid number not digit")
    else:
        user_ch = phone_book.get(user_Pname,"Sorry, the number not found ")
        print(f"The owner for the {user_Pname} is: {user_ch}")

#Q2
def rearranges():
     list_nums = [5, 0, 34, 9, 0, 13, 8]
     list_len = len(list_nums)
     for val in list_nums:
      if val == 0:
            list_nums.remove(val)
            list_nums.append(val)
     return list_nums

#teast Q1
phoneB()
#teast Q2
print(f"The arranged list : {rearranges()}")
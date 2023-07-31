phone_book = {
    "Amal" : "0568323222",
    "Mohammed" : "0522222232",
    "Khadijah" : "0532335983",
    "Abdullah" : "0545341144",
    "Rawan" : "0545534556",
    "Faisal" : "0560664566",
    "Layla" : "0567917077"  
}

def find_name(phoneNum:str) -> str:
    '''This function will find the phone number is registered to whom? '''
    if len(phoneNum) > 10 or len(phoneNum) < 10:
        return f"{phoneNum} : This is invalid number"
    
    for num in phoneNum:
        if not num.isdigit():
            return f"{phoneNum} : This is invalid number, you entered '{num}' "
        
    for phone in phone_book:
        if phone_book[phone] == phoneNum:
            return phone
    else:
        return "Sorry, the number is not found"

chck_phone = input("Please Enter Phone number to search : ")
print(find_name(chck_phone))


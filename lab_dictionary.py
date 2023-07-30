phone_number = {
    568323222 : "Amal",
    522222232 : "Mohammed",
    532335983 : "Khadijah",
    545341144 : "Abdullah",
    545534556 : "Rawan" ,
    560664566 : "Faisal",
    567917077 : "Layla"
}

number = input("enter a phone number: ")

def  phone_book_program():
    entered_number = phone_number.get(number, "Sorry, the number is not found")
    print(f"The owner of the {number} is: {entered_number} ")


    if len(number) > 10   :
        print("this is invalid number")
    elif len(number)< 10 :
        print("this is invalid number")
    else:
        print("this is invalid number") 
    return 

phone_book_program()


'''
number = input("Enter the number: ")

def phone_book_program():
    trooo = phone_number.get(number, "Sorry we don't have the temperature for this city")
    print(f"The temperature for the {number} is: {trooo} c")
    return 


'''



 



'''


'''


'''
 
 def value_exists(value, list_of_dicts):
    for dictionary in list_of_dicts:
        if value in dictionary.values():
            return True
    return False
 '''

'''

entered_number = phone_number.get(number, "Sorry, the number is not found")
print(f"the owner of the {number} is: {entered_number} ")
print(phone_number)

'''





''' def phone_guide():

  guide_number = int(input("Enter a number:"))

  numbers = {"Amal": 1111111111, "Mohammed": 2222222222, "Khadijah": 3333333333, "Abdullah": 4444444444}

  for key, value in numbers.items():
    if guide_number == value:
      return value

  return "This is invalid number"

phone_guide() '''

'''

    result = " "
    for key ,value  in phone_number.items():
        if number == value:
            print(key)
        else:
            print("Sorry, the number is not found")

    return result
'''


'''

cities_temps = {
    "Riyadh" : 47, 
    "Dammam" : 44, 
    "Kharj":46, 
    "Mecca":39
    }

print("Weather App")
user_choice = input("fill in the name of the city: ")

city_temp = cities_temps.get(user_choice, "Sorry we don't have the temperature for this city")
print(f"The temperature for the {user_choice} is: {city_temp} c")

'''



'''

    result = " "
    for key ,value  in phone_number.items():
        if number == value:
            print(key)
        else:
            print("Sorry, the number is not found")

    return result


'''
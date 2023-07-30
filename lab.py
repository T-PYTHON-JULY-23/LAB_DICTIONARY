#1
phone_book = {
    'Amal': '0568323222',
    'Mohammed': '0522222232',
    'Khadijah': '0532335983',
    'Abdullah': '0545341144',
    'Rawan': '0545534556',
    'Faisal': '0560664566',
    'Layla': '0567917077'
}
number = input("Enter a phone number: ")
for name, value in phone_book.items():
    if number == value:
        print(f"{name}")
if not number.isdigit():
    print("This is invalid number")
elif len(number) != 10:
    print("This is invalid number check u number")
elif number not in phone_book.values():
    print("Sorry, the number is not found")
#2
def Zero_funcation(lst):
    new = []
    for n in lst:
        if n != 0:
            new.append(n)
    new.extend([0]* lst.count(0))
    return new

print(Zero_funcation([5, 0, 34, 9, 0, 13, 8]))

#Bonus:
# Store data in dictionary
weather = {}


def input_data():
    city = input("Enter city: ")
    date = input("Enter date (DD/MM/YYYY): ")
    temp = input("Enter temperature: ")

    # Add to dictionary
    if city not in weather:  # New city
        weather[city] = {date: temp}
    else:
        weather[city][date] = temp


def query_city():
    city = input("Enter city to query: ")
    if city in weather:
        dates = weather[city].keys()
        for date in dates:
            print(date, weather[city][date])


while True:
    print("1. Add data")
    print("2. Query data")
    print("3. Exit")
    choice = input("> ")

    if choice == '1':
        input_data()
    elif choice == '2':
        query_city()
    elif choice == '3':
        break
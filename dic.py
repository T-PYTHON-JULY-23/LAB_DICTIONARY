numbers = {'0568323222': "Amal",'0522222232' : "Mohamed",'0532335983':"Khadijah",' 0545341144':"Abdullah",'0545534556':"Rawan",'0560664566':"Faisal",'0567917077':"Layla"}
phone_number = input(" please enter A phone Number:")
if len(phone_number) < 10 or not phone_number.isdigit():
    print ("this is invalid number")
else:
    print(numbers.get(phone_number,"Sorry , the number is not found"))
    # Q2
'''def new_list(list,f):
        co = 0
        for i in range (f):
            if list [i] != 0:
             list[co] = list [i]
                co += 1
                while co < f:
                    list[co]= 0
                    co += 1
                    list = [5,0,34,9,0,13,8]
                    f = len(list)
                    new_list(list,f)
                    print(list)'''
def new_list(list):
    for i in list:
        if i == 0:
            list.remove(0)
            list.append(0)
            print(list)
            new_list({5,0,34,9,0,13,8})
#a question 2
my_list=[5, 0, 34, 9, 0, 13, 8]
'''rearranges the list so that the zeros are the end of the list, and finally returns the arranged list'''
num = len(my_list)
j = 0
for i in range(num):
    if my_list[i] != 0:
        my_list[j], my_list[i] = my_list[i], my_list[j]  
        j += 1
print(my_list)


#a question 1
user_name = {
5568323222: 'Amal',
5522222232: 'Mohammed',
5532335983: 'Khadijah',
5545341144: 'Abdullah',
5545534556: 'Rawan',
5560664566: 'Faisal',
5567917077: 'Layla'
  }
'''Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.'''
def phone_book(x):
    
        
    if not x.isdigit() or len(x)!=10:
        print('This is invalid number')
    else:
        num = int(x)
        if num in user_name:
            print(user_name[num])
        else:
            print('Sorry, the number is not found')
 
phone_book(input('Please Enter The Number: '))


 



            



def phone_book (phoneNum):
  phoneBookDic = { 568323222 :"Amal" , 522222232:"Mohammed", 532335983 :"Khadijah" ,545341144 : "Abdullah ",
            545534556 : "Rawan" ,560664566 : "Faisal", 567917077 : "Layla"}
  
  symbols=("!","@","#","$","%","^","&","*","()","/",":",">","<","=","+","-")
   
  if phoneNum in phoneBookDic:

     print(phoneBookDic[phoneNum])
     
  elif  isinstance(phoneNum,str) or phoneNum == symbols:
       print ("This is invalid number") 
       
    
  elif len(str(phoneNum)) < 10 or  len(str(phoneNum))  > 10:
       print ("This is invalid number")
        

  else: 
      print("Sorry, the number is not found ")
        
phone_book(522222232)





def funReceives () :
 list1 = [5, 0, 34, 9, 0, 13, 8 ]
 list1.sort()
 
 print (funReceives ())


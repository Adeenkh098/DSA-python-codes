def binarysearch (numbers , key ):
   numbers.sort()
   l = 0
   r = len(numbers )-1
   while (l <= r ):
      mid = (l+r) // 2
      if(numbers [mid]==key):
         print(" %d  found at index %d "% (key , mid ) )
         return
      elif(numbers [mid]<key):
         l= mid+1

      elif(numbers [mid]>key):
         r = mid -1
   print ("ELEMENT NOT FOUND ")
      
      
def linearsearch (numbers, key ):
   for i in range(len(numbers)):
      if numbers[i]==key:
         print("%d KEY FOUND AT INDEX %d "%(key,i))
         return
   print("Element not found")
      
z= True
while(z):
   print ( "\t<  MANUAL  >  \t ")
   manual_input = int (input ("\tENTER 1 FOR BINARY SEARCH \n"
                              "\tENTER 2 FOR LINERAR SEARCH\n"
                              "\tENTER 3 FOR EXIT\n"))
   if(manual_input==3):
      print("EXITING THE PROGRAM ><")
      break
   
   
   print("CREATING A LIST ")
   list = []
   n = (int(input("ENTER THE NO OF ELEMENTS U WANT TO ADD IN THE LIST :")))
   for i in range (n):
      ele = int(input("ENTER THE ELEMENT : "))
      list .append(ele)
   user_key = int(input ("ENTER THE ELEMENT  THAT U WANT TO FIND "))
   

   if(manual_input == 1 ):
      binarysearch(list, user_key )

   if(manual_input==2 ):
       linearsearch(list,user_key )
      
         

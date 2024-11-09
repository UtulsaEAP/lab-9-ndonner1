# Noah Donnermeyer
# Th 8am

def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   

   return (user_val2,user_val1,user_val4,user_val3)

if __name__ == '__main__':   
   user_input1 = str(int(input()))
   user_input2 = str(int(input()))
   user_input3 = str(int(input()))
   user_input4 = str(int(input()))
   #store output for every input here
   swap_values(user_input1, user_input2, user_input3, user_input4)
   #print those output
   print(swap_values(user_input1, user_input2, user_input3, user_input4))

 
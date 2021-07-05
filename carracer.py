import randit from random 
def get_int_input(message, error ,low,high):
    while true:
        try:
            inpt=int(input(message))
            
            if low <inpt < high:
                return inpt 
            else: 
                print(error)
        except ValueError:
            print(error)

        
car_choice= get_int_input("choose a car \n', 'please enter number between 1 to 6,"  0,7') 

race_distance=get_int_input("choose a race distance\n" , "Please enter a number between 5 and 15 ", 4,15)

cars=[0,0,0,0,0,0]

for i,cars in enumerate(cars):
    print('_'*car )
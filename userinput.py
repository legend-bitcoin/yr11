def get_integer_input(message,error,low,high):
    while true:
        try:
            inpt =int(input(message))
            if low<inpt<high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)

lmao= get_integer_input
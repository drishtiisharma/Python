color = input()
match color:
    case 'green':
        print ('gooo')
    case 'yellow':
        print('waitttt')
    case 'red':
        print('stoppp')
    case _:
        print("can only choose between : green,yellow,red")
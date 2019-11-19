def collatz(number = 4):
    
    value = None

    if not number % 2:
        value = number//2
    else:
        value = (number * 3) + 1
    
    print(value)
    return value


end_of_collatz = False
print('Input a number')
number = int(input())

while end_of_collatz == False:
    number = collatz(number)
    if number == 1:
        end_of_collatz = True

    
 
def comma_code(input_list):
    
    input_string = ''

    for x in range(0,(len(input_list)-1)):

        input_string = input_string + input_list[x] + ', '
    
    input_string = input_string + 'and ' + input_list[-1]
    
    return input_string

def print_transverse_grid():
    
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

    for y in range(0,len(grid)):
        for x in range(0,len(grid[0])):
            print(grid[x][y], end='')

        print('\n')


def displayInventory(inventory):

    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (str(k) + ' ' + str(v))
        item_total += v

    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):

    print("Inventory:")

    for k in addedItems:
        if k in inventory.keys():
            inventory[k] += 1
        else:
            inventory.setdefault(k, 1)

    item_total = 0
    for k, v in inventory.items():
        print (str(k) + ' ' + str(v))
        item_total += v

    print("Total number of items: " + str(item_total))
    

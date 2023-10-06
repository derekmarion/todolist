def main():
    todo_list = ['Squash Beef', 'Ascend']
    user_input = display_menu()
    tries = 0
    while user_input != {1,2,3,4} or tries > 3:
        user_input = input('Invalid input. Try again.')

    while user_input != '4':
        
        if user_input == '1':
            display_list(todo_list)
        elif user_input == '2':
            todo_list = add_item(todo_list)
        elif user_input == '3':
            remove_item(todo_list)
    
        user_input = display_menu()
    
    return print('Program Exited.')
    
def display_menu():
    return input('\n1: Show To-Do List\n2: Add Item\n3. Remove Item\n4. Quit\n\nEnter selection: ')

def display_list(todo_list):
    i = 1
    for items in todo_list:
        print(f'{i}: {items}')
        i += 1

def add_item(todo_list):
    item_to_add = input('Task to add: ')
    return todo_list.append(item_to_add)

def remove_item(todo_list):
    item_to_remove = input('Task to remove (enter number): ')
    return todo_list.pop(int(item_to_remove))

main()
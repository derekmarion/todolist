def main():
    todo_list = ['Squash Beef', 'Ascend']
    user_input = display_menu(todo_list)

    if user_input == '1':
        display_items()
    elif user_input == '2':
        add_item(todo_list)
    elif user_input == '3':
        remove_item(todo_list)
    return

def display_menu():
    print('1: Show To-Do List\n2: Add Item\n3. Remove Item\n4. Quit ')

def display_items(todo_list):
    i = 0
    for items in todo_list:
        print(f'{i+1}: {items}')
    return input('Enter Menu Choice: ')

def add_item(todo_list):
    item_to_add = input('Task to add: ')
    return todo_list.append(item_to_add)

def remove_item(todo_list):
    item_to_remove = input('Task to remove (enter number): ')
    return todo_list.pop(int(item_to_remove))
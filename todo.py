from app import TodoList
import sys
def main():
    count = 0
    list_args = sys.argv
    list_output = list()

    if 'create' in list_args:
        for args in list_args:
            if count>=2:
                print(TodoList().create_todo_list(description=args))
            count = count + 1
            
    elif "list-all" in list_args:
        if len(list_args)==2:
            print(TodoList().read_todo_list())
        elif len(list_args)>3:
            if '--' in list_args[2]:
                print(TodoList().read_todo_list(command=list_args[2],substring=list_args[3]))
            else:
                print('select a valid command')    
        else:
            print('select a valid command')
    
    elif "update" in list_args:
        for args in list_args:
            if count>=2:
                print(TodoList().update_state('--substring',args))
            count = count+1    
    elif "toggle" in list_args:
        if len(list_args)>3:            
            print(TodoList().update_state('--substring',list_args[2],substr2=list_args[3]))
        else:
            print('select a valid command')
    elif "delete" in list_args:
        if len(list_args)==2:
            print(TodoList().delete_todo('all',''))
        elif len(list_args)>=3:
            for args in list_args:
                if count>=2:
                    print(TodoList().delete_todo('--substring',args))
                count = count + 1
        else:
            print('select a valid command')
    else:
        print("select a valid command, refer to the documents")

        
if __name__ == '__main__':
    main()
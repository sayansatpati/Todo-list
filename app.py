import uuid, json, os

class TodoList:

        
    def create_todo_list(self, description = '',todo_dict = dict()):
        """

        :param description:
        :param todo_dict:
        :return:
        """
        try:        
            json_obj = {'todo':[]}
            if todo_dict is None or todo_dict == {}:            
                todo_dict = {'id':str(uuid.uuid1()),'description':description,'state':'incomplete'}            
            filename = 'datafile'
            
            if os.path.isfile(filename) and self.read_todo_list() is not None:
                
                json_obj = self.read_todo_list()
            
            
            json_obj.setdefault('todo', []).append(todo_dict)
            with open(filename, 'w') as outfile:            
                json.dump(json_obj, outfile)
            return description + ' successfully added to the list'
        except Exception as e:
            return 'Failed to add to todo list due to exception ' + e


    def read_todo_list(self, command='all',substring=''):    
        with open('datafile','r') as json_file:
            if command == 'all':
                data = json.load(json_file)
                if data:
                    return data
                else:
                    return None
            
            elif command=='--substring':
                list_output = list()
                data = json.load(json_file)
                for keys, values in data.items():
                    for row in values:
                        if substring in row['description']:
                            list_output.append(row)
                return list_output


            elif command == '--no-complete':
                list_output = list()
                data = json.load(json_file)
                for keys, values in data.items():
                    for row in values:
                        if substring in row['description'] and row['state']=='incomplete':
                            list_output.append(row)
                return list_output
                
            elif command == '--complete':
                list_output = list()
                data = json.load(json_file)
                for keys, values in data.items():
                    for row in values:
                        if substring in row['description'] and row['state']=='completed':
                            list_output.append(row)
                return list_output
            
            else:
                return 'select a valid command'
            


    def update_state(self,command, substr1, substr2=''):
        data = self.read_todo_list(command=command, substring=substr1)
        self.delete_todo(command=command, substring=substr1)
        
        if substr2:
            
            for row in data:
                row['description']=substr2
                self.create_todo_list(description='',todo_dict=row)
            return 'successfully updated description'
        else:
            for row in data:
                if row['state'] == 'completed':
                    row['state']= 'incomplete'
                else:
                    row['state']= 'completed'
                self.create_todo_list(description='',todo_dict=row)
            return data


    def delete_todo(self,command, substring):
        filename = 'datafile'
        if command=='all':
            with open(filename, 'w') as outfile:
                json.dump(None, outfile)
            return 'successfully deleted all'
        else:
            data_del = self.read_todo_list(command=command, substring=substring)    
            data_all = self.read_todo_list()
            
            for row in data_del:
                for key, value in data_all.items():
                    value.remove(row)
            with open(filename, 'w') as outfile:            
                json.dump(data_all, outfile)
            return substring + ' successfully deleted from the list'

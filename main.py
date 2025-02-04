import argparse
from datetime import datetime
import os
import json

FILE_NAME = 'tasks.json'



def load_tasks():
    path = os.path.exists(FILE_NAME) 
    if path:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME,'w') as file:
        json.dump(tasks, file , indent=4)

def add_task(description):
    tasks = load_tasks()
    max_id = max([task['id'] for task in tasks], default=0)
    task_id = max_id + 1
    new_task = {
        'id': task_id,
        'description' : description,
        'status': 'todo',
        'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'\n!!! task {description} was successfully added !!!\n')

def delete_task(id):
    tasks = load_tasks()
    new_tasks_list = [task for task in tasks if task['id'] != id]
    if len(tasks) == len(new_tasks_list):
        print(f'\n!!! Task with id: {id} is not found !!!\n')
        return
    else:
        print(f'\n!!! Task with id: {id} is was deleted !!!\n')
    save_tasks(new_tasks_list)

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    print("\n{:<4}  {:<25}  {:<10}  {:<16}  {:<16}".format("ID", "DESCRIPTION", "STATUS", "CREATED", "UPDATED"))
    print("-" * 79)  # Разделительная линия
    
    if not tasks:
        return print('\n!!! task list is empty !!!\n')
    
    for task in tasks:
        desc = task['description'][:22] + '...' if len(task['description']) > 25 else task['description']
        print("{:<4}  {:<25}  {:<10}  {:<16}  {:<16}".format(task['id'], desc, task['status'], task['createdAt'], task['updatedAt']))
    print('\n')
    


def update_task(id_task, description):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == id_task), None)
    status = ['done','todo','in-progress']
    if task:

        if not description in status and description:
            if not len(description) > 2:
                print('\n!!! Length must exceed 2 symbols !!!\n')
            else:
                task['description'] = description
                print('\n!!! Description changed successfully !!!\n')
        else:
            task['status'] = description
            print('\n!!! Status changed successfully !!!\n')
        task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M')
        save_tasks(tasks)
        
    else:
        print(f'\n!!! not found task with id: {id_task} !!!\n')
        return


def main():
    parse = argparse.ArgumentParser(description='Task tracker cli')
    parse.add_argument('command',choices=['add','delete','update','list'],help='choose a command')
    parse.add_argument('args', nargs='*',help='additional arguments')
    args = parse.parse_args()

    if args.command == 'list':
        status = ['done', 'todo', 'in-progress']
        if args.args:

            if args.args[0] in status:
                list_tasks(args.args[0])
            
            else:
                print('\n!!! There are no tasks with this status !!!\n')
            
        else:
            list_tasks()
    
    if args.command == 'add':
        if len(args.args[0]) > 2:
            add_task(' '.join(args.args))
        else:
            print('\n!!! Length must exceed 2 symbols !!!\n')
    
    if args.command == 'delete':
        if not args.args:
            print('\n!!! You must input id task !!!\n')
        elif not args.args[0].isdigit():
           print('\n!!! You must input a digit !!!\n')
        else:
            delete_task(int(args.args[0]))

    if args.command == 'update':
        if args.args:
            update_task(int(args.args[0]), ' '.join(args.args[1:]))
            if len(args.args) <= 1:
                print('\n!!! you should have provided an ID and a new description or status !!!\n')
        else:
            print('\n!!! you should have provided an ID and a new description or status !!!\n')


if __name__ == '__main__':
    main()
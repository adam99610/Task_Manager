class TaskManager:
    def __init__(self):
        # Starts the program and makes a list that stores tasks.
        self.tasks = []
    
    def add_task(self, title, detail, due_date):
        """
        Add a new task to the list

        Parameters:
        - title (str): Title of the task.
        - detail (str): More Detail about the task.
        - due_date(str): Due date of the task

        Returns:
        None
        """
        # Creates a Dictionary that shows the task and appends it to the tasks list
        task = {'title': title, 'detail': detail, 'due_date': due_date}
        self.tasks.append(task)
        print(f'Task "{title}" added.')

    def task_list(self):
        """
        Displays all current tasks in the task list, this includes the due dates, titles, and details.
        This will provide a menu for further actions - return to the main menu opr quit the program.
        """
        if not self.tasks:
            print('No tasks are found')
        else:
            #This shows details of each task in the task list.
            print('Tasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. Due Date: {task["due_date"]}, Title: {task["title"]}, Detail: {task["detail"]}')     

            # this shows a simple sub-menu for more actions after listing the tasks        
            print('\nTask List Menu:')
            print('1. Main Menu')
            print('2. Quit')

            sub_choice = input('Enter your choice (1-2): ')
            if sub_choice == '1':
                return
            elif sub_choice == '2':
                print('Exiting Task Manager. Goodbye!')
                exit()
            else:
                print('Invalid choice. Returning to Main Menu')

                
    def find_task(self, title_to_find):
        """
        Find and display details about the task and the title that comes with it.

        Parameters:
        - title_to_find (str): is the title of the task to search for.

        Returns:
        None
        """
        # Search for a task with the title that matches it.
        found_task = next((task for task in self.tasks if task['title'].lower() == title_to_find.lower()), None)
        if found_task:
            print(f'Task found: ')
            print(f'Due Date: {found_task["due_date"]}, Title: {found_task["title"]}, Detail: {found_task["detail"]}')
        else:
            print(f'No task that was found of the title "{title_to_find}".')
def main():
    # This creates an instance of the class callled TaskManager
    task_manager = TaskManager()

    while True:
        # Displays the main menu that the user  has for interaction
        print('\nMain Menu:')
        print('1. Add Task')
        print('2. List All Tasks')
        print('3. Find Task')
        print('4. Quit')

        #Get an input from the user
        choice = input('Please enter your choice (1-4): ')

        #Process the users choice and executes the action that the user has selected
        if choice == '1':
            title = input('Please enter the task name: ')
            detail = input('Please enter details of the task: ')
            due_date = input('Please enter the date for the task: ')
            task_manager.add_task(title, detail, due_date)
        elif choice == '2':
            task_manager.task_list()
        elif choice == '3':
            title_to_find = input('Please enter the task you want to find: ')
            task_manager.find_task(title_to_find)
        elif choice == '4':
            print('Exiting the Task Manager. Goodbye!')
            break
        else:
            print('You have imput an invalid choice. please select a number between 1 and 4')
if __name__ == '__main__':
    main()
'''Create a command-line application that allows users to manage their tasks effectively by adding, viewing, and removing items from a to-do list.'''
tasks = []																						# initializes a list called tasks
while True:																						# a simple while True loop
	user_input = input("Do you want to add task, view tasks, or remove a task: ").lower()		# asks the user for input about 

	if user_input == "add task":																# if the user wants to add task then this branch of the if-else statment activates
		new_task = input("new task: ")															# asks the user what the new task they want to add to the to-do list is
		tasks.append(new_task)																	# adds the users new task to the tasks list
		print(f"Task '{new_task}' added successfully!")											# prints a message to the user that tells them the task they just added was successfully added
		
	elif user_input == "remove task":															# if the user wants would rather remove task then this branch of the if-else statment activates
		if tasks:																				# checks that tasks is a non-empty list
			removed_task = input("Enter task to remove: ")										# asks the user which task they want to remove
			if removed_task in tasks:															# checks if the task is in the list called tasks
				tasks.remove(removed_task)														# removes the task from the list that the person wants removed
				print(f"Task '{removed_task}' removed successfully!")							# prints a message to the user that tells them the task they just attempted to remove was successfully removed
			else:																				# if the task is not in the list called tasks
				print("No tasks to remove. The list is empty.")									# The message: No tasks to remove. The list is empty. is printed out
				
	elif user_input == "view tasks":															# if the user wants to view tasks then this branch of the if-else statement is ativated
		if tasks:																				# checks that tasks is a non-empty list
			print("Your tasks:")																# prints the message: your tasks:
			for index, task in enumerate(tasks, start=1):										#
				print(f"{index}. {task}")														#
		else:																					# if tasks is an empty list
			print("No tasks in the list.")														# prints the message that no tasks in the list
		

	else:																						# if the user types anything besides the commands then this is ativated
		print ("Goodbye!")																		# prints the message Goodbye!
		break																					# ends the while loop and exits the program
		

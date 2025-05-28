while True:
  task = input("Enter your task: ")
  Priority = input("Priority (high/medium/low): ")
  time_bound = input("Is it time-bound? (yes/no): ")
  match Priority:
    case "high":
      if time_bound == "yes":
        print(f"Reminder: '{task}' is a {Priority} priority task that requires immediate attention today!")
      else:
        print(f"Reminder: '{task}' is a {Priority} priority task that requires attention in the upcoming days!")
      break
    case "medium":
      if time_bound == "yes":
        print(f"Reminder: '{task}' is a {Priority} priority task that requires attention today!")
      else:
        print(f"Reminder: '{task}' is a {Priority} priority task that requires attention in the upcoming days!")
      break
    case "low":
      if time_bound == "yes":
        print(f"Reminder: '{task}' is a {Priority} priority task that requires attention if you have free time!")
      else:
        print(f"Reminder: '{task}' is a {Priority} priority task that requires no attention!")
      break
    case _:
      print("Invalid priority entered. Please enter high, medium, or low.")
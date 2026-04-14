# Threading:
#     Threading is a technique that allows a program to run multiple operations concurrently (in parallel) 
#     within the same process.

# import time

# def walk_dog():
#     time.sleep(8) #time.sleep() is a function in Python's time module that pauses the execution of your program for a specified number of seconds.
#     print("You finish walking the dog")

# def take_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# walk_dog()
# take_trash()
# get_mail()

#in the above code, it is using the single thread(Tasks run one after another) 
# like when executing the function it takes 8 sec to execute the walk_dog() function 
# then waits 2 sec to execute the take_trash() function 
# and only after 4 sec executes the get_mail() function like it will run parallely



#########So to run the tasks concurrently we use threads
# import time
# import threading

# def walk_dog():
#     time.sleep(8) 
#     print("You finish walking the dog")

# def take_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# thread1 = threading.Thread(target=walk_dog)
# thread2 = threading.Thread(target=take_trash)
# thread3 = threading.Thread(target=get_mail)

# thread1.start()
# thread2.start()
# thread3.start()

# print("All chores are complete")

# NOTE:print("All chores are complete") this executes right after running while the chores are still not complete

# Terminologies:
# What threading.Thread(target=function_name) Means:
#     This creates thread objects that are configured to run specific functions, but doesn't start them yet.

# The target Parameter:
#     target tells the thread which function to execute when started
#     You pass the function name without parentheses ()
#     Think of it as "I want this thread to run fast_task when you start it"

# Why No Parentheses?:
#     # CORRECT - Pass the function itself
#     thread = threading.Thread(target=fast_task)  # fast_task without ()

#     # WRONG - This would RUN the function immediately
#     thread = threading.Thread(target=fast_task())  # Would execute fast_task() right now!



###############
# import time
# import threading

# def walk_dog():
#     time.sleep(8) 
#     print("You finish walking the dog")

# def take_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# thread1 = threading.Thread(target=walk_dog)
# thread2 = threading.Thread(target=take_trash)
# thread3 = threading.Thread(target=get_mail)

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

# print("All chores are complete")

#now the above code executes concurrently,but when you want your program(print("All chores are complete")) to wait but still do the task concurrently,you could use join()



###########Lets say your function takes argument
# import time
# import threading

# def walk_dog(name):
#     time.sleep(8) 
#     print(f"You finish walking {name}")

# def take_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# thread1 = threading.Thread(target=walk_dog, args=("Shepherd",)) #NOTE: when sending argument,se send as tuple and if there is only one argument we end with comma(,)
# thread2 = threading.Thread(target=take_trash)
# thread3 = threading.Thread(target=get_mail)

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

# print("All chores are complete")


##############While sending two arguments
# import time
# import threading

# def walk_dog(first_name,last_name):
#     time.sleep(8) 
#     print(f"You finish walking {first_name} {last_name}")

# def take_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# thread1 = threading.Thread(target=walk_dog, args=("German","Shepherd")) #NOTE: while sending two arguments,you don't have to end with comma(,)
# thread2 = threading.Thread(target=take_trash)
# thread3 = threading.Thread(target=get_mail)

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

# print("All chores are complete")


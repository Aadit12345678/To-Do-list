#Making of the to-do list.
list=[]

print("Hello... Welcome to the to-do list...")
print("Lets start... :)")
i=int(input("Enter the number of tasks you want to add: "))
if i=="0":
    exit()

def main(i):
    tasks=input("Enter the task name: ")
    list.append(tasks)
    print(list)

for u in range(i):
    main(i)
    if u==i:
        print(list)
#List complete.

#removing tasks from list.
print("Now, as the list has been made, you can type the task number to remove it from the list... It will be marked as done...")
print("You can check the task numbers in the list which is printed after you delete each task... Please note that the task number will change each time with the new list...")

def delete():
    n=int(input("Enter the task number of the task to be deleted: "))
    list.pop(n-1)
    print(list)

for x in range(i):
    delete()
#Deleting function done.
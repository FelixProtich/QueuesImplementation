queue = []

def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "is added to the queue")
    print()

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print(e, "is removed from the queue")
        print()

def display():
    print(queue)

while True:
    print("Operations \n 1.Add \n 2.Delete \n 3.Show \n 4.Quit")
    Choice = int(input())

    if Choice == 1:
        enqueue()
    elif Choice == 2:
        dequeue()
    elif Choice == 3:
        display()
    elif Choice == 4:
        break
    else:
        print("Enter the the correct operation")
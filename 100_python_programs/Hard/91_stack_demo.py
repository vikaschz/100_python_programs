"""
Program: stack demo
Description: perform stack operations(push, pop, display)

"""

stack = []
stack_size = int(input("Enter stack size: "))


def push():
    if len(stack) < stack_size:
        elem = input("Enter an element to be pushed: ")
        stack.append(elem)
    else:
        print("----Stack Overflow----")


def pop():
    if len(stack) == 0:
        print("----Stack Underflow----")

    else:
        print(f"The element popped from stack is: {stack.pop()} ")


def display():
    if len(stack) == 0:
        print("----Stack is empty----")
    else:
        print("----Stack Contents----")
        print("Top ->")
        for n in reversed(stack):
            print(f"|{n}|")
        print("<- Bottom")


cur = True
while cur:
    print("----Menu----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()

    elif choice == "2":
        pop()
    elif choice == "3":
        display()

    elif choice == "4":
        print("Exiting program...")
        cur = False

    else:
        print("Enter valid choice(1,2,3,4).")

import random
def run():
    answer = random.randint(1,100)
    user = int(input("Enter Random Number:"))
    if user == answer:
        print("True")
    else:
        print("False")
    while user != "end":
        answer = random.randint(1,100)
        user = int(input("Enter Random Number:"))
        if user == answer:
            print("True")
        else:
            print("False")
run()
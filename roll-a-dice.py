import random
response = "y"

while response == "y":
    x = random.randint(1,6)

    if x == 1:
        print("[     ]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[     ]")
    elif x == 2:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif x == 3:
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
    elif x == 4:
        print("[ 0 0 ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[ 0 0 ]")
    elif x == 5:
        print("[ 0 0 ]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[ 0 0 ]")
    elif x == 6:
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")

    response = input(str("Enter 'y' or 'n'"))
    print("\n")
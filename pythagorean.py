# define start
def start():
    # list what you wrote in the quotation marks.
    print "Choose two sides to enter."
    print "Don't forget that C is the hypotenuse!"
    print "You can choose 1)AB 2)BC 3)AC"
    print "Type in the number."
    # the user can type the choices in
    choice = raw_input("> ")

    # These commands list all the possibilities the user can use.
    if choice == "1":
        AB()
    elif choice == "2":
        BC()
    elif choice == "3":
        AC()
    else:
        print "type 1, 2, or 3"


# define AB
def AB():
    # float is the number form of raw_input
    # so the user can type numbers instead of letters
    A = float(raw_input("What is the length of A?\n> "))
    B = float(raw_input("What is the length of B?\n> "))
    # Define what C_squared is
    C_squared = A**2 + B**2
    # Define what C is
    C = C_squared**0.5
    # shows the answer
    print "The length of the hypotenuse is %r" % C
    # After all commands, the user goes out of the program automatically
    exit(0)


# define BC
def BC():
    # float is the number form of raw_input
    # so the user can type numbers instead of letters
    B = float(raw_input("What is the length of B?\n> "))
    C = float(raw_input("What is the length of C?\n> "))
    # Define what A_squared is
    A_squared = C**2 - B**2
    # Define what A is
    A = A_squared**0.5
    # shows the answer
    print "The length of the A is %r" % A
    # After all commands, the user goes out of the program automatically
    exit(0)


# define AC
def AC():
    # float is the number form of raw_input
    # so the user can type numbers instead of letters
    A = float(raw_input("What is the length of A?\n> "))
    C = float(raw_input("What is the length of C?\n> "))
    # Define what B_squared is
    B_squared = C**2 - A**2
    # Define what B is
    B = B_squared**0.5
    # shows the answer
    print "The length of the B is %r" % B
    # After all commands, the user goes out of the program automatically
    exit(0)

# It makes the start as the starting point of the whole program
start()

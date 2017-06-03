name = input("What's your name? ")
while name == '':
    name = input("Don't be shy, just say your name? ")
while True:
    try:
        age = int(input("And your age? "))
        break
    except ValueError:
        print("Age is a number ")
username = input("This is uncomfortable, but may I know your reddit username? ")
while username == '':
    username = input("Come on! just for fun, give your reddit user name! ")
print("Hey, so your name is %s, you are %d years old and your reddit username is %s" % (name, int(age), username))


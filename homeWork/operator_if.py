a = int(input("insert 1st number: "))
b = int(input("insert 2nd number: "))
c = int(input("insert 3d number: "))
if a > b:
    print("Свершилось!")
elif b > a:
    print("Да ну!")
elif a == b:
    print("А если так?")
    a = a + c
    b = b - c
    if a > b:
        print("no way!")
    else:
        print("yeah!")
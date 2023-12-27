str1 = input()
str2 = input()

if len(str1) != len(str2):
    print("N")

else:
    for i in range(len(str1)):
        if str2[i] in str1:
            str2, str1 = str2.replace(str2[i], " ", 1), str1.replace(str2[i], " ", 1)

    for i in str2:
        if i == " ":
            continue
        if i != "*":
            print("N")
            break
    else:
        print("A")

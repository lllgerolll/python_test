

with open("Test.txt","r") as file:
    lins = file.readlines()

    for i in lins:
        print(i)

try:
    file = open("T2st.txt","r")
    for i in lins:
        print(i)
    file.close()
except ValueError:
    print (ValueError)
except Exception:
    print ("eto govnishe",ValueError)


import os


labelList = []

def main():
    labelList.clear()
    print("Please enter the location:")
    location = input().upper()
    os.system('clear')


    

    print("Enter the shelf range.")
    shelfStart = int(input("Enter the shelf starting number:"))
    shelfEnd = int(input("Enter the shelf ending number:"))
    shelfEnd += 1
    os.system('clear')

   

    print("Enter the Row range.")
    w = int(input("Starting Row:"))
    x = int(input("Ending Row:"))
    x += 1
    os.system('clear')


   

    print("Enter the Column range.")
    y = int(input("Starting Column:"))
    z = int(input("Ending Column:"))
    z += 1
    os.system('clear')


    

    for a in range(shelfStart,shelfEnd):
        a = str(a).zfill(2)
        
        for b in range(w,x):
            b = str(b).zfill(2)

            for c in range(y,z):
                c = str(c).zfill(2)
                string = location+'-'+a+'-'+b+'-'+c
                labelList.append(string)
     

    csv()

def csv():
    textfile = open("Label.txt", "w")
    for elemenet in labelList:
        textfile.write(elemenet + "\n")
    textfile.close()


main()

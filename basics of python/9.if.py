num = int(input("Enter number = "))
if (int(num) >= 40 and int(num) <= 60):
    print("You have pass the exam Average")
elif(int(num) > 60 and int(num) <= 70):
    print("You have pass the exam Distintion")
elif(int(num) > 70 and int(num) <= 80):
    print("You have pass the exam Top - 20")
elif(int(num) > 80 and int(num) <= 90):
    print("You have pass the exam Top - 10")
elif(int(num) > 90 and int(num) <= 100):
    print("You have pass the exam Top - 5")
else:
    print("You are failed ",num)
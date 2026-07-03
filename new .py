# නමෝ බුද්දාය
quiz = input("ඔටෝබොට්ස්ලා ගෙ නායකයා කවුද?").lower()
while quiz.strip() == "" or quiz != "optimus prime":
    if quiz.strip() == "":
        print("plz answer do not empty")
        quiz = input("ඔටෝබොට්ස්ලා ගෙ නායකයා කවුද?").lower()
    elif quiz != "optimus prime":
        print(f"No, {quiz} is not the autoboot leader")
        quiz = input("ඔටෝබොට්ස්ලා ගෙ නායකයා කවුද?").lower()
if quiz == "optimus prime":
    print(f"yes, {quiz} is leder of autobots")

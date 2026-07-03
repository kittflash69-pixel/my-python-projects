# නමෝ බුද්දාය
x = input("වයස කීයද?:")
while x.strip() == "":
    print = ("වයස දෙන්න බ්‍රො හිස්තැනක් තියන්න බෑ")
    x = input("වයස කීයද?:")
while not x.isdigit():
    print("අංක විතරයි බ්‍රො")
    x = input("වයස කීයද?:")
print(f"ඔකෙ ඔයාගෙ වයස {x} නේද මරු")

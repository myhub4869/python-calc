def main():
  while True:
    print("--------------------")
    print("function calc menues")
    print("1: add")
    print("2: minus")
    print("9: exit")
    print("--------------------")

    menu_key = int(input("Enter Input menu number >> "))

    if menu_key == 1 :
      val1 = int(input("1st Number >> "))
      val2 = int(input("2nd Number >> "))
      print("%d + %d = %d" % ( val1,val2,val1+val2 ))

    elif menu_key == 2 :
      val1 = int(input("1st Number >> "))
      val2 = int(input("2nd Number >> "))
      print("%d - %d = %d" % ( val1,val2,val1-val2 ))

    elif menu_key == 9 :
      break

if __name__ == "__main__":
    main()

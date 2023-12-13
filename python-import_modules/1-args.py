listOfItems = ["Hello","Holberton","School",98,"Battery","street"]
lengthy = len(listOfItems)
if __name__ == "__main__":
    if lengthy == 0:
        print("{} arguments".format(lengthy))
    elif lengthy == 1:
      print("{} argument".format(lengthy))
      print("{}: {} ".format(lengthy,listOfItems[1] ))
    else :
       print("{} arguments".format(lengthy))
       for i in range(lengthy):
         print("{}: {} ".format(i+1,listOfItems[i] ))
    
       
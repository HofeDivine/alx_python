from sys import argv

lengthy = len(argv)-1
if __name__ == "__main__":
    if lengthy == 0:
        print("{} arguments.".format(lengthy))
    elif lengthy == 1:
      print("{} argument:".format(lengthy))
      print("{}: {} ".format(lengthy,argv[1] ))
    else :
       print("{} arguments:".format(lengthy))
       for i in range(lengthy):
         print("{}: {} ".format(i+1,argv[i+1] ))
    
       
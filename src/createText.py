def createText(numbers, names):
    message = ""
    for index in range(len(numbers)):
      message = message + "値上がり率"+str(index+1)+"位：　"+numbers[index]+"　 "+names[index]+"\n"
    return message
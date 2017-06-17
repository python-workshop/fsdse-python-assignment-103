def compress(inputString):
    """ To compress the string in terms only if its saving the space"""
    compressedString = ""
    count = 1
    secondChar = ""
    if(inputString != None and inputString != ""):
        compressedString += inputString[:1]
        #print compressedString

        for i in range(len(inputString)-1):
            if(inputString[i] == inputString[i+1]):
                count += 1
            else:
                if(count > 1):
                    compressedString += str(count)

                compressedString += inputString[i+1]
                count = 1

        if (count > 1 ):
            compressedString += str(count)

    elif(inputString == None):
        compressedString = None
        return compressedString
    elif(inputString == ""):
        compressedString = ""
        return compressedString

    if(len(compressedString) == len(inputString)):
        return inputString
    else:
        print compressedString
        return compressedString


compress("AAAABBCCCC")

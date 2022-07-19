


def main():
    def RunLengthEncoding(inputString = str()):
        """
        Encodes strings of characters into compressed strings following format "4a2b3c..."
        
        Parameters: 
            inputString (str): string of characters to be compressed

        Returns:
            outputString (str): string of compressed characters

        """
        outputString = ''
        isCompressed = False
        i = 0
        j = 1
        k = 1
        while isCompressed == False:
            # print('i ' + str(i))
            # print('j ' +  str(j))
            if inputString[i].isalpha() and inputString[j - 1].isalpha():
                if ((i <= len(inputString) - 1) and (j <= len(inputString) - 1)):
                    if inputString[i] == inputString[j]:
                        k += 1
                        j += 1
                    else:
                        outputString += f'{k}{inputString[i]}'
                        k = 0
                        i = j
                        j = i
                elif i <= len(inputString) - 1 and j > len(inputString) - 1:
                    outputString += f'{k}{inputString[i]}'
                    k = 0
                    j = 1
                    isCompressed = True
                    
                else:
                    isCompressed = True
            else:
                outputString = "ERROR, UNEXPECTED TYPE"
                isCompressed = True
                



        return outputString

    testArray = [[0,1,1,0,0],[0,1,0,0,0],[1,0,0,0,1]]
    def validateRobotPositions(arrayInput = list()):
        robotIndicesTimeSeries = []
        for i in range(0,len(arrayInput)):
            robotIndicesSingleArray = []
            for j in range(0,len(arrayInput[i])):
                if arrayInput[i][j] == 1:
                    robotIndicesSingleArray += [j]
            robotIndicesTimeSeries += [robotIndicesSingleArray]
        
        for j in range(0,len(robotIndicesTimeSeries[0])):
            for i in range(1,len(robotIndicesTimeSeries)):
                if abs(robotIndicesTimeSeries[i][j] - robotIndicesTimeSeries[i - 1][j]) > 1:
                    return "Movement Not Possible"
        
        return "Movement Possible"
                    
            
                    


    print(validateRobotPositions(testArray))

    validateRobotPositions(testArray)



if __name__ == '__main__':
    main()
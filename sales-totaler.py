#This program will take sales numbers from a txt file written as dollars
#     sum the numbers across rows, and output the rows with the sum at the end
#     in an output txt file.

def main():
    print("This program will take sales information and save its sums in a new file!\n")
    
    #get the file name from user
    inputFileName = input("Enter the name of your file? ")
    outputFileName = input("What is the file name for the new sales totals? ")
    
    #open the files
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')
    
    #input file -- process the lines and split
    for line in inputFile.readlines():
        num1, num2 = line.split()
        #$values are converted to floats
        num1, num2 = float(num1[1:]), float(num2[1:])
        #add the two values, turn back to string, store total
        totals = str(num1 + num2)
        #format
        newSales = " ${0:>8}".format(num1) + " ${0:>8}".format(num2) + " ${0:>8}\n".format(totals)
        
        outputFile.write(newSales)
        
    #close both files
    inputFile.close()
    outputFile.close()
    
    print("\nSUCCESS! Totals have been written and saved to", outputFileName)
        

main()
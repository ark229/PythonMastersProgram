# A program that finds sales info based on:
#       invoice id
#       customer last name
# Goals:
#   make the file searchable
#   prompt user to input the following:
#       1. whether they want to search by id or last name (lname)
#              Reject any input that isn't id or last name (lname)
#       2. Search term -- either 'id' value or an 'lname' value
#   Program should open the date file, search w/in columns, and if a match is found
#       print (not save) all matching invoices.
#   Finally, should print total number of records found that matched the search

print("Welcome! This program will find sales information based on invoice id and", \
      "customer last name!")
input("Press <ENTER> to continue!\n")


def main():
    with open('sales_data.csv', 'r') as readFile:
        columns = readFile.read()
        columns = columns.split('\n')
        #empty lines from csv file removal
        if "" in columns:
            columns.remove("")
            
    userChoice = input("Would you like to search by invoice id or last name? Please type either 'id' or 'lastName': ")
    
    #while loop for userChoice to make sure only id and lastName is entered
    while userChoice not in ['id', 'lastName']:
        print("USER INPUT ERROR! Please enter only 'id' for customer id or 'lastName' for customer last name: ")
        userChoice = input("Would you like to search by invoice id or last name? Please type either 'id' or 'lastName': ")
    
    #search loop
    search = input("Please enter your search criteria: ")
    count = 0
    if userChoice == "id":
        for column in columns:
            if column.split(",")[0] == search:
                count = count + 1
                print(column)
        print("\n{} record(s) located!".format(count))
    else:
        for column in columns:
            if column.split(",")[2] == search:
                count = count + 1
                print(column)
        print("\n{} record(s) located!".format(count))
    
        
#call main
if __name__ == "__main__":
    main()
              
              
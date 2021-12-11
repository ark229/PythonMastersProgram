#mad lib game
#user input noun, past tense verb, place

#mother goose old woman in a shoe nursery rhyme mad-libber

def poam():
    name = input("Enter any name: ")
    userPlace = input("Enter any place (school, venue, city, etc.): ")
    userObject = input("Enter the name of any object: ")
    action = input("Enter any action verb: ")
    actionTwo = input("Enter another action verb: ")
    
    print("\nThere was an old", name, "who lived in a", userPlace,".")
    print(name, "had so many", userObject, name, "didn't know what to do.")
    print(name, action,  "them some broth without any bread." "\nAnd", actionTwo, "them all soundly and", action, "them to bed.")  
    
    
def main():
    poam()
    print()
    
main()
    
    
    
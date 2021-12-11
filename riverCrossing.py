#Module 7 Assignment -- crossing the river
#Find a series of crossings that will get everyone safely to the other side of the river
#If the cannibals outnumber the missionaries on either bank, the missionaries will be eaten


# TO START: 3 Cannibals (can) and 3 Missionaries (miss) are on edge 1 of the River
edge1 = {'can': 3, 'miss': 3}    #3 cannibals &  3 miss on edge 1 at start of program
edge2 = {'can': 0, 'miss':0}     # 0 canniblas & 0 missionaries on edge 2 of the other side at start
boat = {'can': 0, 'miss': 0}      #0 people in boat at start of program


#format solution for problem
def print_graph(dict1, dict2, dict3):
    statement = """
    Edge 1 of River: {} Cannibals, {} Missionaries
    Edge 2 (Other side of River): {} Cannibals, {} Missionaries
    Boat: {} Cannibals, {} Missionaries
    
    """
    print(statement.format(dict1['can'], dict1['miss'], dict2['can'], dict2['miss'],
                           dict3['can'], dict3['miss']))


#create the cannibal/missionary function -- call the function people for short
def people(e1 = edge1, e2 = edge2, b = boat):
    
    #edge2 of river is empty
    if all(r == 0 for r in e2.values()):  #The all() function returns True if all items in an iterable are true, otherwise False
        print_graph(e1, e2, b)
        
        #one cannibal will leave edge1 of river
        e1['can'] = e1['can'] - 1
        
        #they get into the boat
        b['can'] = b['can'] + 1
        
    # One missionary will leave edge1 of river
    e1['miss'] = e1['miss'] - 1
    
    #enters boat
    b['miss'] = b['miss'] + 1
    print_graph(e1, e2, b)
    
    #edge1 of river is empty
    if all(r == 0 for r in e1.values()):
        
        #one cannibal and one missionary leave boat
        b['can'], b['miss'] = 0, 0
        #one cannibal is on edge2 of river
        e2['can'] = e2['can'] + 1
        
        #one missionary is on edge2 of river
        e2['miss'] = e2['miss'] + 1
        print_graph(e1, e2, b)
        return
    
    #one missionary leaves boat
    b['miss'] = b['miss'] -1
    
    #is on edge2 of river(the other side)
    e2['miss'] = e2['miss'] + 1
    print_graph(e1, e2, b)
    
    #one cannibal leaves edge 2 and gets on boat
    e1['can'] = e1['can'] - 1
    b['can'] = b['can'] + 1
    print_graph(e1, e2, b)
    
    #one cannibal leaves boat and is on edge2 of river(other side)
    b['can'] = b['can'] - 1
    e2['can'] = e2['can'] + 1
    print_graph(e1, e2, b)
    
    #The series of river crossings
    people(e1, e2, b)
    

#call the people() function
people()
    

        
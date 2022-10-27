def knows(R, x, y):
    # return True if x knows y
    return (y in R.get(x, set())) # if x not in R return empty set

def is_celeb(R, x): 
    # return True if a is celeb, otherwise return False
    # return False if x knows someone who is not him/herself
    # return False if there exists someone in R who don't know x
    # otherwise return True
    if len(R.get(x, set())) > 1:
        return False
    
    for key in R.keys():
        if (key != x) and (x not in R[key]):
            return False

    return True

def find_celeb(R):
    # for each person x in the party
    # if x is celeb --> return x
    # if no celeb in the party --> return None
    for x in R:
        if is_celeb(R, x):
            return x
    
    return None

def read_relations() :
    # build a dictionary R from inputs 
    # whose structure is shown in the example
    people = set()
    R = dict()

    while True:
        d = input().split()
        
        if len(d) == 1 :
            break
        
        u, v = d
        
        if u not in R:
            R[u] = set()
        
        R[u].add(v)

        people.add(u)
        people.add(v)
    
    for person in people:
        
        if person not in R:
            R[person] = set()
        
        R[person].add(person)

    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input().strip()) # do not remove this line
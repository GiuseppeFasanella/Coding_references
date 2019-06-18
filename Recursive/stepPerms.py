'''
Davis has a number of staircases in his house and he likes to climb each staircase 1, 2 or 3  steps at a time. 
Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb 
each staircase.

For example, there is  staircase in the house that is  steps high. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2

There are 13 possible ways he can take these  steps.
'''


#recursive function (there is room for dynamic programming in here)
def stepPerms(n):
    n_ways=0
    
    ##Posso fare 1 gradino alla volta, 2 gradini o 3 alla volta
    ##allowed_moves = [1,2,3]
    ## pop-out conditions
    if n==1:
        n_ways=1
        return n_ways
    elif n==2:
        n_ways=2
        return n_ways
    elif  n==3:
        n_ways=4
        return n_ways
    else:
        # 1. Posso fare un passo e a qual punto mi rimarrebbero tutte le possibilita'
        #    per una scala di n-1 gradini
        # 2. Posso fare due passi e a quel punto mi rimarrebbero tutte le possibilita'
        #    per una scala di n-2 gradini
        # 3. Posso fare tre passi e a quel punto mi rimarrebbero tutte le possibilita'
        #    per una scala di n-3 gradini
        
        n_ways=stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
        
    return n_ways


print(stepPerms(5))
# 13

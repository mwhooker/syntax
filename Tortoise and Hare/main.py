def floyd(f, x0):
    # The main phase of the algorithm, finding a repetition x_mu = x_2mu
    # The hare moves twice as quickly as the tortoise
    tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
 
    # at this point the start of the loop is equi-distant from current tortoise
    # position and x0, so hare moving in circle and tortoise (set to x0 )
    # moving towards circle, will intersect at the beginning of the circle.
 
    # Find the position of the first repetition of length mu
    # The hare and tortoise move at the same speeds
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
 
    # Find the length of the shortest cycle starting from x_mu
    # The hare moves while the tortoise stays still
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
 
    return lam, mu

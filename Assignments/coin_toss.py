def coin():
    Heads = 0
    Tails = 0

    for x in range(0,5000):
        import random
        flip = random.random()
        if (round(flip) == 1):
            Heads = Heads + 1
            print "Throwing a coin ... Head's win! Got {} head(s) so far and {} tails(s) so far..".format(Heads, Tails)
        else:
            Tails = Tails + 1
            print "Throwing a coin ... Tail's win! Got {} head(s) so far and {} tails(s) so far..".format(Heads, Tails)
    print "Ending the program, thank you!"
coin()

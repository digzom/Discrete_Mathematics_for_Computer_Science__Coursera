# n: number of pieces
# from_rod: the rod I want to move all pieces from
# to_rod: the rod I want to move all pieces piece for
def hanoi_towers(n: int, from_rod: int, to_rod: int):
    if n == 1:
        print(f"Move disk from {from_rod} to {to_rod}")
    else:
        unused_rod = 6 - from_rod - to_rod
        # to know how to move all pieces from 1 to 2, I have to discover how to
        # move the all the others from 1 to 3 (because 2 will be ocupied by the bigger)
        hanoi_towers(n - 1, from_rod, unused_rod)
        # after moving all pieces (except the last one) to the 3 rod, I have to move
        # the bigger one:
        print(f"Move disk from {from_rod} to {to_rod}")
        # after move the bigger one, I move all pieces from the 3 to 2
        hanoi_towers(n - 1, unused_rod, to_rod)


hanoi_towers(5, 1, 2)

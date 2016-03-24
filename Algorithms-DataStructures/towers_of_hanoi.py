# Algorithms & data Structures: Recursion - Towers of Hanoi
# 3/16/16
# @totallygloria


import random


def user_input():

    num_disks = int(raw_input('Enter a number of disks to move, between 1 and 10: '))
    while (num_disks <= 0) or (num_disks >= 11):
        num_disks = int(raw_input('Please enter a number of disks to move, between 1 and 10: '))

    locations = [1, 2, 3]

    start_loc = int(raw_input('Enter a starting pole (1, 2, or 3): '))
    if start_loc not in locations:
        start_loc = random.randrange(1,3)
        print "Invalid input, starting on ", start_loc
    locations.remove(start_loc)

    dest_loc = int(raw_input('Enter the destination pole (must be different from the start): '))
    if dest_loc == start_loc:
        dest_loc = random.choice(locations)
        print "Invalid distination, starting on ", dest_loc
    locations.remove(dest_loc)

    helper = locations.pop()

    return num_disks, start_loc, dest_loc, helper


def game_setup(num_disks, start_loc):

    start_peg = []

    for i in range(num_disks, 0, -1):
        start_peg.append("disk"+str(i))

    if start_loc == 1:
        for i in range(num_disks-1, -1, -1):
            print start_peg[i], "\t\t", "|", "\t\t", "|"
    elif start_loc == 2:
        for i in range(num_disks-1, -1, -1):
            print "|", "\t\t", start_peg[i], "\t\t", "|"
    elif start_loc == 3:
        for i in range(num_disks-1, -1, -1):
            print "|", "\t\t", "|", "\t\t", start_peg[i]



def move_disk(current_loc, dest_loc):
    """ The idea is that this would pop a disk off it's current location
    and then append it to the correct list.
    """
    current_disk = current_loc.pop()
    print "moving %s from %s to %s" % (current_disk, current_loc, dest_loc)
    dest_loc.append(current_disk)


def hanoi_solver(num_disks, start_loc, dest_loc):
    """ If the number of disks is one, just move it to the destination.
    Else, move the (n-1) stack to the helper, move the disk to the dest, move
    the stack to the dest-peg. The first and third calls are recursive, the middle
    is simply a call to the move function.
    """

    if num_disks == 1:
        move_disk(start_loc, dest_loc)


def main():

    num_disks, start_loc, dest_loc, helper = user_input()
    game_setup(num_disks, start_loc)





main()
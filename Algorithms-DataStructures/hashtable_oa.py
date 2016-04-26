# Algorithms and Data Structures: Hash Tables & Hashing
# 4.26.2016
# @totallygloria

"""
Uses a python list to hold the values in the hash table.
Hashing function is a separate call, so it can be changed independently.
If there's a collision, resolves using open addressing.
"""
from calculate_two_off_primes import massage_primes


class OAHashTable(object):

    def __init__(self):
        self.size = 0
        self.occupancy = 0
        self.htable = []
        self.initialize_table()

    def initialize_table(self):
        """ Sets self.htable to a prime-length list populated None, up to a max length of 104683.
        The prime selected is the first prime number larger than the desired length, where there
        also exists a pair prime number exactly 2 smaller than the table size (for rehashing). """
        two_off_primes = massage_primes()
        largest_prime = two_off_primes[-1]
        try:
            des_len = int(raw_input('Approximately how large would you like your initial table to be?'))
        except ValueError:
            self.size = two_off_primes[0]
            self.htable = [None] * two_off_primes[0]

        if des_len > largest_prime:
            print "Largest available prime is %d, setting that as max table size." % largest_prime
            self.size = largest_prime
            self.htable = [None] * largest_prime
        else:
            i = 0
            while des_len > two_off_primes[i]:
                i += 1
            self.size = two_off_primes[i]
            self.htable = [None] * two_off_primes[i]

    def compute_hash(self, item):
        """ Given a item, returns its hashed value """
        # TODO this needs a recompute for collisions, I think
        hashedval = item ** 2
        return hashedval % self.size

    def insert_hash(self, item):
        """ Hashes item, if the slot is empty it inserts, otherwise it walks the table
        until it finds an open slot (None) or a 'USED' slot and puts it there.
        Wraps at the end of the table. Does not accept duplicate entries. """
        hashed_val = self.compute_hash(item)
        if self.htable[hashed_val] == item:
            return
        elif self.htable[hashed_val] is None or self.htable[hashed_val] == 'USED':
            self.htable[hashed_val] = item
            self.occupancy += 1
        else:
            while self.htable[hashed_val] is not None and self.htable[hashed_val] != 'USED':
                hashed_val += 1
                if hashed_val >= self.size:
                    hashed_val = 0
                if self.htable[hashed_val] == item:
                    return
            self.htable[hashed_val] = item
            self.occupancy += 1

    def search_hash(self, item):
        """ Hashes item, checks if it's in the hash table - if it's not where it's expected
        to be, walks the table until a None is found. Returns a boolean. """
        hashed_val = self.compute_hash(item)
        if self.htable[hashed_val] == item:
            return True
        else:
            if self.htable[hashed_val] is not None:
                while self.htable[hashed_val] is not None:
                    if self.htable[hashed_val] == item:
                        return True
                    hashed_val += 1
                    if hashed_val >= self.size:
                        hashed_val = 0
            return False

    def remove_item(self, item):
        """ Searches for an item in the hash table, if it's not in the proper slot,
        checks until you hit the first None. When the item is found, it's replaced
        with a marker and returns a boolean. """
        hashed_val = self.compute_hash(item)
        if self.htable[hashed_val] == item:
            self.htable[hashed_val] = 'USED'
            self.occupancy -= 1
            return True
        else:
            if self.htable[hashed_val] != item and self.htable[hashed_val] is not None:
                while self.htable[hashed_val] is not None:
                    if self.htable[hashed_val] == item:
                        self.htable[hashed_val] = 'USED'
                        self.occupancy -= 1
                        return True
                    hashed_val += 1
                    if hashed_val >= self.size:
                        hashed_val = 0
            return False

# Zaw Than, Student ID:#001368744

import csv
from Package import Package


class ChainingHashTable:
    """ Create Hash table and its methods. """

    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, package):
        """ Insert value to hash table. O(1). """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(package)

    def search(self, key):
        """ Search value by key. O(1). """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list

    def remove(self, key):
        """ Remove value by key. O(1). """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        self.table.remove(bucket_list)


""" 
    Pseudocode for get hash method 
        read csv file
        get id 
        get address
        get city
        get state
        get zip code
        get deadline 
        get weight
        get note
        set status as 'at the hub'
        create package with class
        insert package to hash table
        
        return hash table
"""


def get_hash():
    """ Create hash table from packages csv file. O(N). """

    h = ChainingHashTable(40)
    file = open('packages.csv')
    reader = csv.reader(file)

    for row in reader:
        pid = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        status = 'at the hub'
        p = Package(pid, address, city, state, zip_code, deadline, weight, note, status)
        h.insert(pid, p)

    return h

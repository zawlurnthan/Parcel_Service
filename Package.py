# Zaw Than, Student ID:#001368744

class Package:
    """ Create Package and it's method. """

    def __init__(self, pid, add, city, state, zip_code, deadline, weight, note, status):
        self.id = pid
        self.address = add
        self.city = city
        self.state = state
        self.zip = zip_code
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = status

    def __repr__(self):
        return str(self.id) + ", " + str(self.address) + ", " + str(self.city) + ", " + str(self.state) + ", " \
               + str(self.zip) + ", " + str(self.deadline) + ", " + str(self.weight) + ", " + str(self.note) + \
               ", " + str(self.status) + "\n"

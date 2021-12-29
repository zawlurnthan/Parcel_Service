# Zaw Than, Student ID:#001368744

import datetime
from Graph import get_graph
from Hash import get_hash
from Package import Package


class Truck:
    """ Create Truck Object and relative methods of truck object. """

    def __init__(self):
        self.time = datetime.datetime(2021, 1, 9, 0, 00, 00)
        self.packages = []
        self.route = []

    def insert(self, package):
        """ Insert package to the truck. O(1) """
        self.packages.append(package)
        add = f'{package.address} ({package.zip})'
        self.route.append(add)

    def remove(self, package):
        """ Remove package from the truck. O(1) """
        self.packages.remove(package)
        add = f'{package.address} ({package.zip})'
        self.route.remove(add)

    def start_time(self, y, mon, d, h, m, s):
        """ Define truck starting time of delivery. """
        self.time = datetime.datetime(year=y, month=mon, day=d, hour=h, minute=m, second=s)

    def get_time(self):
        return self.time


# Create three truck
T1 = Truck()
T2 = Truck()
T3 = Truck()

"""  
    Pseudocode for loading truck method
    
        put wrong address package and delay packages with EOD deadline in truck 3
        put truck 2 only packages and delay packages with 10:30 am deadline in truck 2
        put id 19 package and all all packages with time deadline in truck 1
        
        if packages in truck 1 is less than 16, load more packages to reach maximum number 16
        if packages in truck 2 is less than 16, load more packages to reach maximum number 16 as well
        the rest of all leftover packages go to Truck 3 
"""


def load_trucks():
    """ Assign and load all the packages from hash table to each truck. Greedy Algorithm is used here. O(N^2). """

    h = get_hash()
    packages = []

    for x in h.table:
        for i in x:
            packages.append(i)

    for line in h.table:
        for p in line:
            if (p.deadline == 'EOD' and 'Delayed' in p.note) or 'Wrong' in p.note:
                T3.insert(p)
                packages.remove(p)

            elif 'Can only' in p.note or ('10:30' in p.deadline and 'Delayed' in p.note):
                T2.insert(p)
                packages.remove(p)

            elif p.id == 19 or '10:30' in p.deadline or '9:00' in p.deadline:
                T1.insert(p)
                packages.remove(p)

    for pk in packages:
        if len(T1.packages) < 16:
            T1.insert(pk)

        elif len(T2.packages) < 16:
            T2.insert(pk)

        else:
            T3.insert(pk)


""" 
    Pseudocode for get shortest path and get route method
    
        get the route of a truck as parameter
            Starting from University address as hub
            find shortest distance in route from starting point (hub)
            get location of shortest distance
            
            repeat the circle to find another shortest distance from first shortest location 
            repeat the circle until end of the route    
            
            put all shortest distance locations from point to point in a list and add the hub to return in the end
            return list
"""


def get_shortest_path(graph, truck, start):
    """ Nearest Neighbor algorithm is used to find shortest distance of current location. O(N). """

    distance = {}
    close_location = ''

    for add in truck.route:
        value = graph.search(start, add)
        distance[start, add] = value

    close_distance = min(distance.values())

    for k, v in distance.items():
        if v == close_distance:
            close_location = k[1]

    return close_location


def get_route(truck):
    """ This method is part of the finding nearest neighbor algorithm.
    It sorts route and add starting and ending point. O(N). """

    graph = get_graph()
    hub = '4001 South 700 East (84107)'
    path = [hub]
    while truck.route:
        location = get_shortest_path(graph, truck, path[-1])
        path.append(location)
        truck.route.remove(location)
    path.append(hub)
    return path


def set_current_time(truck, miles):
    """Setting current time in delivery. O(1). """
    minute = miles * 3.33
    truck.time += datetime.timedelta(minutes=minute)


""" 
    Pseudocode for get mileages method
        get sorted truck route
        get distance of two consecutive locations of the route
        add all distance 
        return total distance
"""


def get_mileages(truck):
    """ This function is used to get total mileages of a truck. O(N). """

    graph = get_graph()
    route = truck.route
    total_distance = 0.0

    for i in range(len(route) - 1):
        distance = graph.search(route[i], route[i + 1])
        total_distance += distance

    return total_distance


""" 
    Pseudocode for delivery method
    
        get truck route
        set starting time of delivery
            get distance form sorted route
            record the current time by distance of truck travels
            
            if current time is less than search time
                if package location is already visited 
                    set the status of packages on the truck as delivered at current time
                    
        print all the packages on the truck
        print truck end time which is the time truck come back to hub
"""


def delivery(truck, h, m, s):
    """ Deliver each truck and change the status of each delivered package
    and show returning time of truck. O(N^2). """

    graph = get_graph()
    route = truck.route
    search_time = datetime.datetime(2021, 1, 1, h, m, s)

    for i in range(len(route) - 1):
        distance = graph.search(route[i], route[i + 1])
        set_current_time(truck, distance)
        current_time = truck.get_time()

        if current_time < search_time:
            for x in truck.packages:
                if route[i + 1][:10] in x.address:
                    delivered_time = truck.get_time().time().strftime('%H:%M:%S %p')
                    x.status = f'delivered at {delivered_time}.'
    printing_packages(truck)
    back_time = truck.get_time().time().strftime('%H:%M:%S %p')
    print(f'Truck come back to hub at {back_time}.')


def printing_packages(truck):
    """ Printing all packages of a truck. """
    for x in truck.packages:
        print(x)


def set_status(truck):
    """ Setting status of every package which is loaded. O(N). """
    for x in truck.packages:
        x.status = 'en route'


""" 
    Pseudocode for check status method 
        load all truck
        
        for truck 1
        get sorted route of truck
        set starting time of delivery
        set status of all packages loaded to truck as 'en route'
        run the delivery method 
            to get distance, 
            current time and 
            set the status of packages which is visited location as 'delivered at current time'
        get total distance of truck travels
        
        repeat the process for all three trucks except loading trucks method

        for truck 2
        truck 2 wait delayed packages
        start delivery at 9:10 am
        tht rest part of the process is same as first truck process
        
        for truck 3
        Truck 3 is not able to start until first truck come back to hub because of only two drivers available.
        In this case 
        All packages which are load to truck 3, will remain in hub at first a few hours
        Once truck 3 started
        process will be same as first two truck
        
        print Total mileages traveled by all trucks
"""


def check_status(h, m, s):
    """ To check all the packages info in specific time interval and show total mileages of all Trucks. O(N^2). """

    search_time = datetime.datetime(2021, 1, 1, h, m, s)
    load_trucks()

    # Process for truck 1.
    T1.route = get_route(T1)
    T1.start_time(2021, 1, 1, 8, 00, 00)
    set_status(T1)
    print('\nTruck 1 delivery \nTruck 1 started at 8:00 AM.\n')
    delivery(T1, h, m, s)
    distance1 = get_mileages(T1)
    print(f'Truck 1 travels {distance1:.2f} miles.')
    truck_returning_time = T1.get_time()

    # Process for truck 2.
    T2.route = get_route(T2)
    T2.start_time(2021, 1, 1, 9, 10, 00)
    set_status(T2)
    print('\n\n\nTruck 2 delivery \nTruck 2 started at 9:10 AM.\n')
    delivery(T2, h, m, s)
    distance2 = get_mileages(T2)
    print(f'Truck 2 travels {distance2:.2f} miles.')

    # Process for truck 3 which has two parts. one is before loading and after loading.
    distance3 = 0.0
    if truck_returning_time > search_time:
        print(f'\n\n\nTruck 3 delivery \nTruck 3 will start when Truck 1 come back to hub.\n')
        printing_packages(T3)
        print('Truck 3 is still at Hub at this time.')
    else:
        fix_address()
        T3.route = get_route(T3)
        T3.time = T1.get_time()
        t3_time = T3.time.strftime('%H:%M:%S %p')
        set_status(T3)
        print(f'\n\n\nTruck 3 delivery \nTruck 3 started at {t3_time}.\n')
        delivery(T3, h, m, s)
        distance3 = get_mileages(T3)
        print(f'Truck 3 travels {distance3:.2f} miles.')
        print('\nPackage 9 address is fixed at 10:20 AM.')

    total = distance1 + distance2 + distance3
    print(f'Total mileages traveled by all trucks is {total:.2f} miles.')


def fix_address():
    """ Fixing wrong address. O(N). """
    for x in T3.packages:
        if 'Wrong' in x.note:
            T3.remove(x)
            p = Package(9, '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD', 2, 'Address fixed', '')
            T3.insert(p)

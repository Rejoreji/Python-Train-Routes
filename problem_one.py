"""
PROBLEM ONE:  TRAINS

Problem:  The local commuter railroad services a number of towns in Kiwiland.
Because of monetary concerns, all of the tracks are 'one-way.' That is, a route from Kaitaia to
Invercargill does not imply the existence of a route from Invercargill to Kaitaia.
In fact, even if both of these routes do happen to exist, they are distinct and are not
necessarily the same distance!

The purpose of this problem is to help the railroad provide its customers with information about the routes.
In particular, you will compute the distance along a certain route, the number of different routes between two
towns, and the shortest route between two towns.

Input:  A directed graph where a node represents a town and an edge represents a route between two towns.
The weighting of the edge represents the distance between the two towns.
A given route will never appear more than once, and for a given route, the starting and ending town will not
be the same town.

Output: For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the
route as given; do not make any extra stops!  For example, the first problem means to start at city A, then
travel directly to city B (a distance of 5), then directly to city C (a distance of 4).

1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3
stops.  In the sample data below, there are two such trips: C-D-C (2
stops). and C-E-B-C (3 stops).
7. The number of trips starting at A and ending at C with exactly 4 stops.
In the sample data below, there are three such trips: A to C (via B,C,D); A
to C (via D,C,D); and A to C (via D,E,B).
8. The length of the shortest route (in terms of distance to travel) from A
to C.
9. The length of the shortest route (in terms of distance to travel) from B
to B.
10. The number of different routes from C to C with a distance of less than 30.
In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC,
CEBCEBC, CEBCEBCEBC.

Test Input:

For the test input, the towns are named using the first few letters of the alphabet from A to D.
A route between two towns (A to B) with a distance of 5 is represented as AB5.

Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

Expected Output:

Output #1: 9
Output #2: 5
Output #3: 13
Output #4: 22
Output #5: NO SUCH ROUTE
Output #6: 2
Output #7: 3
Output #8: 9
Output #9: 9
Output #10: 7
==========
"""
from lib.trains import Trains
from lib.routes import Routes
from lib.stops import Stop
from lib.towns import Town
import unittest

class TrainsTests(unittest.TestCase):

    def setUp(self):
        print "setting up classes..."
        self.trains = Trains()
        self.routes = Routes()

        print "initializing towns..."
        self.a = Town('a')
        self.b = Town('b')
        self.c = Town('c')
        self.d = Town('d')
        self.e = Town('e')

        print "adding routes to route table..."
        self.routes.add_route_to_table(self.a, Stop(self.a, self.b, 5).next(Stop(self.a, self.d, 5).next(Stop(self.a, self.e, 7))))
        self.routes.add_route_to_table(self.b, Stop(self.b, self.c, 4))
        self.routes.add_route_to_table(self.c, Stop(self.c, self.d, 8).next(Stop(self.c, self.e, 2)))
        self.routes.add_route_to_table(self.d, Stop(self.d, self.c, 8).next(Stop(self.d, self.e, 6)))
        self.routes.add_route_to_table(self.e, Stop(self.e, self.b, 3))

    def test_read_input(self):
        print "verifying text file import..."
        self.assertNotEquals(self.trains.schedule_data, "")

    def test_train_array_exists(self):
        print "test existence of train routes..."
        routes = Routes()
        self.assertNotEquals(routes, [])

    def test_correct_data_type_from_route(self):
        print "asserting correct data types..."
        self.assertIsInstance(self.routes.route_table[self.a], Stop)
        self.assertIsInstance(self.routes.route_table[self.b], Stop)
        self.assertIsInstance(self.routes.route_table[self.c], Stop)
        self.assertIsInstance(self.routes.route_table[self.d], Stop)
        self.assertIsInstance(self.routes.route_table[self.e], Stop)

    def test_distance_of_route_ABC(self):
        scenario = '''
        1. The distance of the route A-B-C.
        Output #1: 9
        '''
        print scenario

        towns = []
        towns.append(self.a)
        towns.append(self.b)
        towns.append(self.c)
        self.assertEquals(9, self.routes.distance_between_towns(towns))

    def test_distance_of_route_AD(self):
        scenario = '''
        2. The distance of the route A-D.
        Output #2: 5
        '''
        print scenario

        towns = []
        towns.append(self.a)
        towns.append(self.d)
        self.assertEquals(5, self.routes.distance_between_towns(towns))

    def test_distance_of_route_ADC(self):
        scenario = '''
        3. The distance of the route A-D-C.
        Output #3: 13
        '''
        print scenario

        towns = []
        towns.append(self.a)
        towns.append(self.d)
        towns.append(self.c)
        self.assertEquals(13, self.routes.distance_between_towns(towns))

    def test_distance_of_route_AEBCD(self):
        scenario = '''
        4. The distance of the route A-E-B-C-D.
        Output #4: 22
        '''
        print scenario

        towns = []
        towns.append(self.a)
        towns.append(self.e)
        towns.append(self.b)
        towns.append(self.c)
        towns.append(self.d)
        self.assertEquals(22, self.routes.distance_between_towns(towns))

    def test_distance_of_route_AED(self):
        scenario = '''
        5. The distance of the route A-E-D.
        Output #5: NO SUCH ROUTE
        '''
        print scenario

        towns = []
        towns.append(self.a)
        towns.append(self.e)
        towns.append(self.d)
        self.assertEquals("NO SUCH ROUTE", self.routes.distance_between_towns(towns))

    def test_num_stops_C_to_C_3(self):
        scenario = '''
        6. The number of trips starting at C and ending at C with a maximum of 3
        stops.  In the sample data below, there are two such trips: C-D-C (2
        stops). and C-E-B-C (3 stops).
        Output #6: 2
        '''
        print scenario

        num_stops = self.routes.number_of_stops(self.c, self.c, 3)
        self.assertEquals(2, num_stops)

    def test_num_stops_A_to_C_4(self):
        scenario = '''
        7. The number of trips starting at A and ending at C with exactly 4 stops.
        In the sample data below, there are three such trips: A to C (via B,C,D); A
        to C (via D,C,D); and A to C (via D,E,B).
        Output #7: 3
        '''
        print scenario

        num_stops = self.routes.number_of_stops(self.a, self.c, 4)
        self.assertEquals(3, num_stops)

    def test_shortest_route_A_to_C(self):
        scenario = '''
        8. The length of the shortest route (in terms of distance to travel) from A
        to C.
        Output #8: 9
        '''
        print scenario

        shortest_route = self.routes.shortest_route(self.a, self.c)
        self.assertEquals(9, shortest_route)

    def shortest_route_B_to_B(self):
        scenario = '''
        9. The length of the shortest route (in terms of distance to travel) from B
        to B.
        Output #9: 9
        '''
        print scenario

        shortest_route = self.routes.shortest_route(self.c, self.c)
        self.assertEquals(9, shortest_route)

    def test_num_diff_routes_C_to_C_less_30(self):
        scenario = '''
        10. The number of different routes from C to C with a distance of less than 30.
        Output #10: 7
        '''
        print scenario

        num_routes_within = self.routes.num_routes_within(self.c, self.c, 30)
        self.assertEquals(7, num_routes_within)


def main():
    unittest.main()

# if __name__ == '__main__':
#     main()
from trains import Trains


class Routes:
    route_table = {}
    trains = Trains()
    routes = []

    def __init__(self):
        pass

    def add_route_to_table(self, town_start, stops):
        self.route_table[town_start] = stops

    def get_distance_to_next_stop(self, next_town, stops):
        if stops.destination == next_town:
            return stops.distance
        else:
            #need to iterate through nexts
            if stops.next_stop:
                return self.get_distance_to_next_stop(next_town, stops.next_stop)
            else:
                return False

    def distance_between_towns(self, towns):

        distance = 0
        counter = 0

        for town in towns:
            try:
                next_town = towns[counter + 1]
            except IndexError:
                #list index out of range - this is
                # one over.  we're done.
                return distance

            stops = self.route_table[town]

            distance_to_next_stop = self.get_distance_to_next_stop(next_town, stops)
            if distance_to_next_stop:
                distance += distance_to_next_stop
            else:
                return "NO SUCH ROUTE"

            counter += 1

        return distance

    def number_of_stops(self, town_start, town_end, max_stops):
        return self.find_all_routes(town_start, town_end, 0, max_stops) - 1  #TODO: I'm getting a one-off error

    def find_all_routes(self, town_start, town_end, num_stops, max_stops):
        routes = 0

        # Check if start and end exists in route table
        # If start exists then traverse all possible
        # routes and for each, check if it is destination
        if town_start in self.route_table and town_end in self.route_table:

            # If destination, and number of stops are within
            # allowed limits, count it as possible route.
            num_stops += 1

            # Check if we've exceeded max stops
            if num_stops > max_stops:
                return 0

            # Mark start town as visited
            town_start.visited = True

            #retrieve current stop
            current_stop = self.route_table[town_start]
            while current_stop:

                # If destination matches, we increment route
                # count, then continue to next node at same depth
                if current_stop.destination == town_end:
                    routes += 1
                    current_stop = current_stop.next_stop
                    continue

                # If destination does not match, and
                # destination node has not yet been visited,
                # we recursively traverse destination node
                elif not current_stop.destination.visited:
                    num_stops -= 1
                    routes += self.find_all_routes(current_stop.destination, town_end, num_stops, max_stops)

                current_stop = current_stop.next_stop
        else:
            return "NO SUCH ROUTE"

        # Before exiting this recursive stack level,
        # we mark the start node as not visited.
        town_start.visited = False
        return routes

    def shortest_route(self, town_start, town_end):
        return self.find_shortest_route(town_start, town_end, 1, 0)

    def find_shortest_route(self, town_start, town_end, distance, shortest_route):
        if town_start in self.route_table and town_end in self.route_table:
            # If start node exists then traverse all possible
            # routes and for each, check if it is destination

            town_start.visited = True
            stop = self.route_table[town_start]
            while stop:
                # If node not already visited, or is the destination, increment distance
                if stop.destination == town_end or not stop.destination.visited:
                    distance += stop.distance

                # If destination matches, we compare
                # distance of this route to shortest route
                # so far, and make appropriate switch
                if stop.destination == town_end:
                    if shortest_route == 0 or distance < shortest_route:
                        shortest_route = distance
                    town_start.visited = False
                    return shortest_route  # Unvisit node and return shortest route

                # If destination does not match, and
                # destination node has not yet been visited,
                # we recursively traverse destination node
                elif not stop.destination.visited:
                    # Decrement distance as we backtrack
                    distance -= stop.distance
                    stop = stop.next_stop
                    if stop is not None:
                        return self.find_shortest_route(stop.destination, town_end, distance, shortest_route)
                    else:
                        return shortest_route





            else:
                return "NO SUCH ROUTE"

        # Before exiting this recursive stack level,
        # we mark the start node as visited.
        town_start.visited = False
        return shortest_route


        # Shortest route;
        # Wrapper for recursive function

    def num_routes_within(self, today_start, today_end, max_distance):
        # Wrapper to maintain weight
        return self.find_num_routes_within(today_start, today_end, 0, max_distance)

    def find_num_routes_within(self, town_start, town_end, distance, max_distance):
        routes = 0
        # Check if start and end nodes exists in route table
        if town_start in self.route_table and town_end in self.route_table:

            # If start node exists then traverse all possible
            # routes and for each, check if it is destination

            stop = self.route_table[town_start]

            while stop:
                distance += stop.distance
                # If distance is under max, keep traversing
                # even if match is found until distance is > max

                if distance <= max_distance:
                    if stop.destination == town_end:
                        routes += 1
                        routes += self.find_num_routes_within(stop.destination, town_end, distance, max_distance)
                        stop = stop.next_stop
                        continue

                    else:
                        routes += self.find_num_routes_within(stop.destination, town_end, distance, max_distance)
                        distance -= stop.distance  # Decrement distance as we backtrack


                else:
                    distance -= stop.distance

                stop = stop.next_stop


        else:
            return "NO SUCH ROUTE"

        return routes





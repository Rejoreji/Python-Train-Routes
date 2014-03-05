from towns import Town

data_path = 'data/trains_input.txt'


class Trains:
    """
    you will compute the distance along a certain route, the number of different routes between two
    towns, and the shortest route between two towns
    """
    schedule_data = ""


    def __init__(self):
        with open(data_path, 'r') as content_file:
            self.schedule_data = content_file.read()
        #prune the graph text - just in case
        self.schedule_data = self.schedule_data.replace("Graph: ", "")




















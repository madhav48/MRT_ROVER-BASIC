# Exercise 1: Create a Class with instance attributes
# Create a class ”Rover” with Swarm ID, Rover ID and Rover Location as instance attributes. Add Rover
# Geometry (l,w,h) as a class attribute (an attribute that is shared among all instances of the class)
# Add a function to print out Rover’s location along with its Swarm ID and Rover ID

class Rover:

    rover_geometry = {
        "length" : 2,
        "width" : 1.5,
        "height" : 1.5
    }


    def __init__(self, swarm_id, rover_id, rover_location):
        self.Swarm_ID = swarm_id
        self.Rover_ID = rover_id
        self.rover_location = rover_location

    def print_rover_details(self):
        print(f"The location of Rover is {self.rover_location}. Its Swarm ID is {self.Swarm_ID} and Rover ID is {self.Rover_ID}")


if __name__ == "__main__":

    rover1 = Rover(1,1,(0,0,0))
    rover1.print_rover_details()
    print(f"The location of Rover is {rover1.rover_location}. Its Swarm ID is {rover1.Swarm_ID} and Rover ID is {rover1.Rover_ID}")
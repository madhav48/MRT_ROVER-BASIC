# Exercise 2: Create Class Methods
# Now to add functionality to your class, add a method that would receive a message containing Swarm ID,
# Rover ID and how much the rover should move by, this method would decide whether the rover should
# act on the message or not depending on the Swarm ID, Rover ID of the message received. Example - A
# rover with Swarm ID 5 and Rover ID 1 shouldn’t act on a message sent to Swarm ID 2 Rover ID 2.
# Based on the decision taken by the previous method, invoke a method that would change the ”Rover
# location” instance attribute

class Rover:

    rover_geometry = {
        "length" : 2,
        "width" : 1.5,
        "height" : 1.5
    }

    rovers = []


    def __init__(self, swarm_id, rover_id, rover_location = (0,0,0)):
        self.Swarm_ID = swarm_id
        self.Rover_ID = rover_id
        self.rover_location = rover_location
        Rover.rovers.append({
            "rover_id" : self.Rover_ID,
            "swarm_id" : self.Swarm_ID,
            "rover_obj" : self
        })


    # Old version...
    def print_rover_details(self):
        print(f"The location of Rover is {self.rover_location}. Its Swarm ID is {self.Swarm_ID} and Rover ID is {self.Rover_ID}")

    #New one:
    @classmethod
    def get_rover_location(cls, swarm_id, rover_id):
        for rover in cls.rovers:
            if rover["rover_id"] == rover_id and rover["swarm_id"] == swarm_id:
                return rover["rover_obj"].rover_location
            
        raise ValueError
        

    @classmethod
    def move_rover(cls, swarm_id, rover_id, to_move):
        for rover in cls.rovers:
            if rover["rover_id"] == rover_id and rover["swarm_id"] == swarm_id:
                return rover["rover_obj"].__do_move(to_move)
            
        raise ValueError
    

    def __do_move(self, to_move):

        x,y,z = self.rover_location
        
        if type(to_move) == dict:
            x+= to_move["x"]
            y+= to_move["y"]
            z+= to_move["z"]

        elif type(to_move) in [list , tuple]:
            x+= to_move[0]
            y+= to_move[1]
            z+= to_move[2]

        else:
            raise ValueError

        self.rover_location = (x,y,z)
        return f"Updated location of rover is {self.rover_location} with swarm ID {self.Swarm_ID} and Rover ID {self.Rover_ID}"



if __name__ == "__main__":

    rover1 = Rover(1,1,(0,0,0))
    rover2 = Rover(1,2,(0,0,0))
    rover3 = Rover(2,2,(0,0,0))
    rover4 = Rover(2,3,(0,0,0))
    rover5 = Rover(5,1,(0,0,0))
    
    print(Rover.move_rover(5,1,(2,2,2)))
    print(Rover.move_rover(2,2,(2,3,6)))
    # print(rover1.__do_move((0,0,0)))
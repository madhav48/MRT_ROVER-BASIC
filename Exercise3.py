# Exercise 3: Create a child class
# We also happen to have a smaller rovers we call Daughter Rovers. Create a child class ”Daughter Rover”
# that inherits from the ”Rove” class. Daughter Rover being a smaller version has half the dimensions of
# the ”Rover” class.
# The daughter rover being smaller also modifies the method to move you would have created in the
# previous exercise. Due to constraints, the daughter rover can only move half the distance it has been
# instructed to move.

from Exercise2 import Rover

# class Rover():

#     rover_geometry = {
#         "length" : 2,
#         "width" : 1.5,
#         "height" : 1.5
#     }

#     rovers = []


#     def __init__(self, swarm_id, rover_id, rover_location = (0,0,0)):
#         self.Swarm_ID = swarm_id
#         self.Rover_ID = rover_id
#         self.rover_location = rover_location
#         Rover.rovers.append({
#             "rover_id" : self.Rover_ID,
#             "swarm_id" : self.Swarm_ID,
#             "rover_obj" : self
#         })



#     def print_rover_details(self):
#         print(f"The location of Rover is {self.rover_location}. Its Swarm ID is {self.Swarm_ID} and Rover ID is {self.Rover_ID}")

#     @classmethod
#     def move_rover(cls, swarm_id, rover_id, to_move):
#         for rover in cls.rovers:
#             if rover["rover_id"] == rover_id and rover["swarm_id"] == swarm_id:
#                 return rover["rover_obj"].do_move(to_move)
            
#         raise ValueError
    

#     def __do_move(self, to_move):

#         x,y,z = self.rover_location
        
#         if type(to_move) == dict:
#             x+= to_move["x"]
#             y+= to_move["y"]
#             z+= to_move["z"]

#         elif type(to_move) in [list , tuple]:
#             x+= to_move[0]
#             y+= to_move[1]
#             z+= to_move[2]

#         else:
#             raise ValueError

#         self.rover_location = (x,y,z)
#         return f"Updated location of rover is {self.rover_location} with swarm ID {self.Swarm_ID} and Rover ID {self.Rover_ID}"


class DaughterRover(Rover):
        
    rover_geometry = {axis: value/2 for axis , value in Rover.rover_geometry.items()}
        
    def __init__(self, swarm_id, rover_id, rover_location= (0,0,0)):
        super().__init__(swarm_id, rover_id, rover_location)


    def __do_move(self, to_move):
        if type(to_move) == dict:
            to_move = {axis: value/2 for axis , value in to_move.items()}
        elif type(to_move) in (list, tuple):
            to_move = [value/2 for value in to_move]
        else:
            raise ValueError
        return super().do_move(to_move)


if __name__ == "__main__":


    
    daughterrover1 = DaughterRover(1,1,(0,0,0))
    print(DaughterRover.move_rover(1,1,(2,2,2)))
    print(daughterrover1.rover_geometry)


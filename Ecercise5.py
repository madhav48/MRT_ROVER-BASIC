# Exercise 5: Add your own functionality and features !
# Add at least 1 new feature to the system we have designed. It could be an interface class that would
# take inputs from user and pass it to the rovers or it could be some sort of sensor on the rover. Be creative !

from Exercise4 import Manager, Operator, Scientist
from Exercise2 import Rover

class InputControl:

    rovers = {}

    def __init__(self):

        self.manager = Manager(1)
        self.operator = Operator(1)
        self.scientist = Scientist(1)

    def rover_deatils(self):
        details = input("Enter swarm ID and Rover ID by leaving space between them.").split(" ")
        details = [int(x) for x in details]
        return details

    def process_inputs(self, input_user):

        if input_user == "add_rover":
            return self.manager.add_rover(*self.rover_deatils())
        
        elif input_user == "del_rover":
            return self.manager.del_rover(*self.rover_deatils())
        
        elif input_user == "list_rovers":
            print(self.manager.list_rovers())
        
        elif input_user == "move_rover":
            details = self.rover_deatils()
            to_move = input("Enter the distances in x, y and z axis by leaving space between them..").split(" ")
            to_move = [int(x) for x in to_move]
            return self.operator.move_rover(*details, to_move)
        
        elif input_user == "rover_location":
            print(self.scientist.rover_location(*self.rover_deatils()))
        
        else:
            print("Error!")

    


if __name__ == "__main__":

    print("Hello user!")
    user_input = input("What do you want to do with rover..?")
    inp1 = InputControl()

    while True:

        inp1.process_inputs(user_input)
        print("Done!")
        user_input = input("What additional do you want to do with rover..?")

    
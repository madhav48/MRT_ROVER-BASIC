# Exercise 4: Create a User Class
# Create a class ”User” that would command the rovers. The user class would have User ID as an instance
# variable and a method that prints the User ID. It should also keep a track of all the Swarm IDs and
# Rover IDs of the rovers being used.
# Create Child Classes ”Scientist”, ”Operator” and ”Manager” and the relevant methods. Scientists can
# only view the rover location and are denied access to move the rover or add/remove rovers being controlled
# if they try to do so. Similarly, Operators can freely move the rover and Managers can add/remove rovers
# being controlled and are denied to all other methods.
# Remember, the message you send as an Operator should be compatible with the format the rover
# checks for !


from Exercise2 import Rover

class User:

    rovers = {}

    def __init__(self,userid) -> None:
        self.userid = userid

    def print_uid(self):
        print(self.user_id)
    
    @classmethod
    def add_rover(cls, swarm_id, rover_id):
        raise PermissionError
    
    @classmethod
    def del_rover(cls, swarm_id, rover_id):
        raise PermissionError

    def rover_location(self, swarm_id, rover_id):
        raise PermissionError

    def move_rover(self, swarm_id, rover_id, to_move):
        raise PermissionError



class Scientist(User):
    
    def __init__(self, userid) -> None:
        super().__init__(userid)
    
    def rover_location(self, swarm_id, rover_id):
        return Rover.get_rover_location(swarm_id, rover_id)
    

class Operator(User):
    
    def move_rover(cls, swarm_id, rover_id, to_move):

        if type(to_move) not in (list, tuple, dict):
            raise ValueError
        
        return Rover.move_rover(swarm_id, rover_id, to_move)


class Manager(User,Rover):

    def __init__(self, userid) -> None:
        super().__init__(userid)
    
    @classmethod
    def add_rover(cls, swarm_id, rover_id):
        if swarm_id in cls.rovers.keys():
            cls.rovers[swarm_id].append(rover_id)
        else:
            cls.rovers[swarm_id] = [rover_id]
    
    @classmethod
    def del_rover(cls, swarm_id, rover_id):
        cls.rovers[swarm_id].remove(rover_id)
        if cls.rovers[swarm_id] == []:
            cls.rovers.pop(swarm_id)

    @classmethod
    def list_rovers(cls):
        return cls.rovers



if __name__ == "__main__":

    # Creating object from every class (Useful class):
    sc1 = Scientist(1)
    op1 = Operator(1)
    mn1 = Manager(2)

    # Creating rover object..
    rover1 = Rover(1,2)

    # Adding rover to list (managed by user)..
    mn1.add_rover(1,2)
    # Manager.add_rover(1,2)
    
    print(Manager.list_rovers())
    print(mn1.list_rovers())

    # Manager.del_rover(1,2)
    # print(Manager.list_rovers())
    # print(mn1.list_rovers())

    op1.move_rover(1,2,(2,2,2))

    print(sc1.rover_location(1,2))
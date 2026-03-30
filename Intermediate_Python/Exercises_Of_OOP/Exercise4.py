class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, arm_left, arm_right, leg_left, leg_right):
        self.head = head
        self.arm_left = arm_left
        self.arm_right = arm_right
        self.leg_left = leg_left
        self.leg_right = leg_right

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Feet:
    def __init__(self):
        pass

class Human:
    def __init__(self):
        self.hand_left = Hand()
        self.hand_right = Hand()
        self.foot_left = Feet()
        self.foot_right = Feet()

        self.arm_left = Arm(self.hand_left)
        self.arm_right = Arm(self.hand_right)
        self.leg_left = Leg(self.foot_left)
        self.leg_right = Leg(self.foot_right)

        self.head = Head()

        self.torso = Torso(
            self.head, 
            self.arm_left, 
            self.arm_right, 
            self.leg_left, 
            self.leg_right
        )


person = Human()
print(person.torso.arm_left.hand)
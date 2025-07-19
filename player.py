from config import SPEED

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_position(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise ValueError('Incorrect argumets provided: must be an int')

    def get_position(self):
        return (self.x, self.y)
    
    def increment_position(self):
        self.x += SPEED

    def decrement_position(self):
        self.x -= SPEED


    


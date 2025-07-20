from config import SPEED, JUMP_HEIGHT, GRAVITY, HEIGHT, SQUARE_SIZE

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
    
    def move_right(self):
        self.x += SPEED

    def move_left(self):
        if self.x >= 0:
            self.x -= SPEED
    
    def jump(self):
        self.y -= JUMP_HEIGHT
        print('Jump, jump! Tora is jumping!!')

    def apply_gravity(self):
        if self.y < HEIGHT-SQUARE_SIZE:
            self.y += GRAVITY

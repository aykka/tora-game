from sprites.coin import Coin
from sprites.block import Block
from config import LVL_BLOCK_HEIGHT, LVL_BLOCK_WIDTH

def getLevel(level_path):
    objects = []
    with open(level_path) as file_object:
        contents = file_object.readlines()
        y = 0
        for line in contents:
            x = 0
            print(line.rstrip())
            for symbol in line:
                if symbol == '^':
                    block = Block(x, y)
                    objects.append(block)
                elif symbol == 'o': 
                    coin = Coin(x, y)
                    objects.append(coin)
                x += LVL_BLOCK_WIDTH
            y += LVL_BLOCK_HEIGHT
    return objects

        


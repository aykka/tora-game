from sprites.coin import Coin

def getLevel(level_path):
    objects = []
    with open(level_path) as file_object:
        contents = file_object.readlines()
        y = 0
        for line in contents:
            x = 0
            print(line.rstrip())
            for symbol in line:
                if symbol == '-':
                    # TODO: CREATE BLOCK HERE
                    print('This is block')
                elif symbol == 'o': 
                    # TODO: CREATE COIN HERE
                    coin = Coin(x, y)
                    objects.append(coin)
                    print(f'This is {coin.x} and {coin.y}')
                x += 20
            y += 20
    return objects

        


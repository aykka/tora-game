def getLevel(level_path):
    with open(level_path) as file_object:
        contents = file_object.readlines()
        for line in contents:
            print(line.rstrip())
            for symbol in line:
                if symbol == '-':
                    # TODO: CREATE BLOCK HERE
                    print('This is block')
                elif symbol == 'o': 
                    # TODO: CREATE COIN HERE
                    print('This is coin')


getLevel('../levels/1.txt')
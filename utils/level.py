def getLevel(level_path):
    with open(level_path) as file_object:
        contents = file_object.read()
        print(contents)

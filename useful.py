import json


with open("data/filenames.json", "r") as read_file:
    files = json.load(read_file)


def getFile(changed_id):
    file=files[changed_id]
    return file

    
    

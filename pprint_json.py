import json
import pprint

sourceFile = open(input("Hey, type path to file please: "))

def File_to_survive():
    json_data = json.load(sourceFile)
    print(pprint.pprint(json_data))


__name__=="__main__"
File_to_survive()
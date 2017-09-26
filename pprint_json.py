import json
import pprint

source_file = open(input("Hey, type path to file please: "))

def file_to_survive():
    json_data = json.load(source_file)
    print(pprint.pprint(json_data))


__name__=="__main__"
file_to_survive()

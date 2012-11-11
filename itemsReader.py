import sys
import json


def main():
    """main function for parsing"""
    i = 0
    try:
        if sys.argv[1]:
            json_items = read_json_file(sys.argv[1])
        for json_item in json_items:
            print i, json_item['item_id']
            i += 1
    except IndexError:
        print 'You have to specify a filename to parse!'
    pass


def read_json_file(filename):
    """This function reads the file passed as arg and load the array of jsons"""
    try:
        json_items_file = open(filename)
        return json.load(json_items_file)
    except IOError:
        print "Ups, looks like that file does not exists"
        exit()
    pass


if __name__ == '__main__':
    main()

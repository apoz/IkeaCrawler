import sys
import json


#global variables
item_ids = {}


def main():
    """main function for parsing"""
    try:
        if sys.argv[1] and sys.argv[2]:
            (readfile, writefile) = open_files(sys.argv[1], sys.argv[2])
            json_items = read_json_file(readfile)
            for json_item in json_items:
                if item_id_unique(json_item['item_id'][0]):
                    write_json_file(writefile, json_item)
                else:
                    print json_item['item_id'], "already processed"
            print "Looks like I am done!!"
            close_files(readfile, writefile)
    except IndexError:
        print 'You have to specify a filename to parse!'
    pass


def open_files(readfilename, writefilename):
    """Function to open the files """
    try:
        readfile = open(readfilename, "r")
        writefile = open(writefilename, "a")
    except IOError:
        print "Ups, something went wrong with file openings!"
        exit()
    return (readfile, writefile)


def close_files(readfile, writefile):
    """Function to open the files """
    try:
        readfile.close()
        writefile.close()
    except IOError:
        print "Ups, something went wrong with file closings!"
        exit()
    pass


def write_json_file(filename, json_item):
    """Function for writing an item in a Json file"""
    try:
        # This tries to open an existing file but creates a new file if necessary.
        filename.write(json.dumps(json_item) + "\n")
    except IOError:
        print "Ups, something went wrong when writing the file"
        exit()
    pass


def item_id_unique(item_id):
    """Function to check if the item_id has been already dumped"""
    global item_ids
    print "Item id", item_id.encode('utf-8')
    try:
        if item_ids[item_id.encode('utf-8')]:
            print item_id, "already exists in the hash table"
            return False
    except KeyError:
        item_ids[item_id.encode('utf-8')] = True
        return True
    pass


def read_json_file(json_items_file):
    """This function reads the file passed as arg and load the array of jsons"""
    try:
        return json.load(json_items_file)
    except IOError:
        print "Ups, looks like that file does not exists"
        exit()
    pass


def item():
    """docstring for fname"""
    pass
if __name__ == '__main__':
    main()

import json

#for reading from the data.json file
def read(filename):
    with open (filename, mode="r") as jfile:
        jInput = json.load(jfile)
    jfile.close()
    return jInput

#for writing into the dataUpdated file
def write(filename="datatest.json", newdata=[{"Kindly Provide the data"}]):
    with open (filename, mode="w") as jfile:
        json.dump(newdata, jfile, indent=1, sort_keys=True)
    jfile.close()


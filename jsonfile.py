import json
def read(filename):
    with open (filename, mode="r") as jfile:
        jInput = json.load(jfile)
    jfile.close()
    return jInput

def write(filename="datatest.json", newdata=[{"Kindly Provide the data"}]):
    with open (filename, mode="w") as jfile:
        #filedata = json.load(jfile)
        #jfile.write(newdata["Gender"])
        #filedata.append(newdata)
        #print(filedata)
        #jfile.seek(0)
        json.dump(newdata, jfile, indent=1, sort_keys=True)

    jfile.close()


from os import listdir
from os.path import isfile, join, splitext
import json
from block import block

# Opens all json files in a directory and returns 2D list
# [[Block1,Block2,Block3],
#  [Block1,Block2,Block3]]
#
def open_json_files(directory):

    sessions = {}

    # Get only json files
    json_files = [join(directory,f) for f in listdir(directory) if isfile(
        join(directory, f)) and splitext(join(directory, f))[1] == ".json"]

    # Open all JSON files
    for f in json_files:
        
        with open(f, "r") as json_file:
            jdict = json.load(json_file)
            blk = block().obj_from_json(jdict["block"])
            if blk.session in sessions.keys():
                sessions[blk.session][blk.blocknum] = blk
            else:
                sessions[blk.session] = {blk.blocknum: blk}
                

    patids = []
    for sess in sessions.values():
        for blk in sess.values():
            if blk.patID not in patids:
                patids.append(blk.patID)
    if len(patids)>1:
        return sessions, True

    return sessions, False

def sess_to_csv(sess, folder_name):
    for blk in sess.values():
        with open(join(folder_name,f"Block{blk.blocknum}_{blk.date}.csv"), "w") as csv_file:
            trls = list(blk.trials)
            for i, trl in enumerate(trls):
                csv_file.write(f"Trial {i} emg, Trial {i} acc,")
            csv_file.write("\n")
            max_len = max([len(data) for trl in trls for data in (trl.emg_data, trl.acc_data)])
            for i in range(max_len):
                for trl in trls:
                    if len(trl.emg_data) > i:
                        csv_file.write(str(trl.emg_data[i]))
                    csv_file.write(",")
                    if len(trl.acc_data) > i:
                        csv_file.write(str(trl.acc_data[i]))
                    csv_file.write(",")
                csv_file.write("\n")


import hashlib  # md5


instr="cdc9f61f8154d9174808223df0be80b3"
outstr="dac4b5da5bd69828033fb2aa5e84fd3e"

def getKey(hashstr):
        hl = hashlib.md5()
        hl.update((hashstr+'kgcloud').encode("utf-8"))
        result=hl.hexdigest()
        return result

print(getKey(instr))
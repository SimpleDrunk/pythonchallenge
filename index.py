import os, shutil

for i in range(4, 13):
    if os.path.exists("./" + str(i)):
        print "%d folder exist!" % i
    else:
        os.mkdir("./" + str(i))

    if os.path.exists("./%d.py" % i):
        shutil.move("./%d.py" % i, "./%d/" % i);
    else:
        print "%d.py not exist" % i
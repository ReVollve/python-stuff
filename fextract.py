import os.path
import shutil
import filecmp

path = os.path.dirname(__file__)


def append_id(filename, id):
    return "{0}_{2}.{1}".format(*filename.rsplit('.', 1) + [id])


if __name__ == "__main__":
    print("Starting in", path)
    folders = [x[0] for x in os.walk(path)]
    for x in folders:
        for item in os.listdir(x):
            abspath = os.path.join(x, item)
            altpath = os.path.join(path, item)
            if x == path:
                continue
            if not os.path.isfile(abspath):
                continue
            if os.path.exists(altpath):
                if not filecmp.cmp(abspath, altpath):
                    print("Mismatching file:", abspath)
                    i = 1
                    while True:
                        name = append_id(item, i)
                        thatpath = os.path.join(path, name)
                        if not os.path.exists(thatpath):
                            shutil.copy(abspath, thatpath)
                            print("Copied {}".format(name))
                            break
                        if filecmp.cmp(abspath, thatpath):
                            break
                        i = i + 1
            else:
                shutil.copy(abspath, altpath)
                print("Copied {}".format(item))
    print("Done!")

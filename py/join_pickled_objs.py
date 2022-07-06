import sys
import pickle


def printNone(par, non=True):
    if par[-1] == None and non:
        print(par)
    elif par[-1] == None and not non:
        pass
    else:
        pass #print(par)

if len(sys.argv) > 1:
    for x in range(len(sys.argv)):
        print(sys.argv[x])

main_filename = "solsysbod_dct.pickle"
add_filename = "solsysbod_add_dct.pickle"
result_filename = "solsysbod_res_dct.pickle"
all_lst = []

try:
    with open(main_filename, 'rb') as fl:
        main_objects = pickle.load(fl)
except Exception:
    main_objects = {}

with open(add_filename, 'rb') as fl:
    add_objects = pickle.load(fl)

for obj in add_objects:
    if obj not in main_objects:
        main_objects[obj] = add_objects[obj]
    else:
        print(obj, "already exist:", "\n", main_objects[obj], "\n", add_objects[obj])

with open(result_filename, 'wb') as fl:
    pickle.dump(main_objects, fl)

print(f"Total {len(main_objects)} objects in pickled object")

import pickle
from object_data import BODIES_SIZE_ORDERED


PICKLE_FILENAME = "solsysbod_dct.pickle"
PICKLE_RESULT_FILENAME = "solsysbod1_dct.pickle"


def dct_sort(bodies_lst, bodies_params_dct):
    res_dct = {}
    for objname in bodies_lst:
        if objname in bodies_params_dct:
            res_dct[objname] = bodies_params_dct[objname]
        else:
            print(objname, "is not in params dict")
    for objname in bodies_params_dct:
        if objname not in res_dct:
            res_dct[objname] = bodies_params_dct[objname]
    return res_dct


try:
    with open(PICKLE_FILENAME, 'rb') as handle:
        bodies_params_dct = pickle.load(handle)
except Exception:
    bodies_params_dct = {}

objects = dct_sort(BODIES_SIZE_ORDERED, bodies_params_dct)

with open(PICKLE_RESULT_FILENAME, 'wb') as handle:
    pickle.dump(objects, handle)

a = {
    "fdb:fdb-list": [
        {
            "vlan-id": 2,
            "mac-addr": "00:00:00:00:00:12",
            "interface": "PortChannel1",
            "type": "Static",
            "asic": "No",

        },
        {
            "vlan-id": 3,
            "mac-addr": "00:00:00:00:00:13",
            "interface": "PortChannel1",
            "type": "Static",
            "asic": "No",
            "1": {1: 1, 2: 2}
        },

    ]
}

b = {
    "fdb:fdb-list": [
        {
            "vlan-id": 3,
            "mac-addr": "00:00:00:00:00:13",
            "interface": "PortChannel1",
            "type": "Static",
            "asic": "No",
            "1": {1: 1, 2: 2}
        },
        {
            "vlan-id": 2,
            "mac-addr": "00:00:00:00:00:12",
            "interface": "PortChannel1",
            "type": "Static",
            "asic": "No",

        },
    ]
}


def dict_comp(dict_1, dict_2):
    if dict_1.keys() != dict_2.keys():
        return False
    for key, values in dict_1.items():
        if key not in dict_2.keys():
            return False
        else:
            if dict_2.get(key, None) is None or type(values) != type(dict_2[key]):
                return False
            if type(values) == list:
                if not list_comp(values, dict_2[key]):
                    return False
            elif type(values) == dict:
                if not dict_comp(values, dict_2[key]):
                    return False
            else:
                if values != dict_2.get(key, None):
                    return False
    return True


def list_comp(list_1, list_2):

    if len(list_1) != len(list_2):
        assert False, "list size not equal."

    for idx, item1 in enumerate(list_1):
        if type(item1) == list:
            item2 = list_2[idx]
            if not list_comp(item1, list_2[idx]):
                return False
        elif type(item1) == dict:
            is_find = False
            for dict2 in list_2:
                if dict_comp(item1, dict2):
                    is_find = True
                    list_2.remove(dict2)
                    break
            if not is_find:
                return False
        else:
            if item1 != list_2[idx]:
                return False
    return True


print(dict_comp(a, b))


my_dct = eval(input())
new_key = ''
flat_dict = {}


def flatten(dct):

    global new_key, flat_dict
    for i in dct:
        if type(dct[i]) == dict:
            new_key += i + '.'
            flatten(dct[i])
        else:
            flat_dict.update(dict([(new_key + i, dct[i])]))
            if new_key in dct.keys():
                new_key = ''


flatten(my_dct)
print(flat_dict)







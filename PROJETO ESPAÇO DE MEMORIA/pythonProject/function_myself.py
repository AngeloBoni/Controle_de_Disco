def transform_mb(dic):
    for key in dic:
        dic[key] = int(dic[key]) / 1048576

    return dic

def percent(dic, soma):
    percent = {}

    for key in dic:
        percent[key] = (int(dic[key]) * 100) / soma

    return percent
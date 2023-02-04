def recurs_find_key(key, obj):
    if obj == None:
        return None
    else:
        if key in obj:
            return obj[key]
        if type(obj) == dict or type(obj) == list:
            for k, v in obj.items():
                if type(v) == dict:
                    result = recurs_find_key(k, v)
                    return result
                elif type(v) == list:
                    for el in range(len(v)):
                        result = recurs_find_key(k, v[el-1])
                        return result
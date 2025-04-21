def flatten_v1(obj):
    result = []
    if isinstance(obj, int):
        return [obj]
    else:
        for i in obj:
            result += flatten_v1(i)
        return result


def flatten_v2(obj):
    if isinstance(obj, int):
        return [obj]
    else:
        result = []
        for i in obj:
            result += flatten_v2(i)
        return result


if __name__ == "__main__":
    nested = [1, [2, [3, [4]], 5], [[6]], 7]
    
    print("Flatten v1:", flatten_v1(nested))
    print("Flatten v2:", flatten_v2(nested))
    print("Equal outputs?", flatten_v1(nested) == flatten_v2(nested))


def uppers(list: l):
    return [item for item in l if upper(item)]

def nested_list_contains(obj: int | list, item: int) -> bool:
    contains = False 
    if isinstance(obj, int):
        if obj == item:
            contains = True 
            return contains 
        return contains
    else:
        for k in obj:
            if nested_list_contains(k, item) == True:
                return True 
        return False  \
        

def items_at_depth(obj: int | list, depth: int) -> list[int]:
    curr = copy(depth)
    rlist = []
    if isinstance(obj, int):
        if curr > 0:
            return []
        return [obj]
    else:
        curr -= 1
        for items in obj:
            rlist.extend(items_at_depth(items, curr))
        return rlist
            

def add_one(obj: Union[int, list]) -> None:
    if isinstance(obj, int):
        return
    elif obj == []:
        return 
    else:
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                obj[i] += 1
            else:
                add_one(obj[i])
        return
    
def get_ith_item(obj: str | list, i: int) -> str | int:
    num = 0 
    if isinstance(obj, str):
        if i == 0:
            return obj
        else:
            return 1  # Counted one string, but not the ith
    else:
        num = 0 
        for item in obj:
            result = get_ith_item(item, i - num)
            if isinstance(result, str):
                return result  # Found the ith item
            else:
                num += 1     # Accumulate count
        return num  # Didn't find it, return total count

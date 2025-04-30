def sort_on(dict):
    return dict["num"]

def count_words(text):
    return len(text.split())

def count_characters(text):
    result = {}
    for x in text:
        val = x.lower()
        if val in result:
           result[val] = result[val] + 1
        else:
            result[val] = 1
    return result

def get_sorted_list(dict):
    list = []
    for k,v in dict.items():
        list.append({"char":k, "num":v})
    list.sort(reverse=True, key=sort_on)
    return list
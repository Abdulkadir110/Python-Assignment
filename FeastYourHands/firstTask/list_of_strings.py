


def convert_to_list_of_intergers(letter):
    return int(letter)

def get_map(list_strings) :
    map_list = list(map(convert_to_list_of_intergers, list_strings))
    return map_list



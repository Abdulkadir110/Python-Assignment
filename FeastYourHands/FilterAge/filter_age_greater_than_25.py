
def isGreater_than_25(dictionary):
    return dictionary['age'] > 25

def filter_out_ages_below25(dictionary):
    return list(filter(isGreater_than_25,dictionary))

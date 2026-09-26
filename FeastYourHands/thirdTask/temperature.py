
def toFahrenheit(celsius) :
    return round((celsius * 1.8 + 32), 2)

def getTheMapFor(temperatures):
    return list(map(toFahrenheit, temperatures))

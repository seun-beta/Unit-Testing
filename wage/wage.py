
def computepay(hours, rate):
    if hours < 0:
        raise ValueError('Working hours cannot be negative')
    else:
        if hours <= 40:
            wage = hours * rate
            return wage
        else:
            wage = (40*rate) + ((hours-40)*(1.5*rate))
            return wage

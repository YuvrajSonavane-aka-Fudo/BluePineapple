
#!calculate electricity bill

def calculate_ELECTRICITY_BILL(curMeter , prevMeter , tax , rate , fixedCharges):
    return ((curMeter - prevMeter) * rate)+ fixedCharges + tax



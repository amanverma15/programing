import math,random
def generateOTP():
    otp = ""
    for i in range(4):
        otp = otp + str(random.randint(1,9))
    return otp
result = generateOTP()
print(result)

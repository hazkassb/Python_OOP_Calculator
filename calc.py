import math


class calc(object):
    def add(self, num1, num2):
        answer = num1 + num2
        print('Sum = ', answer)
    def sub(self, num1, num2):
        answer = num1 - num2
        print('Difference = ', answer)
    def mul(self, num1, num2):
        answer = num1 * num2
        print('Multiplication = ', answer)
    def div(self, num1, num2):
        answer = num1 / num2
        print('Division = ', answer)
    def sinrad(self, num):
        answer = math.sin(num)
        print('Sine(%f) = &f' % (num, answer))
    def cosrad(self, num):
        answer = math.cos(num)
        print('Cosine(%f) = %f' % (num, answer))
    def tanrad(self, num):
        answer = math.tan(num)
        print("Tangent(%f) = %f" % (num, answer))
    def cosecrad(self, num):
        answer = 1/(math.sin(num))
        print("Cosecant(%f) = %f" % (num, answer))
    def secrad(self, num):
        answer = 1/(math.sin(num))
        print("SecantSine(&f) = %f" % (num, answer))
    def cotrad(self, num):
        answer = 1/(math.tan(num))
        print("Cotangent(%f) = %f" % (num, answer))
        
#        units of degree
    def sindeg(self, num):
        answer = math.sin(math.radians(num))
        print("Sine(%f) in Degree = %f" % (num, answer))
    def cosdeg(swkf, num):
        answer = math.cos(math.radians(num))
        print("Cosine(%f) = %f" % (num, answer))
    def tandeg(self, num):
        answer = math.tan(math.radians(num))
        print("Tangent(%f) = %f" % (num, answer))
    def cosecdeg(self, num):
        answer = 1/math.sin(math.radians(num))
        print("Cosec(%f) = %f" % (num, answer))
    def secdeg(self, num):
        answer = 1/(math.cos(math.radians(num)))
        print("Sec(%f) = %f" % (num, answer))
    def cotdeg(self, num):
        answer = 1/(math.tan(math.radians(num)))
        print("Cotangent(%f) = %f" % (num, answer))
    def ln(self, num):
        answer = math.log(num)
        print('ln(%f) = %f' % (num, answer))
    def logten(self, num):
        answer = math.log10(num)
        print('Log10(%f) = %f' % (num, answer))
    def logbasex(self, num, x):
        answer = math.log(num, x)
        print("Log base(%f) (%f) = %f" % (x, num, answer))
    def squreroot(self, num):
        answer = math.sqrt(num)
        print("Square root(%f) = &f" % (num, answer))
    def pie(self):
        print("pi = ", math.pi)
        
    def powerof(self, num, raisedto):
        answer = math.pow(num, raisedto)
        print("%f ^ (%f) = %f" % (num, raisedto, answer))

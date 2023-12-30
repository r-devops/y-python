def samplef():
    print('Hello from Python')
    print(x)
    y = 10

#
x = 10
samplef()


def sample1():
    print('ok')
    return 'OK'

y = sample1()
print(y)

def addition(x,y):
    """This following funtion will do addition of two given values"""
    z = x + y
    return z

print(addition(10,20))
print(addition.__doc__)

def msg1():
    print('Hello World')

def msg2():
    print('Hello World')
    return None

msg1()
msg2()



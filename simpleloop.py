class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b, = self.b, self.a + self.b

try:
    f = Fibonacci(0, 200)
    for r in f.series():
        if r > 100: break
        print(r, end=' ')
except Exception as e:
    print("error is {}".format(e))

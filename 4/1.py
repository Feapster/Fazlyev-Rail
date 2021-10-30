import time


class Tamagochi:
    def __init__(self, name):
        self.name = name
        self.satiety = 100
        self.health = 100
        self.t_1 = time.time()
        self.t_2 = time.time()

    def check(self):
        self.t_1 = time.time()
        self.satiety -= int(self.t_1 - self.t_2)
        if self.satiety <= 0:
            self.health += int(self.satiety)
            self.satiety = 0
        self.t_2 = self.t_1
        if self.health <= 0:
            print("Dead")
        else:
            print("Health =", self.health)
            print("Satiety =", self.satiety)
            print(time.ctime())
            return "________________________"

    def feed(self):
        if self.health <= 0:
            pass
        else:
            self.satiety = 100


T_1 = Tamagochi("Peter")

print(T_1.name)

for i in range(8):
    print(T_1.check())
    time.sleep(30)
    if i % 4 == 0:
        T_1.feed()

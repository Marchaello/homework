mport random

class cat:
    def __init__(self):
        self.life = 100
        self.hung = 50
        self.mood = 50
        self.tired = 50

    def is_alive(self):
        if self.life <= 0:
            self.is_alive = False
            print("you dead!")

    def damage(self):
        if self.hung <= 10 and self.hung > 0:
            self.life -= 3
            self.mood -= 5
        elif self.hung < 0:
            self.life -= 12
            self.mood -= 15

    def sleep(self):
        self.tired += 30
        self.life += 12
        self.mood += 10
        self.hung -= 10

    def feed(self):
        self.hung -= 12

    def go_dump(self):
        luck = random.randint(1, 100)
        if luck <= 25:
            self.life -= 10
            print(f"You got poisoned!")
            self.tired -= 12
            self.hung -= 15
        else:
            self.hung += random.randint(20, 30)
            self.tired -= 10
            self.life += 10

    def tiredness(self):
        if self.tired <= 15:
            self.mood -= 8

    def depresion(self):
        if self.mood <= 10:
            self.tired -= 10

    def begging(self):
        luck = random.randint(1, 100)
        if luck <= 15:
            self.life -= 15
            print(f"You got hurted!")
            self.tired -= 20
            self.hung -= 12
        elif 12 < luck <= 35:
            print("You got nothing =(")
            self.tired -= 15
            self.hung -= 8
        elif luck >= 99:
            self.is_alive = False
            print("Someone sheltered you!!")
        else:
            self.hung += random.randint(34, 50)
            self.life += 17

    def show_stats(self):
        print(f"Your cat have {self.life} of health, {self.hung} satiety, {self.mood} mood and {self.tired} tiredness!")

    def cats_life(self):
        kube = random.randint(1, 4)
        if kube == 1:
            self.sleep()
        elif kube == 2:
            self.go_dump()
        else:
            self.begging()
        self.damage()
        self.feed()
        self.tiredness()
        self.depresion()
        self.is_alive()
        self.show_stats()
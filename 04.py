class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
            if self.hungry:
                print('Ahhhhhhhh....')
                self.hungry = False
            else:
                print('NO!thanks!')
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'SQUALLLL'
    def sing(self):
        print(self.sound)
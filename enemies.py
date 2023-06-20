

class Enemy:
    def __init__(self, form, hit_box, vision_box, health, damge, en_x, en_y):
        self.form = form
        self.hit_box = hit_box
        self.vision_box = vision_box
        self.health = health
        self.damge = damge
        self._en_x = en_x
        self._en_y = en_y

    @property
    def en_x(self):
        return self._en_x
    
    @en_x.setter #Setter
    def en_x(self, x):
        self._en_x = x

    @property
    def en_y(self):
        return self._en_y
    
    @en_y.setter #Setter
    def en_y(self, y):
        self._en_y = y         



def generate_enemy(en_x, en_y, hit_box, vision_box, health, damge):
    enemy = Enemy(None, hit_box, vision_box, health, damge, en_x, en_y)
    return enemy
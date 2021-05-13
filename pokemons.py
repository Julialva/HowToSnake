class Pokemon(object):
    def __init__(self, nome ='',id=None):
        self.nome = nome
        self.id = id
        self.golpes = []
    def atribui_hp(self,health_points=39):
        self.hp = int(health_points)
    def atribui_at(self,attack_points=52):
        self.at = int(attack_points)
    def atribui_df(self,defense_points=43):
        self.df = int(defense_points)
    def atribui_sp_at(self,speed_attack=60):
        self.sp_at = int(speed_attack)
    def atribui_sp_df(self,speed_defense=50):
        self.sp_df = int(speed_defense)
    def atribui_sp(self,speed_points=65):
        self.sp = int(speed_points)
    def atribui_golpes(self,golpe):
        if len(self.golpes) < 4:
            self.golpes.append(str(golpe))
        else:
            x = str(input('Deseja remover um golpe? [S/N]: ')).upper()
            if x == 'S':
                print(self.golpes)
                y = int(input('qual dos golpes você deseja remover? [1,2,3,4]: '))
                y = y-1
                self.golpes[y] = golpe
    def info(self):
        print('O nome deste pokemon é {0}, ele tem id {1} e seus golpes são {2}.'.format(self.nome,self.id,self.golpes))


charmander = Pokemon('charmander',id=5)
charmander.atribui_hp(51)
charmander.atribui_at(56)
charmander.atribui_df(58)
charmander.atribui_sp(50)
charmander.atribui_sp_at(51)
charmander.atribui_sp_df(59)
charmander.atribui_golpes('Scratch')
charmander.atribui_golpes('Growl')
charmander.atribui_golpes('Ember')
charmander.atribui_golpes('Smokescreen')
charmander.atribui_golpes('DragonBreath')
charmander.info()
print(charmander.hp,charmander.at,charmander.df,charmander.sp,charmander.sp_at,charmander.sp_df)

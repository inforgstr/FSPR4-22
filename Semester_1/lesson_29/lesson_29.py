def get_user_info(name, clan='Trident', *args, **kwargs):
    if args:
        args = ''.join([f'\n- {arg}' for arg in args])
        kwargs = ''.join([f'\n- {i}:{val}' for i, val in kwargs.items()])
        return f'Your name is {name} and your clan is {clan}. Other information:{args}\n\nKey skills:{kwargs}'
    else:
        return f'Your name is {name} and your clan is {clan}.'

print(get_user_info('Behruz'))
print(get_user_info('Behruz', 'Shunko'))
print(get_user_info('Behruz', 'Shunko', 'sonic speed', 'lightning', 'programming', db='SQL'))

class Artist:
    def __init__(self, paper, pencil, kraska, kistochka):
        self.paper = paper
        self.pencil = pencil
        self.kraska = kraska
        self.kistochka = kistochka

    @classmethod
    def override_init(cls, paper, pencil):
        return cls(paper, pencil, 'VALE', 'HALE')
    
    def draw(self):
        return f'Some random masterpiece with {self.kistochka}'

artist = Artist('tarshon', 'cherni', 'kraski', 'belka')
print(artist.draw())
artist = Artist.override_init('KL', 'Jfd')
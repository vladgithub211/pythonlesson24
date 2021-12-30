class Human:
    def info(self,n):

        for i in range(n):
            print(f'{self.name}')
p1=Human()
p1.name='Yarik'
p1.surname='Glad'
p1.age=15
p1.place_of_birth='UA'


p2=Human()
p2.name='Dana'
p2.surname='Genina'
p2.age='15?'
p2.place_of_birth='UA'


p1.info(2)
p2.info(5)

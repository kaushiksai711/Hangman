import random as rd
e=[chr(i) for i in range(97,123)]
class Inputss:
    def inputs(self):
        self.c=input("enter your word")
        self.c=[i.lower() for i in self.c]
        self.d=[i.lower() for i in self.c]
        self.a=self.d
    def guess_word(self):
        self.c=rd.choice(['Abjure','Future','Picnic','Agonistic','Garland','Protect','Airline','Gigantic','Publish','Bandit','Goofy','Quadrangle','Banquet','Government','Recount','Binoculars','Grandnieces','Redoubtable','Biologist','Handbook','Reflection','Blackboard','Himself','Reporter','Board','Indulge','Ring','Bookworm','Inflatable','Salesclerk','Butterscotch','Inimical','Snapshot','Camera','Interim','Shellfish','Campus','Invest','Ship','Catfish','Jackpot','Significance','Carsick','Kitchenette','Sometimes','Celebrate','Law','Sublime','Celery','Life','Tabletop','Citizen','Lifeline','Teamwork','Coloring','Love','Tennis','Compact','Magnificent','Timesaving','Dark','Malevolence','Tree','Damage','Man','Termination','Dangerous','Mascot','Underestimate','Decorum','Marshmallow','Vineyard','Endorse','Mine','War','Engender','Moonwalk','Way','Erratic','Near','Wealth','Envelope','Nephogram','Wednesday','Etymology','Newborn','World','Eyewitness','Noisome','Xerox','Eulogy','Owl','You','Fish','Parenthesis','Zestful','Food','Perpetrator','Foreclose','Phone'])
        self.c=[i.lower() for i in self.c]
        self.d=[i.lower() for i in self.c]
        self.a=self.d
    def letter(self):
        count=0
        while True:
            i=rd.choice(e)
            if i not in self.a:
                self.a.append(i)
                count+=1
            if count==10:
                self.a=set(self.a)
                self.a=list(self.a)
                break
        self.b=['_' for i in range(len(self.c))]
    def display(self):
        print("give one char at a time")
        count=0
        print(f'guess it \n')
        while True:
            count+=1
            print(self.b)
            print( self.a[:len(self.a)//3],sep=' ')
            print( self.a[len(self.a)//3:2*len(self.a)//3],sep=' ')
            print( self.a[2*len(self.a)//3:],sep=' ')
            z=input("give a char")
            if z in self.c:
                for i in range(len(self.c)):
                    if z==self.c[i]:
                        self.b[i]=z
            else:
                print("too bad wrong guess")
            self.a.remove(z)
            if '_'not in self.b:
                print("".join(self.b))
                print("congrats u guessed it")
                break;
            elif count==len(self.c)+7:
                print("you died")
                break;
while True:
    print('hangman the game')
    print('select one of following')
    g=input("1.give a word    2.guess a word")
    t=Inputss()
    if g=='1':
        t.inputs()
    if g=='2':
        t.guess_word()
    t.letter()
    t.display()
    s=input("contin")
    if s=='no':
        break;
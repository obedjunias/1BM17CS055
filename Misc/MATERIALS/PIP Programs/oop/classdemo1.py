class Hero : #de f ine a c l a s s o b j e c t
    def setName (self , value ) : #de f ine c l a s smethods
        self.name = value #s e l f i d e n t i f i e s apar t i cul a r instance
    def display (self) :
        print (self.name)

x = Hero ( )
y = Hero ( )
z = Hero ( )

x. setName ( "Arthur , King of the Britons " )
y. setName ( " Sir Lancelot , the Brave " )
z. setName ( " Sir Robin , the Not−Quite−So−Brave− As−Sir−Lancelot " )
x.display()
y.display()
z.display()

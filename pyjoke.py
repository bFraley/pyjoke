import os

class PyJoke:
    def __init__(self, amt, forever):
        self.amt = amt
        self.forever = forever
        self.cmds = ['clear', 'python', 'python pyjoke.py']
        
    def start(self):
        for i in range(self.amt):
            for cmd in self.cmds[:2]:
                os.system(cmd)

        if self.forever:
            os.system(self.cmds[-1])
           
     
joke = PyJoke(5, True)
joke.start()


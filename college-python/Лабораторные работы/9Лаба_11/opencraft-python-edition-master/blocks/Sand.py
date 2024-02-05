from blocks.Block import Block
#from ursina import *

class Sand(Block):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.texture='assets/blocks/sand.png'

    def update(self):
        pass
        #gravity
        #ray=raycast(self.position+(.5,.5,.5),(0,-1,0),distance=.5, ignore=[self,])
        #if not ray.hit:
            #self.position-=(0,7*time.dt,0)
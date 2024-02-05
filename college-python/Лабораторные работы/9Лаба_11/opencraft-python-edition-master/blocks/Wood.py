from blocks.Block import Block

class Wood(Block):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.texture='assets/blocks/wood.png'
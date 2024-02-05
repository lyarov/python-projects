from ursina import *
import random

#entities
from entities.Player import Player

#blocks
from blocks.Dirt import Dirt
from blocks.Stone import Stone
from blocks.Wood import Wood
from blocks.Bricks import Bricks
from blocks.Gold import Gold
from blocks.Glass import Glass
from blocks.Sand import Sand

#-------------------------------------

app = Ursina()

#WINDOW SETTINGS
window.title="OpenCraft Python Edition"
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False
window.cog_button.visible = False

player=Player()

Sky(color=rgb(200,255,255))

def input(key):
        #MOUSE INPUT
        if key == 'left mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                #play break sound
                if str(mouse.hovered_entity)=='glass':
                    Audio('assets/sounds/blocks/break-glass.mp3',volume=player.volume, pitch=random.randint(8,12)/10) #turn these into functions???
                else:
                    #temporary break sound
                    Audio('assets/sounds/blocks/place.mp3',volume=player.volume, pitch=random.randint(8,12)/10)

                destroy(mouse.hovered_entity)

                #if u add entities, u will have to check 
                #whether the player clicked on anobject 
                #that inherits the Block class
                #in order to play the right 

        if key == 'right mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                position=hit_info.entity.position + hit_info.normal
                #!!!BUG!!!
                #IF THE PLAYER IS INSIDE OF A BLOCK
                #HE CAN PLACE MULTIPLE BLOCKS
                #IN THE SAME PLACE CAUSING FPS DROPS
                #------------------------------------
                #1ST CHECK IF THE BLOCK IS NOT GONNA
                #COLLIDE WITH THE PLAYER, THEN PLACE IT
                if player.currentBlock=='1':
                    Dirt(position.x, position.y, position.z)

                elif player.currentBlock=='2':
                    Stone(position.x, position.y, position.z)

                elif player.currentBlock=='3':
                    Wood(position.x, position.y, position.z)

                elif player.currentBlock=='4':
                    Bricks(position.x, position.y, position.z)

                elif player.currentBlock=='5':
                    Gold(position.x, position.y, position.z)

                elif player.currentBlock=='6':
                    Glass(position.x, position.y, position.z)

                elif player.currentBlock=='7':
                    Sand(position.x, position.y, position.z)

                #before adding new blocks, add new numbers in player input (choosing a block)
                #add a menu for choosing blocks

                #if u add mobs, u will have to check 
                #whether the player clicked on an 
                #object that inherits from the Block class
                #in order to play the right sound

                #play place sound
                Audio('assets/sounds/blocks/place.mp3',volume=player.volume, pitch=random.randint(8,12)/10)

#GENERATE WORLD
for i in range(21):
    for j in range(21):
        Dirt(i-10,0,j-10)

#LIGHT
DirectionalLight(parent=Entity(), y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()

#----------TODO----------
#render distance, change with cmd
#quality0 - switch to gold_old and disable matcap shader
#do not render blocks that are not visible
#level of detail

#2D ITEMS
#ITEM LIST []
#IN MAIN UPDATE ITEM.ROTATION=PLAYER.ROTATION

#------------------------

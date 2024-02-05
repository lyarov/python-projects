from ursina import *

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.xhair = Entity(parent=camera.ui, model='circle', color=rgb(0,255,0), scale=.005)
        
        self.speed = 5
        self.height = 2

        self.currentBlock='1'

        #cmd
        self.cmd = Text(text='/', scale=0, x=-.86, y=-.447)
        self.cmdIsOn = False
        self.bgColor = rgb(0,0,0)

        #sound
        self.volume = 1

        #camera
        self.camera_pivot = Entity(parent=self, y=self.height)
        camera.parent = self.camera_pivot
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90

        #mouse
        mouse.locked = True
        mouse.visible=False
        self.mouse_sensitivity = 110

        #physics
        self.canMove=True
        self.gravity = 1
        self.grounded = False
        self.jump_height = 2
        self.jump_up_duration = .5
        self.fall_after = .35 # will interrupt jump up
        self.jumping = False
        self.air_time = 0

        self.traverse_target = scene     # by default, it will collide with everything. change this to change the raycasts' traverse targets.
        self.ignore_list = [self, ]

        # make sure we don't fall through the ground if we start inside it
        '''if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)
            if ray.hit:
                self.y = ray.world_point.y'''

    def update(self):
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity

        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity
        self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)

        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()

        feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
        head_ray = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
        if not feet_ray.hit and not head_ray.hit:
            move_amount = self.direction * time.dt * self.speed

            if raycast(self.position+Vec3(-.0,1,0), Vec3(1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[0] = min(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(-1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[0] = max(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[2] = min(move_amount[2], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,-1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[2] = max(move_amount[2], 0)
            if self.canMove:
                self.position += move_amount

            # self.position += self.direction * self.speed * time.dt

        if self.gravity:
            # gravity
            ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=self.ignore_list)

            if ray.distance <= self.height+.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity

    def cmdWrite(self, key):
        self.cmd.text+=key
        self.cmd.create_background(color=self.bgColor)
 
    def input(self, key):
        #KEYBOARD INPUT
        if key == 'space' and not self.cmdIsOn:
            self.jump()

        if key == 'escape':
            quit()

        if key in ('1', '2', '3', '4', '5', '6', '7'):
            self.currentBlock = key

        #cmd
        if key == '/':
            self.cmdIsOn=not self.cmdIsOn
            if self.cmdIsOn:
                self.canMove=False
                self.cmd.scale=1
                self.cmd.create_background(color=self.bgColor)
            else:
                self.canMove=True
                self.cmd.scale=0
        #cmd typing
        if self.cmdIsOn:
            if key == 'enter':
                #--------------------COMMANDS--------------------

                #mouse sensitivity
                if self.cmd.text.startswith('/msens '):
                    if(self.cmd.text[7:].isdigit()):
                        self.mouse_sensitivity=float(self.cmd.text[7:])

                #show/hide fps
                elif self.cmd.text=='/fps':
                    window.fps_counter.enabled=not window.fps_counter.enabled

                #change fov
                elif self.cmd.text.startswith('/fov '):
                    if(self.cmd.text[5:].isdigit()):
                        camera.fov=float(self.cmd.text[5:])

                #change volume
                elif self.cmd.text.startswith('/vol '):
                    if(self.cmd.text[5:].isdigit()):
                        self.volume=int(self.cmd.text[5:])

                #crosshair scale
                elif self.cmd.text.startswith('/xhairs '):
                    if(self.cmd.text[8:].isdigit()):
                        self.xhair.scale=float(self.cmd.text[8:])/1000

                #crosshair color
                elif self.cmd.text.startswith('/xhairc '):
                    color=self.cmd.text[8:].split(sep=None)
                    self.xhair.color=rgb(int(color[0]),int(color[1]),int(color[2]))
                #------------------------------------------------
                self.canMove=True
                self.cmd.text='/'
                self.cmdIsOn=False
                self.cmd.scale=0
                self.cmd.background=None
            elif key == 'backspace':
                if self.cmd.text[-1]!='/':
                    self.cmd.text=self.cmd.text[:-1]
                    self.cmd.create_background(color=self.bgColor)
                else:
                    self.canMove=True
                    self.cmdIsOn=False
                    self.cmd.scale=0
            elif key == 'space':
                self.cmd.text+=' '
                self.cmd.create_background(color=self.bgColor)
            elif key.isalnum() or key == '.' or key == ',':
                self.cmdWrite(key)

    def jump(self):
        if not self.grounded:
            return

        self.grounded = False
        self.animate_y(self.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)

    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False

    def land(self):
        self.air_time = 0
        self.grounded = True

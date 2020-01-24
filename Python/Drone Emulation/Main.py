import pyglet
from pyglet import clock
from pyglet.window import key
from pyglet.gl import *
from Asset_loader import Asset_Loader
from Drone import Drone
# forward tilt down backwards tilt up
class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__(640,480, resizable=False,config =  pyglet.gl.Config(double_buffer = True),
                                   fullscreen=False, caption="Player Movement")
        self.size = self.get_size()
        self.main_batch = pyglet.graphics.Batch()
        self.on_draw = self.event(self.on_draw)
        self.load_assets()
        
    def load_assets(self):
        """load and create player sprite and a tile"""
        self.asset_loader = Asset_Loader("./Assets")
        self.drone_img = self.asset_loader.load_image("Drone.png",(64,64),True)
        self.thruster_still = self.asset_loader.load_image("Thruster_still.png",(32,32),True)
        self.thruster_forward = self.asset_loader.load_image("Thruster_forward.png",(32,32),True)
        self.drone = Drone(self.drone_img,self.thruster_still,self.thruster_forward,
                           x=self.size[0]//2 , y =self.size[1]//2,batch = self.main_batch)
        self.game_object = [self.drone]
        
        pyglet.clock.schedule_interval(self.update,1/60)

    def center_image(self,image):
        """Sets an image's achor point to its center"""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def on_draw(self):
        self.clear()
        self.drone.thrusters_batch.draw()
        self.main_batch.draw()
        
        #self.world_camera.position = (int(self.player.pos_vector[0]-self.world[0]/2),int(self.player.pos_vector[1]-self.world[1]/2))
             
    def on_key_press(self,symbol,modifiers):
        if symbol == key.ESCAPE:
            self.close()
        if symbol == key.W:
            
            #print(self.drone.vel_vector)
            self.drone.vel_vector[1] += self.drone.speed
            
        if symbol == key.A:
            self.drone.vel_vector[0] += -self.drone.speed
        if symbol == key.S:
            self.drone.vel_vector[1] += -self.drone.speed
        if symbol == key.D:
            self.drone.vel_vector[0] += self.drone.speed
        
    def on_key_release(self,symbol, modifiers):
        if symbol == key.W:
            self.drone.vel_vector[1] += -self.drone.speed
        if symbol == key.A:
            self.drone.vel_vector[0] += self.drone.speed
        if symbol == key.S:
            self.drone.vel_vector[1] += self.drone.speed
        if symbol == key.D:
            self.drone.vel_vector[0] += -self.drone.speed

    def update(self,dt):
        for obj in self.game_object:
            obj.update(dt)


        
            
if __name__ == '__main__': 
    
    window = Game()
    
    pyglet.app.run()

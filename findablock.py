import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat("Go find the block")

from random import randint
p = mc.player.getTilePos()
x = p.x + randint(-20, 20)
y = p.y + randint(-5, 5)
z = p.z + randint(-20, 20)
mc.setBlock(x, y, z, block.GOLD_BLOCK.id)

from gpiozero import LED, Buzzer
from time import sleep
led = LED(24)
buzz = Buzzer(17)
led.on()
buzz.on()
sleep(1)
led.off()
buzz.off()

from math import sqrt
dist = 0
gameover = False
while gameover == False:
    p = mc.player.getTilePos()
    xd = p.x - x
    yd = p.y - y
    zd = p.z - z
    dist_now = sqrt((xd*xd) + (yd*yd) + (zd*zd))
    if dist_now > dist:
        buzz.on()
    else:
        buzz.off()
    dist = dist_now
    mc.postToChat(dist)
    if dist_now < 5:
        led.on()
    else:
        led.off()
    if dist_now <1.5:
        gameover = True()
        mc.postToChat("You got Gold")
        led.off()
        buzz.off()
    

#/usr/bin/env python
# Script which goes with gravity.launch, to simulate Hrp2 in the space with a spaceship from a movie and an emu character from Nasa.gov. See gravity_description package.

from hpp.gepetto import Viewer, PathPlayer
from hpp.corbaserver.emu import Robot
from hpp.corbaserver import ProblemSolver
from hpp.corbaserver import Client

robot = Robot ('emu')
ps = ProblemSolver (robot)
cl = robot.client
r = Viewer (ps)
pp = PathPlayer (cl, r)
#r.loadObstacleModel ("gravity_description","gravity_decor","gravity_decor") # visual
#r.loadObstacleModel ("gravity_description","stone","stone")

xStone = 10
yEmu = 5+0.2
zEmu = 6-1
robot.setJointBounds('base_joint_xyz', [xStone-2, xStone+2, yEmu-1, yEmu+2, zEmu-0.5, zEmu+0.5])
# List of configs
q1 = [xStone+2, yEmu+0, zEmu, 1.0, 0.0, 0.0, 0.0]
q2 = [xStone+1.5, yEmu+0.8, zEmu, 0.707106781, 0, 0, 0.707106781]
q3 = [xStone+1, yEmu+1.4, zEmu, 0, 0, 0, 1]
q4 = [xStone+0.5, yEmu+1.7, zEmu, -0.707106781, 0, 0, 0.707106781]
#q5 = [xStone+0, yEmu+2, zEmu, -1, 0, 0, 0]
q5 = [xStone+0, yEmu+2, zEmu, -0.99, 0.14003571, 0.013, 0.011]
q6 = [xStone-0.5, yEmu+1.7, zEmu, -0.707106781, 0, 0, -0.707106781]
q7 = [xStone-1, yEmu+1.4, zEmu, 0, 0, 0, -1]
q8 = [xStone-1.5, yEmu+0.8, zEmu, 0.707106781, 0, 0, -0.707106781]
q9 = [xStone-2, yEmu+0, zEmu, 1, 0, 0, 0]
r(q1)
robot.isConfigValid(q1)

ps.setInitialConfig (q1); ps.addGoalConfig (q2); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q2); ps.addGoalConfig (q3); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q3); ps.addGoalConfig (q4); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q4); ps.addGoalConfig (q5); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q5); ps.addGoalConfig (q6); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q6); ps.addGoalConfig (q7); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q7); ps.addGoalConfig (q8); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q8); ps.addGoalConfig (q9); ps.solve (); ps.resetGoalConfigs ()
ps.setInitialConfig (q1); ps.addGoalConfig (q9); ps.solve (); ps.resetGoalConfigs ()

nInitialPath = ps.numberPaths()-1 #8
ps.pathLength(nInitialPath)

#ps.addPathOptimizer('RandomShortcut') #9
#ps.optimizePath (nInitialPath)
#ps.pathLength(ps.numberPaths()-1)

#ps.clearPathOptimizers()
ps.addPathOptimizer("GradientBased")
ps.optimizePath (nInitialPath)
ps.numberPaths()
ps.pathLength(ps.numberPaths()-1)

pp(ps.numberPaths()-1)


r(ps.configAtParam(0,2))
ps.getWaypoints (0)

# Add light to scene
lightName = "li"
r.client.gui.addLight (lightName, r.windowId, 0.001, [0.4,0.4,0.4,0.5])
r.client.gui.addToGroup (lightName, r.sceneName)
r.client.gui.applyConfiguration (lightName, [xStone,yEmu-0.5,zEmu,1,0,0,0])
r.client.gui.refresh ()
lightName = "li2"
r.client.gui.addLight (lightName, r.windowId, 0.001, [0.4,0.4,0.4,0.5])
r.client.gui.addToGroup (lightName, r.sceneName)
r.client.gui.applyConfiguration (lightName, [xStone-2,yEmu+0.5,zEmu,1,0,0,0])
r.client.gui.refresh ()
lightName = "l3"
r.client.gui.addLight (lightName, r.windowId, 0.001, [0.4,0.4,0.4,0.5])
r.client.gui.addToGroup (lightName, r.sceneName)
r.client.gui.applyConfiguration (lightName, [xStone+2,yEmu+0.5,zEmu,1,0,0,0])
r.client.gui.refresh ()


## Video recording
pp.dt = 0.01
pp.speed = 1.5
r.startCapture ("capture","png")
#pp(1)
pp(ps.numberPaths()-1)
r.stopCapture ()

## ffmpeg commands
ffmpeg -r 50 -i capture_0_%d.png -r 25 -vcodec libx264 video.mp4
x=0; for i in *png; do counter=$(printf %03d $x); ln "$i" new"$counter".png; x=$(($x+1)); done
ffmpeg -r 50 -i new%03d.png -r 25 -vcodec libx264 video.mp4


# Load obstacles in HPP
cl.obstacle.loadObstacleModel('gravity_description','gravity_decor','')
cl.obstacle.loadObstacleModel('gravity_description','emu','')

## DEBUG commands
cl.obstacle.getObstaclePosition('obstacle_base')
cl.robot.getJointOuterObjects('CHEST_JOINT1')
cl.robot.getCurrentConfig()
cl.robot.setCurrentConfig(q3)
cl.robot.collisionTest()
res = cl.robot.distancesToCollision()
cl.problem.pathLength(2)
r( cl.problem.configAtDistance(1,5) )
cl.problem.optimizePath (1)
cl.problem.clearRoadmap ()
cl.problem.resetGoalConfigs ()
robot.getJointNames ()


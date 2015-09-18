#/usr/bin/env python
# Script which goes with gravity.launch, to simulate Hrp2 in the space with a spaceship from a movie and an emu character from Nasa.gov. See gravity_description package.

from hpp.gepetto import Viewer, PathPlayer
from hpp.corbaserver.hrp2 import Robot
from hpp.corbaserver import ProblemSolver
from hpp.corbaserver import Client

#Robot.urdfSuffix = '_capsule'
#Robot.srdfSuffix= '_capsule'
robot = Robot ('hrp2_14')
#robot.setJointBounds('base_joint_xyz', [-5, 10, -10, 10, -5, 5])
robot.setJointBounds('base_joint_xyz', [-3, 10, -4, 4, -3, 5])
ps = ProblemSolver (robot)
cl = robot.client
r = Viewer (ps)
pp = PathPlayer (cl, r)
#r.loadObstacleModel ("gravity_description","emu","emu")
r.loadObstacleModel ("gravity_description","gravity_decor","gravity_decor")

# Difficult init config
q1 = [1.45, 1.05, -0.8, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.8, 1.0, -1.0, -0.85, 0.0, -0.65, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -1.9, 0.0, -0.6, -0.3, 0.7, -0.4, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, 0.1, -0.15, -0.1, 0.3, -0.418879, 0.0, 0.0, 0.3, -0.8, 0.3, 0.0, 0.0]

q2 = [6.55, -2.91, 1.605, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 1.0, -0.4, -1.0, 0.0, -0.2, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -1.5, -0.2, 0.1, -0.3, 0.1, 0.1, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -0.2, 0.6, -0.453786, 0.872665, -0.418879, 0.2, -0.4, 0.0, -0.453786, 0.1, 0.7, 0.0]

q2hard = [7.60, -2.41, 0.545, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, 0.0, -0.4, -0.55, 0.0, -0.6, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -2.8, 0.0, 0.1, -0.2, -0.1, 0.4, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -0.2, 0.6, -0.1, 1.2, -0.4, 0.2, -0.3, 0.0, -0.4, 0.2, 0.7, 0.0]

robot.isConfigValid(q1)
robot.isConfigValid(q2)

# qf should be invalid
qf = [1, -3, 3, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 1.0, -0.4, -1.0, 0.0, -0.2, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -1.5, -0.2, 0.1, -0.3, 0.1, 0.1, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -0.2, 0.6, -0.453786, 0.872665, -0.418879, 0.2, -0.4, 0.0, -0.453786, 0.1, 0.7, 0.0]
robot.isConfigValid(qf)

ps.setInitialConfig (q1); ps.addGoalConfig (q2); ps.solve ()

ps.solve ()
ps.pathLength(0)

ps.addPathOptimizer('RandomShortcut')
ps.optimizePath (0)
ps.pathLength(1)

ps.clearPathOptimizers()
ps.addPathOptimizer("GradientBased")
ps.optimizePath (0)
ps.numberPaths()
ps.pathLength(ps.numberPaths()-1)

pp(ps.numberPaths()-1)


r(ps.configAtParam(0,2))
ps.getWaypoints (0)


# Add light to scene
lightName = "li4"
r.client.gui.addLight (lightName, r.windowId, 0.01, [0.4,0.4,0.4,0.5])
r.client.gui.addToGroup (lightName, r.sceneName)
r.client.gui.applyConfiguration (lightName, [1,0,0,1,0,0,0])
r.client.gui.refresh ()


## Video recording
pp.dt = 0.02
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

# Initial (q1) and final (q2) more simple configurations :
q1 = [0, 0.01, 0.705, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.8, 0.8, -1.0, -1.0, 0.0, 0.2, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, 0.7, -0.8, 0.1, -0.523599, 0.1, -0.3, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, 0.6, 0.1, -0.453786, 0.872665, -0.418879, 0.2, -0.4, 0.0, -0.453786, 0.1, 0.7, 0.0]
q2 = [6.55, -2.91, 1.605, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 1.0, -0.4, -1.0, 0.0, -0.2, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -1.5, -0.2, 0.1, -0.3, 0.1, 0.1, 0.174532, -0.174532, 0.174532, -0.174532, 0.174532, -0.174532, -0.2, 0.6, -0.453786, 0.872665, -0.418879, 0.2, -0.4, 0.0, -0.453786, 0.1, 0.7, 0.0]


from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

LShoulderPitch = robot.getDevice('LShoulderPitch')
RShoulderPitch = robot.getDevice('RShoulderPitch')
LShoulderRoll = robot.getDevice('LShoulderRoll')
RShoulderRoll = robot.getDevice('RShoulderRoll')
HeadYaw = robot.getDevice('HeadYaw')

for i in range(100):
    robot.step(timestep)

print("MOVEMENT 1")
LShoulderPitch.setPosition(-1.2)
RShoulderPitch.setPosition(-1.2)
for i in range(100):
    robot.step(timestep)

LShoulderPitch.setPosition(0.0)
RShoulderPitch.setPosition(0.0)
for i in range(100):
    robot.step(timestep)

print("MOVEMENT 2")
LShoulderRoll.setPosition(1.0)
RShoulderRoll.setPosition(-1.0)
HeadYaw.setPosition(0.8)
for i in range(100):
    robot.step(timestep)

LShoulderRoll.setPosition(0.0)
RShoulderRoll.setPosition(0.0)
HeadYaw.setPosition(0.0)
for i in range(100):
    robot.step(timestep)

print("MOVEMENT 3")
LShoulderPitch.setPosition(-0.8)
RShoulderPitch.setPosition(-0.8)
LShoulderRoll.setPosition(0.5)
RShoulderRoll.setPosition(-0.5)
for i in range(100):
    robot.step(timestep)

print("DONE")

while robot.step(timestep) != -1:
    pass
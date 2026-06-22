from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

LShoulderPitch = robot.getDevice('LShoulderPitch')
RShoulderPitch = robot.getDevice('RShoulderPitch')
LShoulderRoll = robot.getDevice('LShoulderRoll')
RShoulderRoll = robot.getDevice('RShoulderRoll')
LElbowRoll = robot.getDevice('LElbowRoll')
RElbowRoll = robot.getDevice('RElbowRoll')
LElbowYaw = robot.getDevice('LElbowYaw')
RElbowYaw = robot.getDevice('RElbowYaw')
HeadYaw = robot.getDevice('HeadYaw')
HeadPitch = robot.getDevice('HeadPitch')
LHipRoll = robot.getDevice('LHipRoll')
RHipRoll = robot.getDevice('RHipRoll')

def wait(steps):
    for _ in range(steps):
        robot.step(timestep)

def reset():
    LShoulderPitch.setPosition(0.0)
    RShoulderPitch.setPosition(0.0)
    LShoulderRoll.setPosition(0.0)
    RShoulderRoll.setPosition(0.0)
    LElbowRoll.setPosition(0.0)
    RElbowRoll.setPosition(0.0)
    LElbowYaw.setPosition(0.0)
    RElbowYaw.setPosition(0.0)
    HeadYaw.setPosition(0.0)
    HeadPitch.setPosition(0.0)
    LHipRoll.setPosition(0.0)
    RHipRoll.setPosition(0.0)
    wait(50)

wait(50)

print("MOVEMENT 1: Arms Up")
LShoulderPitch.setPosition(-1.2)
RShoulderPitch.setPosition(-1.2)
LShoulderRoll.setPosition(0.4)
RShoulderRoll.setPosition(-0.4)
wait(70)
reset()

print("MOVEMENT 2: Side Lean")
LHipRoll.setPosition(0.2)
RShoulderRoll.setPosition(-0.7)
HeadYaw.setPosition(-0.4)
wait(60)
reset()

RHipRoll.setPosition(-0.2)
LShoulderRoll.setPosition(0.7)
HeadYaw.setPosition(0.4)
wait(60)
reset()

print("MOVEMENT 3: Clap Pose")
LShoulderPitch.setPosition(-0.5)
RShoulderPitch.setPosition(-0.5)
LElbowRoll.setPosition(-0.8)
RElbowRoll.setPosition(0.8)
HeadPitch.setPosition(-0.2)
wait(70)
reset()

print("MOVEMENT 4: Elbow Twist")
LShoulderPitch.setPosition(-0.9)
RShoulderPitch.setPosition(-0.9)
LElbowYaw.setPosition(-1.0)
RElbowYaw.setPosition(1.0)
HeadPitch.setPosition(0.2)
wait(70)
reset()

print("MOVEMENT 5: Head Bop and Swing")
LShoulderPitch.setPosition(-1.0)
LShoulderRoll.setPosition(0.5)
HeadYaw.setPosition(-0.5)
wait(40)
reset()

RShoulderPitch.setPosition(-1.0)
RShoulderRoll.setPosition(-0.5)
HeadYaw.setPosition(0.5)
wait(40)
reset()

LShoulderPitch.setPosition(-1.2)
RShoulderPitch.setPosition(-1.2)
LShoulderRoll.setPosition(0.3)
RShoulderRoll.setPosition(-0.3)
HeadYaw.setPosition(0.0)
HeadPitch.setPosition(-0.2)
wait(50)
reset()

print("DANCE COMPLETE!")

while robot.step(timestep) != -1:
    pass
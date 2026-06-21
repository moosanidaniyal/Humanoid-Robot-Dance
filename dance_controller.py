from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

LShoulderPitch = robot.getDevice('LShoulderPitch')
RShoulderPitch = robot.getDevice('RShoulderPitch')
LShoulderRoll = robot.getDevice('LShoulderRoll')
RShoulderRoll = robot.getDevice('RShoulderRoll')
LElbowRoll = robot.getDevice('LElbowRoll')
RElbowRoll = robot.getDevice('RElbowRoll')
HeadYaw = robot.getDevice('HeadYaw')
HeadPitch = robot.getDevice('HeadPitch')
LHipRoll = robot.getDevice('LHipRoll')
RHipRoll = robot.getDevice('RHipRoll')
LKneePitch = robot.getDevice('LKneePitch')
RKneePitch = robot.getDevice('RKneePitch')
LHipPitch = robot.getDevice('LHipPitch')
RHipPitch = robot.getDevice('RHipPitch')

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
    HeadYaw.setPosition(0.0)
    HeadPitch.setPosition(0.0)
    LHipRoll.setPosition(0.0)
    RHipRoll.setPosition(0.0)
    LKneePitch.setPosition(0.0)
    RKneePitch.setPosition(0.0)
    LHipPitch.setPosition(0.0)
    RHipPitch.setPosition(0.0)
    wait(60)

wait(50)

print("MOVEMENT 1: Arms Up")
LShoulderPitch.setPosition(-1.2)
RShoulderPitch.setPosition(-1.2)
LShoulderRoll.setPosition(0.5)
RShoulderRoll.setPosition(-0.5)
wait(80)
reset()

print("MOVEMENT 2: Side Lean")
LHipRoll.setPosition(0.3)
RShoulderRoll.setPosition(-0.8)
HeadYaw.setPosition(-0.5)
wait(70)
reset()

RHipRoll.setPosition(-0.3)
LShoulderRoll.setPosition(0.8)
HeadYaw.setPosition(0.5)
wait(70)
reset()

print("MOVEMENT 3: Clap Pose")
LShoulderPitch.setPosition(-0.5)
RShoulderPitch.setPosition(-0.5)
LElbowRoll.setPosition(-0.8)
RElbowRoll.setPosition(0.8)
HeadPitch.setPosition(-0.3)
wait(80)
reset()

print("MOVEMENT 4: Squat and Reach")
LHipPitch.setPosition(-0.4)
RHipPitch.setPosition(-0.4)
LKneePitch.setPosition(0.6)
RKneePitch.setPosition(0.6)
LShoulderPitch.setPosition(-1.4)
RShoulderPitch.setPosition(-1.4)
wait(90)
reset()

print("MOVEMENT 5: Head Bop and Swing")
# Swing 1: left arm up, head left
LShoulderPitch.setPosition(-1.0)
LShoulderRoll.setPosition(0.6)
HeadYaw.setPosition(-0.6)
HeadPitch.setPosition(-0.2)
wait(40)
reset()

RShoulderPitch.setPosition(-1.0)
RShoulderRoll.setPosition(-0.6)
HeadYaw.setPosition(0.6)
HeadPitch.setPosition(-0.2)
wait(40)
reset()

LShoulderPitch.setPosition(-1.3)
RShoulderPitch.setPosition(-1.3)
LShoulderRoll.setPosition(0.4)
RShoulderRoll.setPosition(-0.4)
HeadYaw.setPosition(0.0)
HeadPitch.setPosition(-0.3)
wait(60)
reset()

print("DANCE COMPLETE!")

while robot.step(timestep) != -1:
    pass
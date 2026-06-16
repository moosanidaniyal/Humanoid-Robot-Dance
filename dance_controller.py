from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

motor = robot.getDevice('LShoulderPitch')
motor.setPosition(0.5)

while robot.step(timestep) != -1:
    pass
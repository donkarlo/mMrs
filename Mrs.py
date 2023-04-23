from mMrs.Robot import Robot


class Mrs:
    def __init__(self, robots:list=None):
        self.__robots = robots

    def addRobot(self, robot:Robot):
        self.__robots.append(robot)

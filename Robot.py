from mMrs.sensor.Sensor import Sensor


class Robot:
    ''''''
    def __init__(self,robotId:int,sensors:list=None):
        self.__sensors = sensors
    def addSensor(self,sensor:Sensor):
        self.__sensors.append(sensor)
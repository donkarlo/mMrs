from mMrs.sensor.SensorType import SensorType


class Sensor:
    def __init__(self,sensorType:SensorType,sensorId:int,robotId:int,memLen:int):
        self.__vals = []
        pass

    def getLastVal(self):
        pass

    def pushVal(self,val):
        '''
        - remove the first val and push the new val to keep the len of sensor value
        - compute val

        Parameters
        ----------
        val

        Returns
        -------

        '''
        self.__removeFirstVal()
        pass

    def __removeFirstVal(self):
        pass
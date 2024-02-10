from threading import Event
# SMART class to monnitor soil conditions
class SMART:
    # Constructor
    def __init__(self, Name, deviceID, soil_moisture_threshold, soil_temp_threshold, soil_ph_threshold): 
        
        self._Name = "DEMO"
        self._deviceID = deviceID
        self._soil_moisture_threshold = soil_moisture_threshold
        self._soil_temp_threshold = soil_temp_threshold
        self._soil_ph_threshold = soil_ph_threshold
        self.soil_temp = None
        self._soil_moisture = None
        self._soil_temp = None
        self._soil_ph = None
        self._action = Event()

    # properties device Name
    @property
    def Name(self):
        return self._Name
    
    # Set device Name
    @Name.setter
    def Name(self, value):
        self._Name = value
    
    # properties device ID
    @property
    def deviceID(self):
        return self._deviceID
    
    # Set device ID
    @deviceID.setter
    def deviceID(self, value):
        self._deviceID = value

    # properties soil_moisture_threshold
    @property
    def soil_moisture(self):
        return self._soil_moisture
    
    # Set soil_moisture_threshold
    @soil_moisture.setter
    def soil_moisture(self, value):
        self._soil_moisture = value
        if self._soil_moisture < self._soil_moisture_threshold:
            self._action.set()
        else:
            self._action.clear()
    
    # properties soil_temp_threshold
    @property
    def soil_temp(self):
        return self._soil_temp
    
    # Set soil_temp_threshold
    @soil_temp.setter
    def soil_temp(self, value):
        self._soil_temp = value
        if self._soil_temp < self._soil_temp_threshold:
            self._action.set()
        else:
            self._action.clear()
    
    # properties soil_ph_threshold
    @property
    def soil_ph(self):
        return self._soil_ph
    
    # Set soil_ph_threshold
    @soil_ph.setter
    def soil_ph(self, value):
        self._soil_ph = value
        if self._soil_ph < self._soil_ph_threshold:
            self._action.set()
        else:
            self._action.clear()
    
    # properties action
    @property
    def action(self):
        return self._action
    
    def conditiion(self):
        return self._action.is_set()
    

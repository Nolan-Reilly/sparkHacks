from threading import Event
# SMART class to monitor soil conditions
class SMART:
    # Constructor
    def __init__(self, Name, deviceID,Email,soil_high_temp_threshold,soil_low_temp_threshold,
                 soil_high_moisture_threshold,soil_low_moisture_threshold,
                 soil_high_ph_threshold,soil_low_ph_threshold): 
        
        # Device properties
        self._Name = Name
        self._deviceID = deviceID
        self._Email = Email
        
        # Thresholds
        # soil temperature threshold
        self._soil_high_temp_threshold = soil_high_temp_threshold
        self._soil_low_temp_threshold = soil_low_temp_threshold

        # soil moisture threshold
        self._soil_high_moisture_threshold = soil_high_moisture_threshold
        self._soil_low_moisture_threshold = soil_low_moisture_threshold

        # soil ph threshold
        self._soil_high_ph_threshold = soil_high_ph_threshold
        self._soil_low_ph_threshold = soil_low_ph_threshold

        # soil conditions
        self._soil_temp = 45
        self._soil_moisture = 60
        self._soil_ph = 6
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
    
    # properties Email
    @property
    def Email(self):
        return self._Email
    
    # Set Email
    @Email.setter
    def Email(self, value):
        self._Email = value

    # properties soil_moisture_threshold
    @property
    def soil_high_moisture_threshold(self):
        return self._soil_high_moisture_threshold
    
    # Set soil_moisture_threshold
    @soil_high_moisture_threshold.setter
    def soil_high_moisture_threshold(self, value):
        self._soil_high_moisture_threshold = value

    #properties soil_low_moisture_threshold
    @property
    def soil_low_moisture_threshold(self):
        return self._soil_low_moisture_threshold
    
    # Set soil_low_moisture_threshold
    @soil_low_moisture_threshold.setter
    def soil_low_moisture_threshold(self, value):
        self._soil_low_moisture_threshold = value

    # properties soil_high_temp_threshold
    @property
    def soil_high_temp_threshold(self):
        return self._soil_high_temp_threshold
    
    # Set soil_high_temp_threshold
    @soil_high_temp_threshold.setter
    def soil_high_temp_threshold(self, value):
        self._soil_high_temp_threshold = value

    # properties soil_low_temp_threshold
    @property
    def soil_low_temp_threshold(self):
        return self._soil_low_temp_threshold
    
    # Set soil_low_temp_threshold
    @soil_low_temp_threshold.setter
    def soil_low_temp_threshold(self, value):
        self._soil_low_temp_threshold = value

    # properties soil_high_ph_threshold
    @property
    def soil_high_ph_threshold(self):
        return self._soil_high_ph_threshold
    
    # Set soil_high_ph_threshold
    @soil_high_ph_threshold.setter
    def soil_high_ph_threshold(self, value):
        self._soil_high_ph_threshold = value

    # properties soil_low_ph_threshold
    @property
    def soil_low_ph_threshold(self):
        return self._soil_low_ph_threshold
    
    # Set soil_low_ph_threshold
    @soil_low_ph_threshold.setter
    def soil_low_ph_threshold(self, value):
        self._soil_low_ph_threshold = value
    
    # properties soil_moisture
    @property
    def soil_moisture(self):
        return self._soil_moisture
    
    # Set soil_moisture
    @soil_moisture.setter
    def soil_moisture(self, value):
        self._soil_moisture = value
        # if soil moisture is below the low threshold or above the high threshold
        # set the action event
        if self._soil_moisture < self._soil_low_moisture_threshold or self._soil_moisture > self._soil_high_moisture_threshold:
            self._action.set()
        else:
            self._action.clear()

    # properties soil_temp
    @property
    def soil_temp(self):
        return self._soil_temp
    
    # Set soil_temp
    @soil_temp.setter
    def soil_temp(self, value):
        self._soil_temp = value
        # if soil temperature is below the low threshold or above the high threshold
        # set the action event
        if self._soil_temp < self._soil_low_temp_threshold or self._soil_temp > self._soil_high_temp_threshold:
            self._action.set()
        else:
            self._action.clear()

    # properties soil_ph
    @property
    def soil_ph(self):
        return self._soil_ph
    
    # Set soil_ph
    @soil_ph.setter
    def soil_ph(self, value):
        self._soil_ph = value
        # if soil ph is below the low threshold or above the high threshold
        # set the action event
        if self._soil_ph < self._soil_low_ph_threshold or self._soil_ph > self._soil_high_ph_threshold:
            self._action.set()
        else:
            self._action.clear()

    # properties action
    @property
    def action(self):
        return self._action
    
    def condition(self):
        return self._action.is_set()

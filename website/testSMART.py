from SMART import SMART 
def test_smart():
    # Test the SMART class
    smart_device = SMART("Test Device", "1234", 50, 10, 30, 10, 7, 5)

    print(smart_device.Name)
    print(smart_device.deviceID)

    smart_device.soil_moisture = 70
    smart_device.soil_temp = 40
    smart_device.soil_ph = 8

    #check conditions
    if(smart_device.condition()):
        print("Conditions are not normal")
        if(smart_device.soil_moisture < smart_device.soil_low_moisture_threshold ):
            print("Soil moisture is low")
        if(smart_device.soil_moisture > smart_device.soil_high_moisture_threshold):
            print("Soil moisture is high")
        if(smart_device.soil_temp < smart_device.soil_low_temp_threshold):
            print("Soil temperature is low")
        if(smart_device.soil_temp > smart_device.soil_high_temp_threshold):
            print("Soil temperature is high")
        if(smart_device.soil_ph < smart_device.soil_low_ph_threshold):
            print("Soil ph is low")
        if(smart_device.soil_ph > smart_device.soil_high_ph_threshold):
            print("Soil ph is high")

    else:
        print("Conditions are normal")

test_smart()
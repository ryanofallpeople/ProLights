import time
import tinytuya
import threading
import json
import concurrent.futures


def create_lights_from_file(json_list): #NOW MULTI THREADED TO IMPROVE PERFORMANCE
    new_objects = []
    creation_start = time.time()
    
    def create_light_object(obj): #Function to be spawned into each thread
        deviceid = obj['id']
        localkey = obj['key']
        ip = obj['ip']
           
        new_obj = tinytuya.BulbDevice(
            dev_id=deviceid,
            address=ip,      # Or set to 'Auto' to auto-discover IP address
            local_key=localkey, 
            version=3.3
            )
        
        new_objects.append(new_obj)

    threads = []
    for obj in json_list:
        t = threading.Thread(target=create_light_object, args=(obj,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join() # Hold excecution until each thread terminates and can join the main process.
    
    creation_end = time.time()
    execution_time = creation_end - creation_start
    print(f"Light Objects Created in {execution_time}")
    return new_objects




#Creats usable dictionary of lights with the friendly names as the keys
#Handles race condition created by the multi-threading process by matching the id of the bulbdevice to the id in the scan file
########################################################################

with open('devices.json') as file: #Import devices from scan file
    json_list = json.load(file)

light_objects = create_lights_from_file(json_list)

lights = {}
for obj in json_list: #For every light in the scan file
    for index, bulbdevice in enumerate(light_objects): 
        if(obj['id'] in str(bulbdevice)):
            lights[obj['name']] = light_objects[index]
    
########################################################################


##################################################### SO FAR #############################################
# 1. An unsorted list of bulb device objects has been created named light_objects from the multithreads
# 2. A dictionary named lights has been created with the friendly names of the lights as the key
# 
# * The left light in the booth can be enabled by calling: 
#    lights['BOOTH-LEFT'].set_value(20, True)
#
# * See more information in tinytuya documentation or in notes file
#
##################################################### SO FAR #############################################

def set_studio(rgb):
    for i in lights:
        lights[i].set_value(20, True, nowait=True)
        lights[i].set_colour(rgb[0], rgb[1], rgb[2], nowait=True)
        
def set_light(net_name, rgb, brightness_val):
    # Check if net_name exists in the lights dictionary
    if net_name not in lights:
        error_msg = f"Invalid light name: {net_name}"
        print(error_msg)
        raise ValueError(error_msg)

    # Check if brightness_val is within the valid range
    if not (0 <= brightness_val <= 100):
        error_msg = "Brightness value must be an integer between 0 and 100"
        print(error_msg)
        raise ValueError(error_msg)

    # Execute the rest of the function if inputs are valid
    lights[net_name].set_value(20, True)
    lights[net_name].set_colour(rgb[0], rgb[1], rgb[2], nowait=True)
    lights[net_name].set_brightness_percentage(brightness=brightness_val, nowait)

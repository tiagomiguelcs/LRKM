import evdev, yaml, pathlib, sys, os
from keymapper import keymapper
LOGO = "[LRKM] - "
PROFILE = pathlib.Path(str(pathlib.Path(__file__).resolve().parent)+"/profile.yaml")
DEVICE_NAME = ""

"""
Shows a list of available devices.
"""     
def scan_devices():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    if (not devices): 
        print(LOGO+"Please, run as sudo")
        sys.exit(1)    
    for device in devices:
        print(device.path, device.name, device.phys)

"""
Create a profile YAML file with the name of
device further information can also be added - I need more time :(
"""     
def create_profile(profile_data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(profile_data, file, default_flow_style=False)
        print(LOGO+"Profile created")
    except Exception as e:
        print(LOGO+"Error creating profile: "+str(e))

""" 
Get the device name by its event id.
"""
def get_device_name_by_id(event_id):
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        path = device.path+""
        if path=="None": continue
        c_event_id = path[path.rindex("/")+6:]
        if (c_event_id == event_id):
            return(device.name)

""" 
Get the device name by its event id.
"""
def get_device_id_by_name(device_name):
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        path = device.path+""
        if path=="None": continue
        # print(device)
        if (device.name == device_name):
            return(path[path.rindex("/")+6:])
""" 
Scan Key Codes (opcional).
"""
def scan_key_codes(event_id):
    # Replace '/dev/input/eventX' with the actual event device for your R500s remote
    R500S_REMOTE_DEVICE = '/dev/input/event'+event_id
    # Create an InputDevice object for the R500s remote
    remote_device = evdev.InputDevice(R500S_REMOTE_DEVICE)
    for event in remote_device.read_loop():
        if event.type == 1 and event.value == 1:
            print(f"Keycode: {event.code}")

"""
Read a property from a YAML file.
"""
def read_yaml_property(file_path, property_name):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data.get(property_name)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {file_path}: {e}")
        return None

if __name__ == "__main__":
    if not PROFILE.is_file():
        os.system('clear')
        scan_devices()
        print(LOGO+"Please, enter device id to be used (/dev/input/eventX, where X is the device ID):", end=" ")
        DEVICE_NAME = get_device_name_by_id(input())
        print(LOGO+"Creating Profile File for Device Name '"+DEVICE_NAME+"'")
        create_profile({'device_name': DEVICE_NAME},PROFILE)
    # Run the keymapper
    dname = read_yaml_property(PROFILE,"device_name")
    did = get_device_id_by_name(dname)
    print(LOGO+"Connecting to device id '"+str(did)+"' ("+dname+")...")
    keymapper(did)

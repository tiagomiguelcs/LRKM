from evdev import InputDevice, categorize, ecodes
import subprocess
LOGO = "[LRKM] - "
DEBUG = False
# Set the key codes for the remote keys
LEFT_KEYCODE = 105  # Remote's Keycode for LEFT button (TODO: make this configurable in the profile file)
RIGHT_KEYCODE = 106  # Remote's Keycode for RIGHT button (TODO: make this configurable in the profile file)
# Define flags to keep track of key states and timing
left_key_pressed = False
right_key_pressed = False
event_number = 1

"""
Execute a command using xdotool to a window that is in focus
"""
def execute(command,times,arg=""):
    # Use xdotool to search for a window by its name
    # xdotool_output = subprocess.check_output(["xdotool", "search", "--name", window_name]).decode("utf-8")
    # window_ids = xdotool_output.strip().split("\n")
    # window_id = window_ids[0]

    xdotool_output = subprocess.check_output(["xdotool", "getwindowfocus"]).decode("utf-8")
    window_focus_id = xdotool_output.strip().split("\n")[0]
    if (DEBUG): print(" > ID of the window in focus:"+str(window_focus_id))
    if window_focus_id:
        count = 1
        # Execute x times the command (user provided)
        while count <= times:
             # Execute xdotool on a specified window
            subprocess.call(["xdotool", "key", "--window", window_focus_id, arg, command])
            count += count
    else:
        print("[Remote] Error Window not found.")

def keymapper(event_id):
    # Replace '/dev/input/eventX' with the actual event device for your R500s remote
    remote_device = '/dev/input/event'+event_id
    # Create an InputDevice object for the R500s remote
    device = InputDevice(remote_device)
    print(LOGO+"App running...")
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            #if (event.value == 0): # Skip the second event, when event.value == 0
            #    continue
            if (DEBUG): print("")
            if (DEBUG): print ("# Event "+str(event_number))
            if event.code == RIGHT_KEYCODE:
                if event.value == 1:
                    right_key_pressed = True         
            if event.code == LEFT_KEYCODE:
                if event.value == 1:
                    left_key_pressed = True
        
            if (DEBUG): print(" > Left click="+str(left_key_pressed))
            if (DEBUG): print(" > Right Click="+str(right_key_pressed))
            
            if (event_number==2): # Only analsy flags after second event
                if (DEBUG): print("  > Taking decisions:")
                if (left_key_pressed and right_key_pressed):
                    if (DEBUG): print("    > Both keys were pressed")
                    execute("F11", 1)
                elif(left_key_pressed):
                    if (DEBUG): print("    > Left key pressed")
                    execute("5",3, "click")
                elif(right_key_pressed):
                    if (DEBUG): print("    > Right key pressed")
                    execute("4",3, "click")
                    # execute("Left",1) // A right key will be sent, reverse to the left!
                    
                # after the second event all keys are reseted
                right_key_pressed = False
                left_key_pressed = False
                    
            event_number += event_number
            # Reset the event number after the second one
            if (event_number > 2): event_number = 1
    device.close()

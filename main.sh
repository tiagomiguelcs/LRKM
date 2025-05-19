SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
VERBOSE=1
# Identify current session, wayland or x11
is_wayland() {
    if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
        echo "wayland"
    else
        echo "x11"
    fi
}
SESSION=$(is_wayland)
if [ "$SESSION" = "wayland" ]; then
    if [ "$VERBOSE" = 0 ]; then
        sudo killall ydotoold &> /dev/null
        sudo ydotoold &> /dev/null &
    else
        sudo killall ydotoold
        sudo ydotoold &
    fi
fi
sudo python3 "$SCRIPT_DIR"/main.py --session "$SESSION"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SESSION="x11"
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
    sudo killall ydotoold
    sudo ydotoold &
fi
sudo python3 "$SCRIPT_DIR"/main.py --session "$SESSION"

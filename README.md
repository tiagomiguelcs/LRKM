# Logitech Remote Key Mapper (LRKM)
![](https://img.shields.io/badge/Python-97ca00?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Tested-Logitech%20R500-blue)
![](https://img.shields.io/badge/Distro%20Tested-Debian%2012-orange)

The **Logitech Remote Key Mapper** is a Python script designed to enhance the functionality of Logitech presentation remotes by providing a customizable button mapping solution for different Linux distros. The official Logitech App is not available in Linux-based distros. 

This solution allows users to map each button on the Logitech remote to a different keyboard or mouse button, enabling a more personalized and efficient control experience during presentations or other use cases (_e.g.,_ presenting the content of a Web Page where the Left button in the Logitech remote needs to be remapped to mouse scroll up or down).

**Feel free to fork the repo, happy codding! 🙃**

# Installation and Usage
1. Install dependencies as follows: `sudo apt install xdotool python3-evdev`.
2. Add the execute permission to `main.sh` as follows: `chmod +x main.sh`.
4. Run LRKM as follows: `./main.sh`.

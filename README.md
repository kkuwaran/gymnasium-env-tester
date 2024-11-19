# Gymnasium Environment Tester (gymnasium-env-tester)
This repository contains a Python script for testing (the lastest version of) all **Gymnasium** and **Gymnasium Robotics** environments to ensure they run properly. The script allows users to test:
- All environments at once.
- A specific environment individually.

## Installation Guide
Before running the script, ensure you have installed the required dependencies for the environments you wish to test.

**Note 1:** Some packages require a C++ compiler to build dependencies. For Windows users, you can install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to satisfy this requirement.

**Note 2:** The package versions listed below reflect the latest versions as of November 18, 2024. Newer versions may also work.


### Gymnasium
Gymnasium is the base library required for this project. Install it using pip:
```bash
pip install gymnasium
```
- Installed version: `gymnasium-1.0.0`

More information: [Gymnasium Documentation](https://gymnasium.farama.org/index.html)

### Box2D Environments
For environments requiring Box2D, follow these steps:
1. Install swig:
   ```bash
   pip install swig
   ```
   - Installed package: `swig-4.2.1.post0`
  
2. Install Gymnasium with Box2D support:
   ```bash
   pip install gymnasium[box2d]
   ```
   - Installed packages: `box2d-py-2.3.5`, `pygame-2.6.0`
  
### Mujoco Environments
To use Mujoco-based environments, install the required packages:
```bash
pip install gymnasium[mujoco]
```
- Installed packages: `glfw-2.7.0`, `imageio-2.36.0`, `mujoco-3.2.5`, `pyopengl-3.1.7`

### A.L.E (Arcade Learning Environment)
For Atari-based environments, use the following command:
```bash
pip install gymnasium[atari]
```
- Installed package: `ale-py-0.10.1`

For more information, refer to the [ALE Documentation](https://ale.farama.org/getting-started/)

### Gymnasium-Robotics
Gymnasium robotics environments:
```bash
pip install gymnasium-robotics
```
- Installed version: `PettingZoo-1.24.3`, `gymnasium-robotics-1.3.1`
- **Note:** Installing `gymnasium-robotics` will downgrade mujoco to `mujoco-3.1.6`

For more information, refer to the [Gymnasium-Robotics Documentation](https://robotics.farama.org/)


## Running the Script
- Test all environments:
  ```bash
  python test_gymnasium_envs.py
  ```
- Test a specific environment: Provide the environment name as an argument:
  ```bash
  python test_gymnasium_envs.py --env-id <environment-id>
  ```

Example:
```bash
python test_gymnasium_envs.py --env-id CartPole-v1
```

## Features
- Comprehensive testing of Gymnasium and Robotics environments.
- Flexibility to run individual tests.

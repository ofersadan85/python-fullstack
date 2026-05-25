# Installing Docker Desktop on Windows 11

## Step 1: Install Windows Subsystem for Linux (WSL)

Docker Desktop for Windows requires WSL 2. Start by installing WSL if it's not already installed on your system.

1. Open the terminal as an administrator and run the following command to install WSL and set WSL 2 as your default version:

    ```powershell
    wsl --install
    ```

    This command will enable the necessary features, download the latest WSL Linux kernel, set WSL 2 as your default version, and install a Linux distribution for you (by default, Ubuntu).

2. Restart your computer if prompted.

## Step 2: Install Docker Desktop

1. Download Docker Desktop for Windows from the official [Docker website](https://www.docker.com/products/docker-desktop).

2. Run the installer and follow the prompts. Make sure to:
    - Agree to the terms and conditions.
    - Choose to enable the WSL 2 feature.

3. Once the installation is complete, Docker Desktop will start automatically. If it doesn't, you can start it from the Start menu.

4. Docker Desktop will prompt you to log in with a Docker account. If you don't have one, you can create a free account.

5. Docker Desktop will configure itself to use WSL 2. If there are any issues, you can go to Docker Desktop settings and ensure that WSL 2 is selected under the "General" tab.

## Step 3: Verify Installation

1. Open a new terminal window and run the following command to verify that Docker is installed correctly:

    ```powershell
    docker --version
    ```

    This command should return the Docker version installed on your system.

## Basic Usage Examples

See the section on [Docker Tutorial](./docker2.md) for basic usage examples and a step-by-step guide on running containers and creating a Dockerfile.

See [Docker documentation](https://docs.docker.com/get-started/overview/) for more detailed information on using Docker.

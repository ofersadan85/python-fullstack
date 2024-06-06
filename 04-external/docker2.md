# Docker Usage

This section provides basic usage examples for Docker. For more detailed information, see the [Docker documentation](https://docs.docker.com/get-started/overview/).

When installing Docker Desktop on Windows, we get multiple tools which include:

1. Docker Desktop - The UI tool for managing Docker containers.
2. Docker CLI - The command-line tool for managing Docker containers.
3. Docker Compose - A tool for defining and running multi-container Docker applications.
4. Docker Build - A tool for building Docker images from a Dockerfile.
5. Docker Engine - The core Docker technology that runs containers.

## Docker Desktop Installation

See the [docker installation guide](./docker.md) if you haven't installed Docker Desktop yet.

## Basic Usage

### Running an Existing Container Image

Some applications have already been packaged into Docker images and are available on [Docker Hub](https://hub.docker.com/). You can search for these images and run them as containers on your local machine. To search for an image, either go the the Docker Hub website or use the `docker search` command:

```powershell
docker search python
```

The results will show you which images are popular (more starts) and which are official (approved by the software developers). It's always recommended to use official images when possible unless you know for sure that you need something else.

Optional: To pull an image from Docker Hub, use the `docker pull` command followed by the image name and tag (if applicable). For example, to pull the official Python image:

```powershell
docker pull python:3.9
```

This will download the Python 3.9 image to your local machine. You can then run a container using this image:

```powershell
docker run -it --rm python:3.9 python
```

And you'll be dropped into a Python shell where you can run Python code. The `-it` flag is used to allocate a pseudo-TTY and keep STDIN open even if not attached, and the `--rm` flag is used to remove the container when it exits.

We can also use `run` directly without pulling the image first, and Docker will automatically pull the image if it's not available locally. Let's try that with a different version of Python:

```powershell
docker run -it --rm python:3.10 python
```

We have now run both Python 3.9 image and a Python 3.10 image in separate containers. This was done without installing anything on our local machine (other than Docker Desktop), so there is no collision between the two versions. This is one reason why Docker is so popular for development and testing environments.

Our changes and commands are isolated (contained) within the container, so we can run multiple versions of the same software without conflicts. This is a powerful feature of Docker that allows us to create reproducible environments for our applications, that can be recreated on any machine that has Docker installed.

The Python images are a complete Linux environment with Python installed, so you can run any Python code you like. When you exit the container, it will be removed automatically because of the `--rm` flag we used.

## Running in Detached Mode

When you run a container with the `-it` flags, you are attached to the container's terminal and can interact with it. If you want to run a container in the background (detached mode), you can use the `-d` flag:

```powershell
docker run -d python:3.10
```

You won't see any output from the container, but you can check its status using the `docker ps` command:

```powers
docker ps
```

This will show you a list of running containers, including their container ID, image name, command, status, and ports. You can use the container ID or name to interact with the container, stop it, or remove it.

For this example, we won't see any output because the Python container doesn't have a command "running" - so without a terminal the container will exit immediately.

Let's try a different image that runs a web server:

```powershell
docker run -d -p 8080:80 --name mynginx nginx
```

This command runs an Nginx web server in detached mode, maps port 8080 on your host machine to port 80 in the container, and assigns the name `mynginx` to the container. You can now access the Nginx server by navigating to [http://localhost:8080](http://localhost:8080) in your web browser.

It's important to note that the `-d` flag runs the container in the background, so you won't see any output from the container. If you want to see the logs, you can use the `docker logs` command:

```powershell
docker logs mynginx
```

This will show you the logs from the Nginx container.

If you want to stop the container, you can use the `docker stop` command followed by the container name or ID:

```powershell
docker stop mynginx
```

Note that this stops the running container process, but the container still exists. We can start it again using the `docker start` command:

```powershell
docker start mynginx
```

Or remove it completely using the `docker rm` command:

```powershell
docker rm mynginx
```

## Building a Custom Docker Image

See the [Dockerfile tutorial](./docker3.md) for a step-by-step guide on creating a custom Docker image using a Dockerfile.

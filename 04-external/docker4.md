# Docker cheat sheet

This document is meant to serve as a quick reference for common Docker commands and concepts. It is not meant to be an exhaustive guide to Docker, but rather a concise collection of commands and tips to help you get started with Docker.

Most of these commands can be run in one way or another through the Docker Desktop UI as well, but it's useful to get familiar with the options.

## Building Docker images

```powershell
docker build -t my-app .
```

This is the most common command used to build a Docker image. It takes a `Dockerfile` in the current directory and builds an image tagged with the name `my-app`. The `-t` flag is used to specify the tag or name of the image. The `.` at the end of the command specifies the path to the current directory, which must contain the `Dockerfile`.

### Complex builds

```powershell
docker build -t my-app:latest -f Dockerfile.prod --build-arg BACKEND_URL=http://backend:8000 backend
```

This command represents a more complex build scenario. It builds an image tagged with `my-app:latest` using the `Dockerfile.prod` file in the `backend` directory. It also passes a build argument `BACKEND_URL` with the value `http://backend:8000` to the build process. This can be useful for passing environment-specific values to the build process.

Let's break it down step by step:

- `docker build` - Command to build a Docker image.
- `-t my-app:latest` - Tag the image with the name `my-app` and the tag `latest`. You can use different tags for different builds that still share the same base image name. For example, you might have `my-app:production` and `my-app:development` live side by side for different purposes.
- `-f Dockerfile.prod` - Use the `Dockerfile.prod` file for the build process. Without this flag, Docker looks for a file named `Dockerfile` in the current directory, so use it to specify a different file.
- `--build-arg BACKEND_URL=http://backend:8000` - Pass a build argument `BACKEND_URL` with the value `http://backend:8000` to the build process. This variable can be used in the `Dockerfile` during the build process. This variable is not available in the final image or the running container.
- `backend` - The path to the directory containing the `Dockerfile.prod` file. This is the context for the build process, and Docker will look for the `Dockerfile.prod` file in this directory. If you have a `.dockerignore` file in this directory, Docker will use it to exclude files and directories from the build context.

## Running Docker containers

```powershell
docker run -p 4000:5000 my-app
# OR
docker run -p 4000:5000 my-app:latest
```

This command runs a Docker container based on the `my-app` image. It maps port `4000` on the host machine to port `5000` in the container. This allows you to access the application running inside the container on port `5000` by navigating to `http://localhost:4000` in your web browser.

Usually, not specifying a tag (`my-app`) is the same as specifying the "latest" tag, and it will use the latest image you have (`my-app:latest`).

If the `my-app` image does not exist on your local machine, docker will automatically search for an image by that exact name on [DockerHub](http://hub.docker.com) and will pull it to your machine if it exists.

### Running a temporary container with an interactive terminal

```powershell
docker run -it --rm my-app
```

This is often useful when you want to test something out. You terminal will be "attached" to the running container, so your commands (Ctrl-C for example) are executed directly there. You can also combine it with most other flags if needed (for example, `-p 4000:5000`)

### Running a container in the background

```powershell
docker run -d --name my-running-app my-app
```

This has the same effect of running the `my-app` image as above, but this time, your terminal is "detached" (`-d` or `--detach`) from it, which means it will keep running in the background. You can always see the terminal later if needed with `docker logs [container-name]` which is why it's useful to give it a custom name like we did with `--name my-running-app`. Without `--name` docker chooses a random name for you.

You can also stop the container (which doesn't delete it) with

```powershell
docker stop my-running-app
```

And start it back up later with

```powershell
docker start my-running-app
```

Or remove it completely with

```powershell
docker rm my-running-app
```

Which removes the running container and it's files (but does not delete the static image that was used for this container).

### Complex example

```powershell
docker run -e API_KEY=abcde -v ./my-data:/container-data -p 4000:5000 --env-file=production.env --name my-running-app my-app:production
```

This are just a few of the flags we can use when running a container, but they are the most important / useful ones. Let's break it down:

- `docker run` - The basic command for running docker containers
- `-e API_KEY=abcde` - We can pass environment variables that will be accessible to any running process within the container. Can be used multiple times to specify more variables (for example: `-e API_KEY=abcde -e ANOTHER_SECRET=12345`)
- `-v ./my-data:/container-data` or `--volume ./my-data:/container-data` - maps a real folder on our local host computer (`./my-data`) to a folder that exists only inside the container (`/container-data`). Can be specified multiple times to map multiple folders. While it's possible to use to map specific files instead of folders, it can be more complex for various reasons, so prefer folders for this use when you can.
- `-p 4000:5000` or `--port 4000:5000` - Maps a real port (4000) from out local host computer, to a port that is used by the container (5000). The app running in the container must be listening on that port for this flag to have any effect. Without it, the inner container might be listening on that port but we can't (easily) access it. This flag makes that process available to us on [http://localhost:5000](http://localhost:5000)
- `--env-file=production.env` - Load a whole file of environment variables instead of loading multiple variables through `-e`. Useful for when you have complete sets of variables for different purposes, for example `production.env` vs. `development.env`
- `--name my-running-app` - Specify a custom name for the container. Must be unique (no other active container under that same name, or the run command will fail). Usually a good idea so you can use that name later in other commands, unless you know you need to run many similar containers and don't want to name them all.
- `my-app:production` - The image name (`my-app`) and the tag (`production`) of the image that will be used as a starting point for the container to run. The image (with the correct tag) must be wither previously build by you on the same computer, or pulled from [DockerHub](http://hub.docker.com). If you don't specify a tag, this is the (usually) same as using the "latest" tag (`my-app` is the same as `my-app:latest`).

## Docker Compose

Building and running docker containers through the command line has several difficulties:

- Running each container often requires a long and complex command with many flags
- The flags usually repeat themselves for running the same image for the same purpose.
- The `build` step is usually done just before the `run` step, so it'll be simpler if this step could be done in one command.
- Running multiple containers for the same app (for example, a `backend`, a `frontend` and a `database`) might mean that we want to repeat some values multiple times, and have them be more manageable and predictable.

To solve that, we have "Docker Compose" - a special command that takes in a `docker-compose.yml` file in a specific format that contains all of our needs, and gives us the running containers we need.

We don't get into too much details about the file format and all the options (you can read more [here](https://docs.docker.com/compose/)) but a `docker-compose.yml` file might look like this:

```yml
services:
  frontend:
    container_name: frontend
    build:
      context: ./frontend
      args:
        - BACKEND_URL=http://api.example.com
    ports:
      - 8888:80

  backend:
    container_name: backend
    build:
      context: ./backend
    environment:
      - FRONTEND_URL=http://www.example.com
    env_file:
      - .env
    ports:
      - 4444:5555
    volumes:
      - ./data:/data
```

Which contains our definitions to both a `backend` image and `frontend` image that need to run together. The following commands can now be run in that same folder, which will simplify our workflow:

- Just build both containers, don't run them

```powershell
docker compose build
```

- Just run the containers - the terminal stays attached to the containers

```powershell
docker compose up
```

- Run the containers in the background (detach the terminal)

```powershell
docker compose up -d
```

- Stop all the containers (only the ones specified in the file)

```powershell
docker compose down
```

- Force a build, run, and detach - in one step

```powershell
docker compose up -d --build
```

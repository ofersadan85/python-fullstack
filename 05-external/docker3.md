# Dockerfile - Custom Docker Image

While using pre-built Docker images is convenient, you may want to create your own custom image for your application. This allows you to define the environment and dependencies required for your application to run.

Let's create a basic Dockerfile for a simple Python application. Create a new directory for your project and add the following files:

- `main.py` - A simple Flask application that responds with "Hello, World!".

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run()
```

- `Dockerfile` - A file that defines the steps to build the Docker image.

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10

# Install Flask
RUN pip install Flask

# Set the working directory in the container
WORKDIR /app

# Copy our main.py file into the container
COPY main.py /app/main.py

# Expose port 5000 to the outside world
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=main.py

# Define the command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
```

We'll break down the steps in a moment, but first, let's build the Docker image. Run the following command in the directory where your `Dockerfile` and `main.py` files are located:

```powershell
docker build -t my-app .
```

This command builds a Docker image based on the `Dockerfile` in the current directory and tags it with the name `test-app`. It may take a few moments to download the necessary dependencies and build the image.

Let's break down the command we just ran:

- `docker build` - Command to build a Docker image.
- `-t test-app` - Tag the image with the name `test-app`.
- `.` - The path to the directory containing the `Dockerfile` (the current directory in this case).

Once the build is complete, you can run the Docker container using the following command:

```powershell
docker run -p 5000:5000 -d --name my-app --rm my-app
```

Which will run our app. Check it out by navigating to [http://localhost:5000](http://localhost:5000) in your web browser. You should see "Hello, World!" displayed on the page.

Let's break down the command we just ran:

- `docker run` - Command to run a Docker container.
- `-p 5000:5000` - Map port 5000 on your host machine (the real port) to port 5000 in the container (the virtual port).
- `-d` - Run the container in detached mode (in the background).
- `--name my-app` - Assign the name `my-app` to the container.
- `--rm` - Automatically remove the container when it exits.
- `my-app` - The name of the Docker image to run, must match the tag used when building the image.

Congratulations! You've just created a custom Docker image for a simple Python application. This process can be extended to more complex applications with additional dependencies and configurations.

To stop the running container, you can use the following command:

```powershell
docker stop my-app
```

We don't need to remove the container manually because we used the `--rm` flag when running it. The container will be automatically removed when it exits. If we forget to use the `--rm` flag, we can remove the container using the following command:

```powershell
docker rm my-app
```

## Dockerfile Breakdown

Let's go back and break down the `Dockerfile` we created. It contains several instructions that define how the Docker image is built:

1. `FROM python:3.10` - Use an official Python runtime as the base image. This image contains the Python runtime and pip package manager. It's the basis for our custom image, so we don't have to install a complete Linux distribution or Python environment from scratch. We can experiment with different base images to find the one that best fits our needs, or create our own base images if necessary. For example, using the `python:3.10-slim` image would result in a smaller image size, but it may lack some dependencies that our application needs. `python:3.10-alpine` is another popular choice for even smaller images, but it uses the Alpine Linux distribution, which may require additional configuration for some applications.
2. `RUN pip install Flask` - Install the Flask package using `pip`. This command installs Flask in the Docker image, so our application can use it. This is the same step that we would need if we would install Flask on our local machine.
3. `WORKDIR /app` - Set the working directory in the container to `/app`. This is where our application code will be copied and where all our other commands will be executed.
4. `COPY main.py /app/main.py` - Copy the `main.py` file from the host machine to the `/app` directory in the container. This is how we add our application code to the image. Without this step, our application code wouldn't be available inside the container, which is isolated from our host machine.
5. `EXPOSE 5000` - Expose port 5000 to the outside world. This is the port that our Flask application will listen on, and we need to expose it so that we can access our application from outside the container.
6. `ENV FLASK_APP=main.py` - Set the `FLASK_APP` environment variable to `main.py`. This tells Flask which Python file contains the application code. This is necessary for Flask to find and run our application. We can set any environment variables we need for our application in the Dockerfile, and they will be available to the running container. This is a common way to configure applications in Docker, but don't include sensitive information like passwords in environment variables (since they can be viewed by anyone with access to the container, or our Docker image, or our git repository).
7. `CMD ["flask", "run", "--host=0.0.0.0"]` - Define the command to run the application. This command tells Docker to run the Flask development server when the container starts. The `--host=0.0.0.0` argument tells Flask to listen on all network interfaces inside the container, so we can access the server from outside the container. This is necessary because by default Flask only listens on `localhost`, which would prevent us from accessing the server from our host machine.

Any of these commands can be used multiple times in a Dockerfile, and they will be executed in order. This allows us to define a series of steps to build our custom image, including installing dependencies, copying files, setting environment variables, and more. The only exception (in a simple Dockerfile) is that there can only be one `FROM` instruction (at the start), which defines the base image for our custom image, and one `CMD` instruction, which defines the default command to run when the container starts (at the end).

## Dockerfile commands

Let's summarize the most common and useful Dockerfile commands:

- `FROM` - Defines the base image for our custom image.
- `RUN` - Executes a command in the container during the build process (not when the container starts).
- `WORKDIR` - Sets the working directory for subsequent commands. Creates the directory if it doesn't exist.
- `COPY` - Copies files from the host machine to the container. Use `COPY . .` to copy all files from the current directory to the container.
- `EXPOSE` - Exposes a port to the outside world.
- `ENV` - Sets environment variables for the container.
- `ARG` - Defines build-time variables that can be passed to the `docker build` command. Does not persist in the final image.
- `CMD` - Defines the default command to run when the container starts. Only the last `CMD` instruction is used.
- `ENTRYPOINT` - Defines the default executable to run when the container starts. Can be overridden by specifying a command when running the container. We'll discuss the difference between `CMD` and `ENTRYPOINT` in the future.
- `VOLUME` - Creates a mount point for a volume in the container. Used to persist data outside the container. We'll discuss volumes in the future as well.

## Docker build caching

When you build a Docker image, Docker caches the results of each step to speed up the build process. If you change a step in the Dockerfile, Docker will only rebuild the steps that come after the change. This is why it's important to order your Dockerfile commands from least likely to change to most likely to change. For example, you would install dependencies first and copy application code last, since the application code is more likely to change frequently.

## Publishing Docker images

Once you've built a custom Docker image, you can publish it to a container registry like Docker Hub or GitHub Container Registry. This allows you to share your image with others or use it in different environments. We won't discuss publishing images in this guide, but it's a common practice in software development workflows.

But just as a warning: Once your images are published they can be seen and reviewed by anyone, so be careful not to include sensitive information in your images (like passwords or API keys), even in environment variables. Always use secure methods to manage sensitive information in your applications.

In other words, images should always be considered public, even if you think they're private. This is a good practice to follow when working with Docker and other container technologies, much like how we treat git repositories as public (even if they're private) and avoid committing sensitive information to them.

Any information that is needed to run the application should be passed as environment variables or configuration files, and not hardcoded into the Dockerfile or application code. This is a best practice for security and portability, and it allows you to run the same image in different environments without modification.

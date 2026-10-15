# Experiment 10 — Containerization with Docker

## Aim

Package the model-serving application and its Python dependencies into a Docker image, then run and verify the container.

## Learning objectives

- Explain the role of a Dockerfile, image, and container.
- Build an image using this folder's Dockerfile.
- Run the application with a port mapping and verify its health endpoint.

## Requirements

- Docker Engine or Docker Desktop installed and running
- The Python dependencies listed in this experiment's `requirements.txt`

## Procedure

1. Review this folder's [`Dockerfile`](./Dockerfile), [`app.py`](./app.py), and `requirements.txt`.
2. Open a terminal in this folder and build the image:

   ```bash
   docker build -t mlops-practical:1.0 .
   ```

3. In the same terminal, start the container:

   ```bash
   docker run --rm --name mlops-practical -p 8000:8000 mlops-practical:1.0
   ```

4. In a second terminal, call the health endpoint:

   ```bash
   curl http://127.0.0.1:8000/health
   ```

5. Stop the running container with Ctrl+C, then record the actual build result, image details, health response, and any errors.

On Windows, use `curl.exe` if PowerShell resolves `curl` to its web-request alias. If port 8000 is already in use, choose another host port, for example `-p 8001:8000`, and use that port in the request URL.

## Captured environment result

[`OUTPUT.txt`](./OUTPUT.txt) records the Docker availability check. No image-build output is claimed when the Docker CLI or daemon is unavailable.

## Viva questions

1. What is the difference between a Docker image and a container?
2. Why should a Docker build context contain only the files needed by the image?
3. What does the `-p 8000:8000` option configure?

## Related practicals

- Model API: [Experiment 11](../experiment-11-rest-api/README.md)
- Integrated results: [Experiment 12](../experiment-12-integrated-workflow/README.md)

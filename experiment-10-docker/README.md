# Experiment 10 — Containerization with Docker

## Aim

Package the model-serving application and its Python dependencies into a Docker image, then run and verify the container.

## Learning objectives

- Explain the role of a Dockerfile, image, and container.
- Build an image using the repository-root Dockerfile.
- Run the application with a port mapping and verify its health endpoint.

## Requirements

- Docker Engine or Docker Desktop installed and running
- Python project dependencies described in the repository-root `requirements.txt`

## Procedure

1. Review the canonical [`Dockerfile`](../Dockerfile) and [`.dockerignore`](../.dockerignore) at the repository root.
2. From the repository root, build the image:

   ```bash
   docker build -t mlops-practical:1.0 .
   ```

3. Start the container:

   ```bash
   docker run --rm --name mlops-practical -p 8000:8000 mlops-practical:1.0
   ```

4. In a second terminal, call the health endpoint:

   ```bash
   curl http://127.0.0.1:8000/health
   ```

5. Stop the running container with Ctrl+C, then record the actual build result, image details, health response, and any errors.

On Windows, use `curl.exe` if PowerShell resolves `curl` to its web-request alias. If port 8000 is already in use, choose another host port, for example `-p 8001:8000`, and use that port in the request URL.

## Observation and result

Record the Docker version, image tag, actual command output, and health response. A Dockerfile or an illustrative output example is not evidence that an image was built or a container ran.

## Expected output format

See [`OUTPUT.txt`](./OUTPUT.txt) for an illustrative format only.

## Viva questions

1. What is the difference between a Docker image and a container?
2. Why does `.dockerignore` matter when building an image?
3. What does the `-p 8000:8000` option configure?

## Related practicals

- Model API: [Experiment 11](../experiment-11-rest-api/README.md)
- Integrated checklist: [Experiment 12](../experiment-12-integrated-workflow/README.md)

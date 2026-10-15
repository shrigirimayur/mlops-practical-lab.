# Practical 10 | Containerizing a Model Service

**Focus:** Dockerfile, image build, container run, port mapping and health verification.

## Aim

Package the model API and its Python dependencies into a Docker image and verify the running container through its health endpoint.

## Requirements

- Docker Engine or Docker Desktop installed and running (`docker info` must succeed).
- This folder's [`Dockerfile`](./Dockerfile), [`app.py`](./app.py) and `requirements.txt`.

## Procedure

Open a terminal in this folder:

```powershell
docker build -t mlops-practical:1.0 .
docker run --rm --name mlops-practical -p 8000:8000 mlops-practical:1.0
```

In a second terminal, verify the service:

```powershell
curl.exe http://127.0.0.1:8000/health
```

Stop the container with Ctrl+C. If port `8000` is occupied, use `-p 8001:8000` and request port `8001`.

## Observed result

The execution environment did not have the Docker command available. Therefore the image build, container startup and container health check are **not verified**. The actual environment check is in [`OUTPUT.txt`](./OUTPUT.txt); the Dockerfile and reproducible commands are included for execution on a Docker-enabled system.

## Conclusion

The Dockerfile defines a repeatable image build context for the model API. A successful local Python run is not a substitute for building and running the container.

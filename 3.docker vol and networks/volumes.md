# Docker Volumes and Networks

## 1. Docker Volumes

Docker volumes are used to persist data generated or used by Docker containers. They allow data sharing between containers and the host system, ensuring data longevity beyond container lifespans.

### Volume Types

1. **Path-to-Path Volume**: Maps a specific path on the host to a path within the container. It allows for direct host-to-container interaction with the specified directory.
   - **Example**: 
     ```bash
     docker run -v /host/path:/container/path my-image
     ```
   - In this example, `/host/path` is mapped to `/container/path` in the container, enabling both to access shared data.

2. **Object-to-Path Volume**: This uses Docker's volume object feature, allowing Docker to manage storage in a specific location on the host.
   - **Example**: 
     ```bash
     docker volume create my-volume
     docker run -v my-volume:/container/path my-image
     ```
   - Here, `my-volume` is a Docker-managed volume, mounted at `/container/path` in the container.

### Volume Commands

  ```bash
  docker volume create volume-name
# List Volumes:
    docker volume ls
# Inspect Volume:
    docker volume inspect volume-name
# Remove Volume:
    docker volume rm volume-name
    ```
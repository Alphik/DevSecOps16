# Docker Networks and Inspecting Containers

## Docker Networks

Docker networks allow containers to communicate with each other and with the host system. They provide various networking options to suit different use cases, such as isolating containers or connecting them in a shared network.

### Types of Docker Networks

1. **Bridge Network**: The default network for standalone containers. It allows containers to communicate within the same network but isolates them from external networks.

   - **Example**:
     ```bash
     docker network create my-bridge-network
     docker run --network my-bridge-network my-image
     ```

2. **Host Network**: Connects the container directly to the host’s network stack, bypassing the network isolation.

   - **Example**:
     ```bash
     docker run --network host my-image
     ```

3. **Overlay Network**: Used primarily for Docker Swarm services, enabling multi-host communication across Docker nodes.

   - **Example**:
     ```bash
     docker network create -d overlay my-overlay-network
     ```

4. **None Network**: Disables all networking, isolating the container completely.
   - **Example**:
     ```bash
     docker run --network none my-image
     ```

### Network Commands

```bash
docker network create network-name
# List Networks:
  docker network ls
# Inspect Network:
  docker network inspect network-name
# Remove Network:
  docker network rm network-name
```

# Inspecting Containers

The docker inspect command provides detailed information about Docker objects, including containers, images, volumes, and networks. This command returns JSON-formatted data that includes various settings and configurations.

Syntax:
docker inspect object-name-or-id

Example:

```bash
docker inspect my-container
```

Information Provided by docker inspect
Network Settings: Details about the network configuration of the container, such as IP address, MAC address, and network mode.
Volume Mounts: Information about volumes mounted to the container, including source and destination paths.
Environment Variables: Lists environment variables set within the container.
Configuration Details: Includes details about the container’s configuration, such as the image used, command executed, and resource limits.
Using docker inspect for Networks
To inspect a specific network:

```bash
docker inspect network-name
```

This command provides detailed information about the network, including connected containers, network driver, and subnet configurations.

Using docker inspect for Containers
To inspect a specific container:

```bash
docker inspect container-id
```

This command returns comprehensive details about the container, which can be useful for debugging and monitoring purposes.

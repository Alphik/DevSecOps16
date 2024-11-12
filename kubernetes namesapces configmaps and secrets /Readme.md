In Kubernetes, Secrets and ConfigMaps are used to manage configuration data for applications. They both serve similar purposes in providing configuration to containers, but they differ in the types of data they store and how they're used. Let’s break down each:

1. ConfigMaps
   ConfigMaps store non-sensitive configuration data in key-value pairs, and they're typically used for data such as configuration settings, environment variables, or file paths.

- Use Case: Non-sensitive configuration settings like app configurations, feature flags, etc.
- Data Type: Plain text (strings).
- Volume Mounting: ConfigMaps can be mounted as files or environment variables in your containers.
- Common Usage: Setting up app configurations that may vary between environments (e.g., dev, staging, prod).
  Example of a ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  APP_MODE: "production"
  APP_PORT: "8080"
```

In this example, the my-config ConfigMap holds two configurations: APP_MODE and APP_PORT.

### Using ConfigMap in a Pod:

You can inject ConfigMap data as environment variables or mount it as a volume.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: my-container
      image: my-image
      envFrom:
        - configMapRef:
            name: my-config
```

In this example, the APP_MODE and APP_PORT values are available as environment variables in the container.

2. Secrets
   Secrets store sensitive data like passwords, tokens, or SSH keys. Kubernetes keeps this data encrypted or base64-encoded to limit accidental exposure.

- Use Case: Sensitive data like API keys, database credentials, or any other private information.
- Data Type: Encoded in Base64 for storage but can be plain text or binary data.
- Volume Mounting: Like ConfigMaps, Secrets can also be mounted as files or environment variables in your containers.
- Security: Secrets are encrypted at rest (if configured properly) and transmitted securely within the cluster.
  Example of a Secret:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  DB_PASSWORD: cGFzc3dvcmQ= # Base64-encoded string
```

Using Secret in a Pod:
You can use a Secret as environment variables or files in a Pod.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-secure-pod
spec:
  containers:
    - name: secure-container
      image: my-secure-image
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: DB_PASSWORD
```

In this example, the DB_PASSWORD environment variable is set in the container from the my-secret Secret.

## Differences Between ConfigMaps and Secrets

| Feature      | ConfigMap                                         | Secret                                            |
| ------------ | ------------------------------------------------- | ------------------------------------------------- |
| **Purpose**  | Non-sensitive config data                         | Sensitive data                                    |
| **Storage**  | Plain text                                        | Base64-encoded (and optionally encrypted at rest) |
| **Usage**    | Environment variables, volumes, command arguments | Environment variables, volumes                    |
| **Data**     | Plain text                                        | Base64-encoded                                    |
| **Security** | Not encrypted                                     | Encrypted in etcd (if configured)                 |

### When to Use ConfigMaps vs. Secrets

- **ConfigMaps**: Use ConfigMaps when you have non-sensitive configuration data.
- **Secrets**: Use Secrets whenever your configuration data is sensitive, even if it’s not highly confidential, to reduce the risk of exposure.

By separating configuration and sensitive data into ConfigMaps and Secrets, you keep your applications flexible, secure, and adaptable across different environments.

# namespaces in k8s

In Kubernetes, Namespaces provide a way to divide cluster resources among multiple users or teams. They act as virtual clusters within a single physical Kubernetes cluster, enabling logical isolation, resource organization, and easier management.

## Key Concepts of Namespaces

- Logical Isolation:
  Namespaces help isolate resources, allowing you to have different environments ( development, staging, production) or to organize resources by team, project, or business unit.
- Scope of Namespaces:
  Not all resources are namespaced. For instance, resources like Nodes and PersistentVolumes are cluster-wide, meaning they are shared across namespaces.
  Namespaced resources include Pods, Services, ConfigMaps, Secrets, Deployments, and more.
- Access Control:
  Namespaces enable you to define role-based access controls (RBAC) for specific groups of resources. For example, a team might have access only to the namespace they work within, while other namespaces remain inaccessible to them.
- Resource Quotas:
  You can apply ResourceQuotas to namespaces to control the amount of CPU, memory, or storage that resources within the namespace can use, helping prevent resource hogging and enforcing limits.
- Default and System Namespaces:
  When you create a cluster, some namespaces are created by default:

1. default: The default namespace where resources are created if no namespace is specified.
2. kube-system: Used for Kubernetes system components (like the API server, DNS).
3. kube-public: A publicly readable namespace, typically used for public, non-sensitive information.
4. kube-node-lease: Contains lease objects for each node, used to determine node health.

## Creating and Managing Namespaces

You can create and manage namespaces using kubectl:
Creating a Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-namespace
```

Or create it directly via kubectl:

```bash
kubectl create namespace my-namespace
```

Listing Namespaces

```bash
kubectl get namespaces
```

Deleting a Namespace

```bash
kubectl delete namespace my-namespace
```

Deleting a namespace removes all resources within it, so use this command carefully.

## Using Namespaces with Resources

Specify a namespace when creating resources to place them in the desired namespace:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: my-namespace
spec:
  containers:
    - name: my-container
      image: nginx
```

You can also switch to a namespace for all commands in a session:

```bash
kubectl config set-context --current --namespace=my-namespace
```

## Multi-Tenancy and Namespaces

Namespaces help in multi-tenant environments, where multiple teams or projects use a shared Kubernetes cluster. By providing each team or project with its own namespace, you can enforce isolation while sharing the underlying infrastructure.

Namespace Best Practices

- Use Namespaces for Environment Separation: Have separate namespaces for dev, staging, and prod.
- Leverage RBAC: Limit access to specific namespaces for different teams to enhance security.
- Apply Resource Quotas: Set quotas per namespace to prevent overuse and balance resources across the cluster.
- Namespaces simplify the management of large clusters, enabling better organization, security, and control over resources.

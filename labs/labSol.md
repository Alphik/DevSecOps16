link to the labs : [https://github.com/devopsPRO27/k8s-lab1/tree/main]

# lab2 solution

1. start the cluster

```bash
minikube start

```

1. create a flask application 

app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

1. build a docker file 

```docker
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]

```

1. Build the Docker Image

```docker
docker build -t flask-app:latest .
minikube image load flask-app:latest

```

1. Create the YAML File for the Pod

```docker
apiVersion: v1
kind: Pod
metadata:
  name: flask-app
  labels:
    app: flask-app
spec:
  containers:
  - name: flask-app
    image: flask-app:latest
    ports:
    - containerPort: 5000
```

```bash
kubectl apply -f pod.yaml
```

1.  Create a NodePort Service

```docker
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  type: NodePort
  selector:
    app: flask-app
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
    nodePort: 31311

```

```bash
kubectl apply -f service.yaml
```

1. Expose the Service

```bash
kubectl expose pod flask-app --type=NodePort --name=flask-service --port=5000 --target-port=5000 --node-port=31311
**minikube ip**
```

lab3 solution

```bash
kubectl create namespace frontend
kubectl create namespace backend
```

```bash
apiVersion: v1
kind: Pod
metadata:
  name: frontend-app
  namespace: frontend
  labels:
    app: frontend-app
spec:
  containers:
  - name: frontend-app
    image: busybox
    command:
    - sleep
    - "3600" # Keep the pod running

```

```bash
kubectl apply -f frontend-deployment.yaml

```

```bash
apiVersion: v1
kind: Pod
metadata:
  name: backend-app
  namespace: backend
  labels:
    app: backend-app
spec:
  containers:
  - name: backend-app
    image: busybox
    command:
    - sleep
    - "3600" # Keep the pod running

```

```bash
kubectl apply -f backend-deployment.yaml

```

```bash
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: restrict-frontend
  namespace: backend
spec:
  podSelector: {} # Apply to all pods in the 'backend' namespace
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: backend # Only allow traffic from the 'backend' namespace

```

```bash
kubectl apply -f network-policy.yaml

```

### **Test and Verify Network Connectivity**

### **Step 1: Verify Initial Connectivity**

```bash
kubectl exec -it frontend-app -n frontend -- ping backend-app.backend.svc.cluster.local
```

If connectivity exists, you’ll see successful pings.

### **Step 2: Verify Restricted Connectivity (With Policy)**

After applying the **NetworkPolicy**, retry the same test:

```bash

kubectl exec -it frontend-app -n frontend -- ping backend-app.backend.svc.cluster.local
```

Now, the connection should **fail** because traffic from `frontend` to `backend` is blocked.

### 

---

### **Clean Up**

```bash

kubectl delete namespace frontend backend

```
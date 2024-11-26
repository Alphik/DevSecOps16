# Jenkins Pipeline Tutorial

## 1. Prerequisites

- Jenkins is installed and running on your system.
- You have admin access to Jenkins.
- Git is installed and configured.
- A basic understanding of Jenkins jobs.

---

## 2. Types of Pipelines in Jenkins

1. **Declarative Pipeline**:
   - Easier to write and more structured.
   - Preferred for most use cases.
2. **Scripted Pipeline**:
   - Written in Groovy and more flexible but less readable.

We'll focus on **Declarative Pipelines**.

---

## 3. Pipeline Basics

A Jenkins Pipeline is defined in a file named `Jenkinsfile`. This file lives in the root of your project repository and defines the stages and steps for your build.

### Basic Declarative Pipeline Structure

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
```

## 4. Setting Up Your First Pipeline

### Step 1: Create a New Jenkins Job

Open Jenkins in your browser.
Click New Item.
Enter a name for your job.
Select Pipeline and click OK.

### Step 2: Configure the Pipeline

Scroll down to the Pipeline section.
Select Pipeline script from SCM if your Jenkinsfile is in a Git repository. Enter the repository URL and branch.
If not using Git, paste your pipeline script into the Pipeline script section.

## 5. Key Pipeline Concepts

### a. Agent

The agent block specifies where the pipeline will run.

any: Runs on any available agent.
label: Runs on a specific labeled agent.
docker: Runs inside a Docker container.
Example:

```groovy
pipeline {
    agent {
        docker {
            image 'node:14'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building inside Docker...'
            }
        }
    }
}
```

### b. Stages and Steps

Stages: Represent major phases like Build, Test, and Deploy.
Steps: Define the actions within a stage.
Example:

```groovy
stages {
    stage('Build') {
        steps {
            sh 'npm install'
        }
    }
    stage('Test') {
        steps {
            sh 'npm test'
        }
    }
    stage('Deploy') {
        steps {
            sh 'npm run deploy'
        }
    }
}
```

## c. Post Actions

The post block defines actions to run after the pipeline finishes, like notifications or cleanups.

Example:

```groovy
post {
    success {
        echo 'Pipeline completed successfully!'
    }
    failure {
        echo 'Pipeline failed.'
    }
}
```

## 6. Example: Complete CI/CD Pipeline

Here’s a pipeline example for a Node.js application:

```groovy
pipeline {
    agent any
    environment {
        NODE_ENV = 'production'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'npm run deploy'
            }
        }
    }
    post {
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
```

## 7. Integrating with Docker

To build and run Docker containers in your pipeline:

```groovy
pipeline {
    agent {
        docker {
            image 'maven:3.6.3-jdk-11'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
}
```

## 8. Running the Pipeline

Save your job configuration in Jenkins.
Click Build Now to run the pipeline.
View the progress in the Build History and Console Output.

## 9. Best Practices

- Store your Jenkinsfile in the project repository.
- Use environment variables for sensitive data (e.g., credentials).
- Use Docker agents for consistent builds.
- Write small, reusable pipeline scripts.

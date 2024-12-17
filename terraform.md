# Terraform with AWS:

## Prerequisites

Before starting, ensure you have the following:

1. **AWS Account**: You need access to an AWS account.
2. **Terraform Installed**: Download and install Terraform from [Terraform Downloads](https://www.terraform.io/downloads).
3. **AWS CLI Installed**: Download and configure the AWS CLI from [AWS CLI Installation](https://aws.amazon.com/cli/).
4. **IAM User with Programmatic Access**: Ensure you have an AWS IAM user with sufficient permissions (e.g., EC2FullAccess, S3FullAccess).
5. **Basic Understanding of AWS Services**: Familiarity with services like EC2, S3, and IAM is recommended.

---

## Step 1: Set Up AWS CLI

1. Configure AWS CLI with your credentials:

```bash
aws configure
```

You will be prompted to provide:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region** (e.g., `us-east-1`)
- **Default output format** (leave blank for JSON)

---

## Step 2: Create a Terraform Project

1. Create a project directory:

```bash
mkdir terraform-aws-tutorial && cd terraform-aws-tutorial
```

2. Initialize the directory as a Terraform project:

```bash
terraform init
```

---

## Step 3: Write the Terraform Configuration

### Example: Provision an EC2 Instance and an S3 Bucket

1. Create a file named `main.tf` in your project directory and add the following configuration:

```hcl
# Specify the provider
provider "aws" {
  region = "us-east-1" # Replace with your desired region
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-terraform-bucket-name"
  acl    = "private"

  tags = {
    Name        = "MyBucket"
    Environment = "Dev"
  }
}

# Create an EC2 instance
resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI
  instance_type = "t2.micro"

  tags = {
    Name = "MyInstance"
  }
}

# Output the instance's public IP
output "instance_public_ip" {
  value = aws_instance.my_instance.public_ip
}
```

2. Replace the `bucket` value with a globally unique name for your S3 bucket.

3. Replace the `ami` value with an appropriate AMI ID for your region. You can find AMI IDs using the AWS Management Console or CLI.

---

## Step 4: Initialize Terraform

1. Run the following command to download the AWS provider plugin:

```bash
terraform init
```

---

## Step 5: Validate the Configuration

1. Validate your configuration for syntax errors:

```bash
terraform validate
```

If everything is correct, you will see:

```
Success! The configuration is valid.
```

---

## Step 6: Plan the Deployment

1. Generate a plan to see what Terraform will create:

```bash
terraform plan
```

This will output a detailed plan of the resources Terraform will provision.

---

## Step 7: Apply the Configuration

1. Apply the configuration to create the resources:

```bash
terraform apply
```

2. Type `yes` when prompted to confirm the operation.

---

## Step 8: Verify the Resources

1. Verify the S3 bucket:
   - Go to the **AWS Management Console** > **S3**.
   - Check if the bucket is created.

2. Verify the EC2 instance:
   - Go to the **AWS Management Console** > **EC2**.
   - Check if the instance is running.

3. Check the public IP address output in the terminal:

```bash
Outputs:
instance_public_ip = "<public_ip_here>"
```

Access the instance using SSH:

```bash
ssh -i <path-to-keypair> ec2-user@<public_ip_here>
```

---

## Step 9: Clean Up Resources

1. Destroy the resources to avoid unnecessary charges:

```bash
terraform destroy
```

2. Type `yes` when prompted to confirm the operation.

---

## Additional Notes

### Best Practices

1. **Use Variables**:
   - Replace hardcoded values with variables for flexibility.

   Example:

   ```hcl
   variable "region" {
     default = "us-east-1"
   }

   provider "aws" {
     region = var.region
   }
   ```

2. **State File Management**:
   - Use a backend like AWS S3 with DynamoDB for state file locking in production.

   Example:

   ```hcl
   terraform {
     backend "s3" {
       bucket         = "my-terraform-state-bucket"
       key            = "state/terraform.tfstate"
       region         = "us-east-1"
       dynamodb_table = "terraform-lock"
     }
   }
   ```

3. **Modularize Code**:
   - Break down Terraform configuration into reusable modules.

   Example:

   ```hcl
   module "ec2_instance" {
     source       = "./modules/ec2"
     instance_type = "t2.micro"
     ami           = "ami-0c55b159cbfafe1f0"
   }
   ```

### Debugging Tips

1. Use `terraform fmt` to format your code.
2. Use `terraform show` to inspect the state file.
3. Use `TF_LOG=DEBUG` for detailed logs during execution:

   ```bash
   TF_LOG=DEBUG terraform apply
   ```

---


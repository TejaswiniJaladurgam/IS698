# Deploying a Scalable AWS Architecture with Infrastructure as Code
## Project Overview 
This project involves designing, implementing, and testing a cloud-based architecture on AWS using a combination of services including EC2, VPC, RDS, S3, Lambda, and CloudFormation. The goal is to deploy a scalable architecture using Terraform for Infrastructure as Code (IaC) and CloudFormation for managing EC2 instances, RDS, and Lambda functions.

## **File Structure** (The files are located in the Project Directory)

- **Terraform scripts**:  The `main.tf` file contains the scripts to deploy the **VPC**, **subnets**, and **security groups**.

- **CloudFormation Template**:   The file `infra-setup1.yaml` contains the scripts to deploy **EC2 instances**, **RDS**, and **Lambda functions**.

- **Architecture Diagram**:    The file `Architecture Diagram.drawio (3).png` contains the architecture diagram for this project.

- **Python scripts**:   All the `.py` files use **Boto3** to interact with AWS services like **EC2**, **S3**, and **Lambda**.


## **Technologies Used**
- **AWS EC2**: Virtual machines running your application.
- **AWS RDS**: Managed relational database service.
- **AWS Lambda**: Serverless computing for handling S3 events.
- **AWS S3**: Object storage for files and logs.
- **AWS CloudFormation**: Infrastructure management as code.
- **AWS VPC**: Virtual Private Cloud for networking.
- **Terraform**: Infrastructure as code for managing AWS resources.
- **Python Boto3**: AWS SDK for Python to interact with AWS services.
- **AWS CLI**:A command-line tool for managing AWS resources.

  ## Conclusion
  This project demonstrates the power of Infrastructure as Code (IaC) with Terraform and CloudFormation, combined with AWS services like EC2, RDS, S3, and Lambda. It ensures scalable, secure, and automated deployment of infrastructure, making it easier to manage and replicate environments

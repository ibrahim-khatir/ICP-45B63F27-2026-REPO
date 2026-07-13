# Serverless Function API

A serverless REST API built with **AWS Lambda** and **Amazon API Gateway**. This project demonstrates how to create a scalable, pay-per-use backend without managing servers.

## Project Overview

Traditional APIs require servers that must be provisioned, monitored, and maintained. With AWS Lambda and API Gateway, the backend only runs when a request is received, reducing operational overhead and cost.

This project exposes REST endpoints for managing a simple list of tasks.


## AWS Services Used

* AWS Lambda
* Amazon API Gateway (HTTP API)
* AWS IAM
* Amazon CloudWatch Logs

## Features

* Serverless architecture
* REST API endpoints
* JSON responses
* Environment variable support
* CloudWatch logging
* IAM least-privilege permissions

## API Endpoints

| Method | Endpoint | Description        |
| ------ | -------- | ------------------ |
| GET    | /tasks   | Retrieve all tasks |

Deployment Steps

1. Create an AWS Lambda function.
2. Upload the Python source code.
3. Create an HTTP API using Amazon API Gateway.
4. Connect the API Gateway route to the Lambda function.
5. Deploy the API.
6. Test the endpoint using a browser, curl, or Postman.
7. Monitor execution logs in Amazon CloudWatch.

## Monitoring

Amazon CloudWatch Logs capture each Lambda invocation, making it easy to troubleshoot requests and verify successful execution.

## Security

The Lambda function uses an IAM execution role that follows the principle of least privilege by granting only the permissions required for logging.



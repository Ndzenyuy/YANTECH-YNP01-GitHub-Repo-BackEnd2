# 📬 Notification System with LocalStack

A microservices-based Python project using FastAPI, Docker, and LocalStack to handle notification requests (EMAIL, SMS, PUSH) through AWS services simulated locally.

## 📦 Prerequisites

# Add Docker's official GPG key:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo apt-get update
sudo apt-get install docker-compose-plugin -y

sudo apt install docker-compose -y

sudo usermod -aG docker $USER   

# Make sure python3-full and venv are installed
sudo apt install -y python3-full python3-venv

# Create a virtual environment
python3 -m venv ~/.venvs/localstack

# Activate the environment
source ~/.venvs/localstack/bin/activate

# Upgrade pip inside the venv
pip install --upgrade pip

# Now safely install localstack inside the venv
pip install localstack
```

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ndzenyuy/YNP-app.git
cd YNP-app
```

### 2. Set up `.env` files for each service

Create `.env` files inside each of the `admin`, `requestor`, and `worker` folders. Here's an example:

```env
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_REGION=us-east-1
SQS_QUEUE_URL=http://localstack:4566/000000000000/notifications-queue
DYNAMODB_TABLE=Applications
REQUEST_LOG_TABLE=RequestLogs
```

### 3. Build and Run Services

```bash
docker-compose build --no-cache
docker-compose up -d
```

## 🧪 Test the Services

### ✅ Check if Services Are Running

```bash
curl http://localhost:4566/_localstack/health
curl http://localhost:8000/health     # Requestor
curl http://localhost:8001/health     # Admin

```

# Test messages

## admin register a new app
curl -X POST http://localhost:8001/app \
  -H "Content-Type: application/json" \
  -d '{
    "Application": "App1",
    "App_name": "CHA - Student Platform",
    "Email": "no-reply@cha.com",
    "Domain": "cha.com"
  }'
  

## requester send a new request of type email  
curl -X POST http://localhost:8000/requester \
  -H "Content-Type: application/json" \
  -d '{
    "Application": "App2",
    "Recipient": "user@example.com",
    "Subject": "Test Subject",
    "Message": "Hello, this is a test message!",
    "OutputType": "EMAIL",
    "Interval": {
      "Once": true
    },
    "EmailAddresses": ["user@example.com"]
  }'

## requester send a new request of type SMS   
curl -X POST http://localhost:8000/requester \
  -H "Content-Type: application/json" \
  -d '{
    "Application": "App1",
    "Recipient": "1234567890",
    "Subject": "Test SMS",
    "Message": "This is an SMS test.",
    "OutputType": "SMS",
    "PhoneNumber": "+15555555555",
    "Interval": {
      "Days": [1, 15]
    }
  }'

## requester send a new request of type PUSH   
curl -X POST http://localhost:8000/requester \
  -H "Content-Type: application/json" \
  -d '{
    "Application": "App1",
    "Recipient": "pushUser1",
    "Subject": "New Alert",
    "Message": "You have a new notification!",
    "OutputType": "PUSH",
    "PushToken": "example_token_123",
    "Interval": {
      "Weeks": [2, 4]
    }
  }'


## 🔍 Debugging & Logs

### Access Container Logs

```bash
docker logs worker
docker logs admin
docker logs requestor
```

### Interact with LocalStack Services

```bash
# List queues
aws --endpoint-url=http://localhost:4566 sqs list-queues

# Receive messages
aws --endpoint-url=http://localhost:4566 sqs receive-message \
  --queue-url http://localstack:4566/000000000000/notifications-queue

# Check DynamoDB tables
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name Applications
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name RequestLogs
```

## 🔁 Developer Workflow (Auto Refresh on Code Change)

**Clean All**

```bash
docker-compose down --volumes --remove-orphans
docker system prune -af
docker volume prune -f

```

## 📁 Directory Structure

```
├── admin/
│   ├── app/
│   ├── .env
│   ├── Dockerfile
├── requestor/
│   ├── app/
│   ├── .env
│   ├── Dockerfile
├── worker/
│   ├── app/
│   ├── .env
│   ├── Dockerfile
├── localstack/
│   ├── bootstrap.sh
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## ✅ Requirements

```txt
fastapi
boto3
python-dotenv
uvicorn
pydantic==1.10.13
email-validator
```

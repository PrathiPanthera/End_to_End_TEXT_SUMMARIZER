# End_to_End_TEXT_SUMMARIZER# End-to-End Text Summarization using Transformers

An end-to-end NLP project that generates concise summaries from long-form text using a fine-tuned PEGASUS Transformer model. The project demonstrates the complete machine learning lifecycle—from data ingestion to model deployment—using a modular, production-ready architecture.

> **Repository:** https://github.com/PrathiPanthera/End_to_End_TEXT_SUMMARIZER

---

# Project Highlights

* End-to-end NLP pipeline
* Modular project architecture
* Data validation and preprocessing
* Transformer-based text summarization
* Model training and evaluation
* FastAPI REST API for inference
* Docker-ready project structure
* AWS deployment with GitHub Actions CI/CD

---

# Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* FastAPI
* Uvicorn
* YAML
* Docker
* AWS (EC2 & ECR)
* GitHub Actions

---

# Project Workflow

The project is organized into independent pipeline stages.

```
Data Ingestion
        ↓
Data Validation
        ↓
Data Transformation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Prediction Pipeline
        ↓
FastAPI Deployment
```

---

# Repository Structure

```
End_to_end_Text_Summariser_Project/
│
├── .github/
│   └── workflows/
│
├── config/
│   ├── config.yaml
│
├── research/
│
├── src/
│   └── text_summarizer/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
│
├── app.py
├── main.py
├── params.yaml
├── requirements.txt
├── setup.py
├── Dockerfile
├── template.py
└── README.md
```

---

# Development Workflow

The implementation follows these stages:

1. Configure project settings (`config.yaml`)
2. Update model parameters (`params.yaml`)
3. Define entities
4. Configure the Configuration Manager
5. Implement project components
6. Build training and prediction pipelines
7. Execute the training pipeline (`main.py`)
8. Serve predictions using FastAPI (`app.py`)

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/PrathiPanthera/End_to_End_TEXT_SUMMARIZER

cd End_to_end_Text_Summariser_Project
```

---

## 2. Create a Conda Environment

```bash
conda create -n summary python=3.8 -y
```

Activate the environment:

```bash
conda activate summary
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Training Pipeline

Execute the complete ML pipeline:

```bash
python main.py
```

The pipeline automatically performs:

* Data Ingestion
* Data Validation
* Data Transformation
* Model Training
* Model Evaluation

---

# Launch the API

Start the FastAPI application:

```bash
python app.py
```

After the server starts successfully, open:

```
http://localhost:2122/docs
```

(or the port configured in `app.py`)

Swagger UI provides an interactive interface to test the prediction endpoint.

---

# API Endpoints

## Home

```
GET /
```

Redirects to the interactive API documentation.

---

## Predict Summary

```
POST /predict
```

Accepts text input and returns the generated summary.

---

# Deployment (AWS + Docker + GitHub Actions)

This project supports automated deployment using AWS services and GitHub Actions.

## Deployment Flow

```
GitHub Repository
        ↓
GitHub Actions
        ↓
Build Docker Image
        ↓
Push Image to Amazon ECR
        ↓
Launch EC2 Instance
        ↓
Pull Docker Image
        ↓
Run FastAPI Application
```

---

## Step 1 – AWS Login

Sign in to your AWS Console.

---


## Step 2 – Create an IAM User

Grant the following permissions:

* AmazonEC2FullAccess
* AmazonEC2ContainerRegistryFullAccess

---


## Step 3 – Create an Amazon ECR Repository

Create an Elastic Container Registry repository and save its URI.

Save the URL: 245594728390.dkr.ecr.eu-north-1.amazonaws.com/textsummarizer


## Step 4 – Launch an EC2 Instance

Recommended Operating System:

* Ubuntu

---


## Step 5 – Install Docker

Optional:

```bash
sudo apt-get update -y
sudo apt-get upgrade
```

Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

Verify installation:

```bash
docker --version
```

---


## Step 6 – Configure GitHub Self-Hosted Runner

Navigate to:

```
Repository
    ↓
Settings
    ↓
Actions
    ↓
Runners
    ↓
New Self-hosted Runner
```

Follow the generated setup commands on the EC2 instance.

---


## Step 7 – Configure GitHub Secrets

Add the following secrets to your repository:

```
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION

AWS_ECR_LOGIN_URI

ECR_REPOSITORY_NAME
```

Example:

```
AWS_REGION=us-east-1

AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME=text-summarizer
```


---

# Future Enhancements

* Deploy on Kubernetes
* Add experiment tracking
* Integrate MLflow
* Improve monitoring and logging
* Support multilingual summarization
* Develop a frontend interface using Streamlit or React

---

# Author

**Prathibha M**

Aspiring Data Scientist | Machine Learning & NLP Enthusiast

GitHub:
https://github.com/PrathiPanthera

---

If you found this project helpful, consider giving the repository a ⭐.

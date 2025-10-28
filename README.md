# 🎓 Student Performance Estimator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)

**An end-to-end machine learning project for predicting student mathematics performance using demographics and prior test scores**

[Live Demo](http://ec2-13-127-106-188.ap-south-1.compute.amazonaws.com:8080) • [Watch Video Demo](https://youtu.be/-xSl99Kn3Bo) • [Report Bug](../../issues) • [Request Feature](../../issues)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Data Schema](#-data-schema)
- [Live Demo](#-live-demo)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Training the Model](#training-the-model)
  - [Running the Application](#running-the-application)
- [Docker Deployment](#-docker-deployment)
- [AWS Deployment (CI/CD)](#-aws-deployment-cicd)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## 🎯 Overview

This project demonstrates a complete machine learning workflow from data ingestion to production deployment. It predicts a student's mathematics test score based on demographic information (gender, ethnicity, parental education) and prior performance (reading and writing scores).

**What makes this project special:**
- 🔄 Automated end-to-end ML pipeline
- 🤖 Compares 8 regression algorithms and auto-selects the best
- 🌐 Production-ready Flask web application
- 🐳 Fully containerized with Docker
- ☁️ CI/CD pipeline using GitHub Actions + AWS ECR
- 📊 Interactive data visualizations and model insights
- 🔧 Reusable preprocessing pipeline with serialized artifacts

---

## ✨ Key Features

- **🔄 Complete ML Pipeline**: Automated data ingestion → transformation → model training → deployment
- **🤖 Multi-Model Comparison**: Evaluates 8 regression algorithms (Random Forest, XGBoost, CatBoost, Gradient Boosting, AdaBoost, Linear Regression, Decision Tree, KNN)
- **📊 Smart Model Selection**: Automatically selects and persists the best model based on R² score
- **🎨 User-Friendly Web Interface**: Clean Flask UI for real-time predictions
- **💾 Reusable Artifacts**: Serialized preprocessing pipeline and trained model for consistent inference
- **🐳 Docker Support**: Containerized application for easy deployment
- **☁️ Production CI/CD**: GitHub Actions workflow for automated AWS ECR deployment
- **📈 Comprehensive Logging**: Detailed execution logs for debugging and monitoring
- **🔧 Custom Exception Handling**: Rich error context for troubleshooting

---

## 🛠 Tech Stack

**Core Technologies:**
- **Python 3.11** - Programming language
- **Flask 2.x** - Web framework for REST API and UI
- **scikit-learn** - Machine learning algorithms and preprocessing
- **pandas & numpy** - Data manipulation and numerical operations

**ML Models:**
- XGBoost, CatBoost - Gradient boosting frameworks
- Random Forest, Gradient Boosting, AdaBoost - Ensemble methods
- Linear Regression - Baseline model
- Decision Tree, KNN - Traditional ML algorithms

**DevOps & Deployment:**
- **Docker** - Containerization
- **GitHub Actions** - CI/CD automation
- **AWS ECR** - Container registry
- **AWS EC2** - Application hosting

**Utilities:**
- **dill** - Python object serialization
- **matplotlib & seaborn** - Data visualization (in notebooks)

---

## 🏗 Architecture

### System Architecture

```mermaid
flowchart TD
	A[User Browser] --> B[Flask App]
	B --> C{Route}
	C -- GET / --> D[Index Page]
	C -- GET/POST /predict-data --> E[Prediction Handler]
	E --> F[CustomData -> Pandas DataFrame]
	F --> G[Load preprocessor.pkl]
	F --> H[Load model.pkl]
	G --> I[Transform features]
	I --> J[model.predict]
	J --> K[Render result in home.html]
```

### Training Pipeline

```mermaid
flowchart LR
	A[data/stud.csv] --> B[Train/Test Split]
	B --> C[Build Preprocessor]
	C --> D[Fit on train]
	D --> E[Save preprocessor.pkl]
	D --> F[Transform train/test]
	F --> G[Train multiple models]
	G --> H[Evaluate R²]
	H --> I{Select best}
	I --> J[Save model.pkl]
```

### Request Flow for Prediction

```mermaid
sequenceDiagram
	participant U as User
	participant F as Flask
	participant P as PredictPipeline
	participant PRE as preprocessor.pkl
	participant M as model.pkl
	U->>F: POST /predict-data (form fields)
	F->>P: predict(df)
	P->>PRE: load + transform
	P->>M: load + predict
	P-->>F: prediction array
	F-->>U: Render result in home.html
```

### CI/CD Pipeline

```mermaid
flowchart LR
	X[Push to main] --> CI[CI: checkout + lint/tests]
	CI --> BLD[Build Docker image]
	BLD --> ECR[AWS ECR]
	ECR --> DEP[Self-hosted runner]
	DEP --> RUN[Run container :8080]
```

---

## 📊 Data Schema

The dataset `data/stud.csv` contains the following columns:

| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| **gender** | Categorical | Student's gender | `male`, `female` |
| **race_ethnicity** | Categorical | Ethnic group classification | `group A`, `group B`, `group C`, `group D`, `group E` |
| **parental_level_of_education** | Categorical | Highest education level of parents | `associate's degree`, `bachelor's degree`, `high school`, `master's degree`, `some college`, `some high school` |
| **lunch** | Categorical | Lunch program participation | `standard`, `free/reduced` |
| **test_preparation_course** | Categorical | Test prep course completion | `none`, `completed` |
| **reading_score** | Numeric | Reading test score | 0–100 |
| **writing_score** | Numeric | Writing test score | 0–100 |
| **math_score** | Numeric (Target) | Mathematics test score to predict | 0–100 |

**Target Variable:** The model predicts `math_score` based on the other 7 features.

---

## 🌐 Live Demo

### Try the Deployed Application

A live instance of this project is available at:

**🔗 [http://ec2-13-127-106-188.ap-south-1.compute.amazonaws.com:8080](http://ec2-13-127-106-188.ap-south-1.compute.amazonaws.com:8080)**

> **⚠️ Note:** The EC2 instance may be stopped at times due to cost savings or maintenance. If the site is unreachable, please follow the [Getting Started](#-getting-started) section to run the application locally.

### 🎥 Video Walkthrough

Watch a complete demonstration of the **Student Performance Estimator** in action:

**Features showcased:**
- ☁️ Live deployment on AWS EC2
- 🌐 Flask web application interface
- 🤖 Real-time student performance predictions
- 🔍 Feature processing and model inference flow

**Click the thumbnail below to watch:**

[![Student Performance Estimator - ML Project Demo](https://img.youtube.com/vi/-xSl99Kn3Bo/maxresdefault.jpg)](https://youtu.be/-xSl99Kn3Bo)

> 💡 **Perfect for:** Getting a quick overview of the deployed application before trying it yourself!

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **pip** (latest version recommended)
- **(Optional) Docker Desktop** ([Download](https://www.docker.com/products/docker-desktop/)) - Required only for containerized deployment

### Installation

1️⃣ **Clone the repository**
```

## Data schema

The dataset `data/stud.csv` contains the following columns:

- gender: [male|female]
- race_ethnicity: [group A|B|C|D|E]
- parental_level_of_education: e.g., "associate's degree", "bachelor's degree", ...
- lunch: [standard|free/reduced]
- test_preparation_course: [none|completed]
- reading_score: integer 0–100
- writing_score: integer 0–100
- math_score: integer 0–100 (target)

The model predicts `math_score` from the other fields.

## Try Deployed Project

A deployed instance of this project is available at:

http://ec2-13-127-106-188.ap-south-1.compute.amazonaws.com:8080

Please note: the EC2 instance may be stopped or unavailable at times (cost savings, maintenance, or other reasons). If the site is unreachable while you read this README, follow the "Try Locally" sections below to run the app yourself.

## Demo Video

🎥 Watch a quick walkthrough of the **Student Performance Estimator** ML project in action!

This demo showcases:
- � Live deployment on AWS EC2
- 🌐 Flask web application interface
- � Real-time student performance predictions
- 🔍 How the model processes input features and returns math score predictions

**Click on the thumbnail below to watch the demo:**

[![Student Performance Estimator - ML Project Demo](https://img.youtube.com/vi/-xSl99Kn3Bo/maxresdefault.jpg)](https://youtu.be/-xSl99Kn3Bo)

> 💡 **Perfect for:** Getting a quick overview of the deployed application before trying it yourself!

---

## 🚀 Getting Started (Continued)

### Installation Steps

1️⃣ **Clone the repository**

```powershell
git clone https://github.com/mahesh-javiniki/student-exam-performance-prediction-deployment-cicd.git
cd student-exam-performance-prediction-deployment-cicd
```

2️⃣ **Create and activate a virtual environment**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3️⃣ **Install dependencies**

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### Training the Model

4️⃣ **Train the model and generate artifacts**

This step will:
- Load `data/stud.csv`
- Split into train/test → `artifacts/train.csv`, `artifacts/test.csv`
- Fit preprocessing pipeline and save → `artifacts/preprocessor.pkl`
- Train and evaluate 8 regression models
- Select best model by test R² and save → `artifacts/model.pkl`

```powershell
python -m src.components.data_ingestion
```

> **Expected output:** Training logs will appear in the console and be saved to `logs/` directory. The best model's R² score will be displayed.

### Running the Application

5️⃣ **Launch the Flask web application**

```powershell
python app.py
```

6️⃣ **Access the application**

Open your browser and navigate to: **http://localhost:8080**

You can now:
- Fill out the student information form
- Submit to get a predicted mathematics score
- See the prediction result displayed instantly

---

## 📦 Project Structure

```
student-performance-estimator-docker/
├─ app.py                     # Flask application (routes + UI logic)
├─ Dockerfile                 # Container image definition
├─ requirements.txt           # Python dependencies
├─ setup.py                   # Package setup for editable install
├─ LICENSE                    # MIT License
├─ .gitignore                 # Git ignore patterns
├─ data/
│  └─ stud.csv               # Raw dataset (training input)
├─ artifacts/                # Generated files (created after training)
│  ├─ data.csv               # Copy of raw data
│  ├─ train.csv              # Training split (80%)
│  ├─ test.csv               # Testing split (20%)
│  ├─ preprocessor.pkl       # Serialized preprocessing pipeline
│  └─ model.pkl              # Serialized best-performing model
├─ src/
│  ├─ __init__.py
│  ├─ logger.py              # Logging configuration (file + console)
│  ├─ exception.py           # Custom exception with rich context
│  ├─ utils.py               # Utility functions (save/load objects, evaluate models)
│  ├─ components/
│  │  ├─ __init__.py
│  │  ├─ data_ingestion.py   # Data loading and train/test split
│  │  ├─ data_transformation.py # Preprocessing pipeline (OHE + scaling)
│  │  └─ model_trainer.py    # Model training, evaluation, and selection
│  └─ pipeline/
│     ├─ predict_pipeline.py # Inference pipeline (load artifacts + predict)
│     └─ train_pipeline.py   # Training orchestration (placeholder)
├─ templates/
│  ├─ index.html             # Landing page
│  └─ home.html              # Prediction form and results display
├─ notebooks/
│  ├─ EDA.ipynb              # Exploratory Data Analysis
│  └─ MODEL_TRAIN.ipynb      # Model training experiments
├─ logs/                     # Application logs (auto-generated)
└─ .github/
   └─ workflows/
      └─ main.yaml           # CI/CD pipeline configuration
```

---

## 🔍 How It Works

### Data Preprocessing Pipeline

The `src/components/data_transformation.py` module builds a scikit-learn `ColumnTransformer` that:

**Numeric Features** (`reading_score`, `writing_score`):
- Imputation: Median strategy for missing values
- Scaling: StandardScaler for normalization

**Categorical Features** (`gender`, `race_ethnicity`, `parental_level_of_education`, `lunch`, `test_preparation_course`):
- Imputation: Most frequent strategy for missing values
- Encoding: OneHotEncoder for categorical conversion
- Scaling: StandardScaler with `with_mean=False` (for sparse matrices)

### Model Training and Selection

The `src/components/model_trainer.py` evaluates **8 regression algorithms**:

1. **Random Forest Regressor**
2. **Decision Tree Regressor**
3. **Gradient Boosting Regressor**
4. **Linear Regression**
5. **K-Neighbors Regressor**
6. **XGBoost Regressor**
7. **CatBoost Regressor**
8. **AdaBoost Regressor**

**Selection Criteria:** The model with the highest R² score on the test set is automatically selected and persisted.

### Prediction Pipeline

The `src/pipeline/predict_pipeline.py` module:
1. Loads `artifacts/preprocessor.pkl` and `artifacts/model.pkl`
2. Transforms incoming features using the preprocessing pipeline
3. Generates predictions using the trained model
4. Returns results to the Flask application

### Flask Application Routes

The `app.py` exposes two main routes:

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Renders the landing page (`index.html`) |
| `/predict-data` | GET | Displays the prediction form (`home.html`) |
| `/predict-data` | POST | Processes form data, runs prediction, and displays result |

---

## 🐳 Docker Deployment

### Important Note

The Docker container expects trained artifacts (`artifacts/preprocessor.pkl` and `artifacts/model.pkl`) to exist. You must train the model locally first or mount the artifacts directory.

### Option A: Build with Pre-trained Artifacts (Recommended)

**Step 1:** Train the model locally first

```powershell
python -m src.components.data_ingestion
```

**Step 2:** Build the Docker image (artifacts will be copied into the image)

**Step 2:** Build the Docker image (artifacts will be copied into the image)

```powershell
docker build -t student-performance-estimator:latest .
```

**Step 3:** Run the container

```powershell
docker run -d -p 8080:8080 --name student-perf-app student-performance-estimator:latest
```

**Step 4:** Access the application at **http://localhost:8080**

### Option B: Mount Artifacts (Dynamic Development)

This approach allows you to retrain the model without rebuilding the Docker image.

**Step 1:** Build the Docker image once

```powershell
docker build -t student-performance-estimator:latest .
```

**Step 2:** Run with mounted artifacts directory

```powershell
docker run -d -p 8080:8080 -v ${PWD}\artifacts:/app/artifacts --name student-perf-app student-performance-estimator:latest
```

**Step 3:** Retrain the model anytime (artifacts update automatically in container)

```powershell
python -m src.components.data_ingestion
```

### Docker Management Commands

```powershell
# Stop the container
docker stop student-perf-app

# Start the container
docker start student-perf-app

# View logs
docker logs student-perf-app

# Remove the container
docker rm student-perf-app

# Remove the image
docker rmi student-performance-estimator:latest
```

---

## ☁️ AWS Deployment (CI/CD)

This project includes a complete CI/CD workflow in `.github/workflows/main.yaml` that automates building, pushing to Amazon ECR, and deploying to EC2.

### Workflow Overview

```mermaid
graph LR
    A[Push to main] --> B[CI: Lint & Tests]
    B --> C[Build Docker Image]
    C --> D[Push to AWS ECR]
    D --> E[Self-hosted Runner]
    E --> F[Pull & Run Container]
```

### Pipeline Jobs

**1. Integration (CI)**
- Runs on: `ubuntu-latest`
- Actions: Code checkout, linting, unit tests
- Purpose: Ensures code quality before deployment

**2. Build and Push to ECR (CD)**
- Runs on: `ubuntu-latest`
- Depends on: Integration job success
- Actions:
  - Configures AWS credentials
  - Logs into Amazon ECR
  - Builds Docker image
  - Tags image as `latest`
  - Pushes to ECR repository

**3. Continuous Deployment**
- Runs on: `self-hosted` (EC2 instance)
- Depends on: Build and Push job success
- Actions:
  - Pulls latest image from ECR
  - Stops existing container (if running)
  - Runs new container on port 8080
  - Cleans up unused Docker resources

### Required GitHub Secrets

Configure the following secrets in your repository settings (`Settings` → `Secrets and variables` → `Actions`):

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | IAM user access key with ECR permissions | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret access key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_REGION` | AWS region for ECR and EC2 | `us-east-1`, `ap-south-1` |
| `AWS_ECR_LOGIN_URI` | ECR registry URI | `123456789012.dkr.ecr.us-east-1.amazonaws.com` |
| `ECR_REPOSITORY_NAME` | ECR repository name | `student-performance-estimator` |

### Required IAM Permissions

Your IAM user needs the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:PutImage",
        "ecr:InitiateLayerUpload",
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload"
      ],
      "Resource": "*"
    }
  ]
}
```

### Setting Up EC2 Self-Hosted Runner

**Prerequisites:**
- EC2 instance (Amazon Linux 2023 or Ubuntu 22.04 recommended)
- Security group allowing inbound traffic on port 8080
- Docker installed on the instance

**Steps:**

1️⃣ **Launch an EC2 instance**
```bash
# Instance type: t2.medium or larger
# AMI: Amazon Linux 2023 or Ubuntu 22.04
# Storage: 20GB minimum
```

2️⃣ **Install Docker on the EC2 instance**

```bash
# For Amazon Linux 2023
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user

# For Ubuntu 22.04
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ubuntu
```

3️⃣ **Register as GitHub Actions Runner**

- Navigate to your repository on GitHub
- Go to `Settings` → `Actions` → `Runners` → `New self-hosted runner`
- Follow the provided commands to download and configure the runner
- Start the runner service

```bash
# Example commands (specific to your repo)
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz
./config.sh --url https://github.com/YOUR-USERNAME/YOUR-REPO --token YOUR-TOKEN
sudo ./svc.sh install
sudo ./svc.sh start
```

4️⃣ **Configure AWS CLI on EC2 (Optional)**

```bash
aws configure
# Enter your AWS credentials when prompted
```

5️⃣ **Update Security Group**

Ensure your EC2 security group allows:
- Inbound: Port 8080 (HTTP for app access)
- Inbound: Port 22 (SSH for management)
- Outbound: All traffic (for pulling images)

### Manual Deployment (Alternative)

If you prefer manual deployment without GitHub Actions:

**Step 1:** Authenticate Docker with ECR

```powershell
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-ecr-uri>
```

**Step 2:** Build and tag the image

```powershell
docker build -t student-performance-estimator:latest .
docker tag student-performance-estimator:latest <your-ecr-uri>/student-performance-estimator:latest
```

**Step 3:** Push to ECR

```powershell
docker push <your-ecr-uri>/student-performance-estimator:latest
```

**Step 4:** SSH into EC2 and run

```bash
# Pull the image
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <ecr-uri>
docker pull <ecr-uri>/student-performance-estimator:latest

# Run the container
docker run -d -p 8080:8080 --name student-perf-app \
  -e AWS_ACCESS_KEY_ID='<your-key>' \
  -e AWS_SECRET_ACCESS_KEY='<your-secret>' \
  -e AWS_REGION='<region>' \
  <ecr-uri>/student-performance-estimator:latest
```

> **⚠️ Security Note:** Avoid hardcoding AWS credentials. Use IAM roles attached to EC2 instances or AWS Secrets Manager instead.

---

## 🧪 Testing

### Running Tests

(Note: Test framework setup is a recommended addition to this project)

To add tests, create a `tests/` directory and use pytest:

```powershell
# Install pytest
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Manual Testing

Test the prediction pipeline manually:

```powershell
python -c "from src.pipeline.predict_pipeline import PredictPipeline, CustomData; import pandas as pd; data = CustomData(gender='female', race_ethnicity='group B', parental_level_of_education='bachelor''s degree', lunch='standard', test_preparation_course='completed', reading_score=85, writing_score=90); df = data.get_data_as_data_frame(); pipeline = PredictPipeline(); print(f'Predicted Math Score: {pipeline.predict(df)[0]}')"
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

**1. File not found: `artifacts/model.pkl` or `artifacts/preprocessor.pkl`**

**Cause:** Model artifacts don't exist yet.

**Solution:**
```powershell
python -m src.components.data_ingestion
```

**2. XGBoost/CatBoost installation errors on Windows**

**Cause:** Missing build tools or incompatible Python version.

**Solution:**
```powershell
# Ensure Python 3.11 is installed
python --version

# Upgrade pip, wheel, and setuptools
pip install --upgrade pip wheel setuptools

# Install Microsoft C++ Build Tools if needed
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

**3. Port 8080 already in use**

**Cause:** Another process is using port 8080.

**Solution:**
```powershell
# Find the process using port 8080
netstat -ano | findstr :8080

# Kill the process (replace <PID> with actual process ID)
taskkill /PID <PID> /F

# Or change the port in app.py
# app.run(host='0.0.0.0', port=8081)
```

**4. Docker container fails to start**

**Cause:** Missing artifacts or incorrect paths.

**Solution:**
```powershell
# Check if artifacts exist
ls artifacts/

# View container logs
docker logs student-perf-app

# Restart container
docker restart student-perf-app
```

**5. AWS ECR authentication fails**

**Cause:** Expired credentials or incorrect region.

**Solution:**
```powershell
# Verify AWS CLI configuration
aws sts get-caller-identity

# Re-authenticate with ECR
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-ecr-uri>
```

**6. Model performance is poor**

**Cause:** Insufficient training data or hyperparameter tuning needed.

**Solution:**
- Add more training data to `data/stud.csv`
- Implement hyperparameter tuning in `src/components/model_trainer.py`
- Experiment with feature engineering

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Ideas

- 🧪 Add comprehensive unit and integration tests
- 📊 Implement additional ML models (neural networks, ensemble methods)
- 🎨 Enhance the UI/UX of the web interface
- 📈 Add model performance monitoring and logging
- 🔒 Implement authentication and user management
- 📝 Improve documentation and add tutorials
- 🐛 Fix bugs and improve code quality
- ⚡ Optimize model training and inference speed

### Code Style

- Follow PEP 8 guidelines for Python code
- Add docstrings to functions and classes
- Write descriptive commit messages
- Include tests for new features

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Mahesh Javiniki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **Dataset Source:** Student Performance Dataset (publicly available educational data)
- **Inspiration:** End-to-end MLOps best practices and deployment patterns
- **Technologies:** Thanks to the open-source communities of Flask, scikit-learn, XGBoost, CatBoost, and Docker
- **CI/CD:** GitHub Actions for seamless automation
- **Cloud Provider:** AWS for scalable infrastructure

### Special Thanks

- All contributors who have helped improve this project
- The machine learning and data science community for valuable resources
- Open-source maintainers whose libraries made this project possible

---

## 📧 Contact

**Mahesh Javiniki**

- 📧 Email: [maheshjaviniki@gmail.com](mailto:maheshjaviniki@gmail.com)
- 🐙 GitHub: [@mahesh-javiniki](https://github.com/mahesh-javiniki)
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/mahesh-javiniki)

### Project Links

- **Repository:** [student-exam-performance-prediction-deployment-cicd](https://github.com/mahesh-javiniki/student-exam-performance-prediction-deployment-cicd)
- **Issues:** [Report bugs or request features](https://github.com/mahesh-javiniki/student-exam-performance-prediction-deployment-cicd/issues)
- **Pull Requests:** [Contribute to the project](https://github.com/mahesh-javiniki/student-exam-performance-prediction-deployment-cicd/pulls)

---

<div align="center">

**⭐ If you found this project helpful, please consider giving it a star!**

Made with ❤️ by [Mahesh Javiniki](https://github.com/mahesh-javiniki)

</div>
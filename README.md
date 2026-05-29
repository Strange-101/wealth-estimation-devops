# AI-Based Household Wealth Estimation System

A Computer Vision + DevOps project that predicts household wealth categories using house exterior images.

The project uses:

* EfficientNet-B0
* PyTorch
* FastAPI
* Streamlit
* Docker Compose
* GitHub Actions

---

# Features

* Image-based wealth classification
* Deep Learning prediction system
* FastAPI backend
* Streamlit frontend
* Dockerized microservices
* Docker Compose orchestration
* CI workflow using GitHub Actions

---

# Tech Stack

* Python
* PyTorch
* FastAPI
* Streamlit
* Docker
* Docker Compose
* GitHub Actions

---

# Run Using Docker Compose

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:8501
```

Backend:

```text
http://localhost:8000/docs
```

---

# Project Structure

```text
backend/        -> FastAPI backend
frontend/       -> Streamlit frontend
ml-service/     -> Trained model
dataset/        -> Image dataset
docker-compose.yml
```

---

# Sample Output

```json
{
  "prediction": "high",
  "confidence": 0.97
}
```

---

# Author

Kunal Mahore
B.Tech CSE

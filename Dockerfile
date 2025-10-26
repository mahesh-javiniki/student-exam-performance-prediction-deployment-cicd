FROM python:3.11-slim-bookworm
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 unzip curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install awscli && \
    pip install -r requirements.txt
CMD ["python3", "app.py"]
FROM python:3.8

# WORKDIR /Users/zhengnaigong/Documents/mnist-fastapi-docker/app
WORKDIR /app

# COPY requirements.txt .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 12347

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "12347"]
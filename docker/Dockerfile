FROM python:3.12-slim

# WORKDIR /Users/zhengnaigong/Documents/mnist-fastapi-docker/app
WORKDIR /app

# COPY requirements.txt .
COPY docker/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .


EXPOSE 12347

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "12347"]
FROM python:3.9-slim
RUN apt-get update && apt-get install -y gcc python3-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
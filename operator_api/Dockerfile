# Use an official Python runtime as a parent image
FROM python:3.11-slim
WORKDIR /app
COPY /app .
RUN pip install --no-cache-dir -r requirements.txt
CMD kopf run api_operator.py --verbose

# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8090
CMD ["python3","app.py"]
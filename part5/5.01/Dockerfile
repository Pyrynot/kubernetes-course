FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dummysite_controller.py .

CMD ["kopf", "run", "dummysite_controller.py"]
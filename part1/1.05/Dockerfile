FROM python:3.12.4-alpine3.19

WORKDIR /app

COPY reqs.txt /app/reqs.txt

RUN pip install --no-cache-dir --upgrade -r /app/reqs.txt

COPY main.py /app/main.py
COPY templates /app/templates

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]

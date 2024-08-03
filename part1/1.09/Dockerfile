FROM python:3.12.4-alpine3.19

WORKDIR /app

COPY reqs.txt /app/reqs.txt

RUN pip install --no-cache-dir --upgrade -r /app/reqs.txt

COPY /app/ /app/

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8020"]
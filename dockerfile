FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask requests

EXPOSE 5000

CMD ["python", "app.py"]

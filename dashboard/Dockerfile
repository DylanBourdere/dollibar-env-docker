FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask pyyaml requests

COPY app.py /app/app.py
COPY templates /app/templates
COPY static /app/static

EXPOSE 8080

CMD ["python", "app.py"]

FROM python:3.14

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY . .

CMD ["python", "main.py"]
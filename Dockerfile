FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

#CMD ["gunicorn", "cyber_portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]



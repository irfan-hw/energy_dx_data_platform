FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /gui

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "/src/manage.py", "runserver", "0.0.0.0:8083"]
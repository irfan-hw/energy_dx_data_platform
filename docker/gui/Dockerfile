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
    pip install --no-cache-dir -r requirements.txt \
    pip install mysqlclient

RUN apt-get update && apt-get install -y default-libmysqlclient-dev

COPY . .

CMD ["python", "/src/energy_dx_gui/manage.py", "runserver", "0.0.0.0:80"]
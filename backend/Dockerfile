FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install -y vim wget dos2unix

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN dos2unix /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["gunicorn", "django_project.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["/docker-entrypoint.sh"]

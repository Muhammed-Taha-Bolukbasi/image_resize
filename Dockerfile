FROM python:alpine

COPY . /app
WORKDIR /app

RUN apk --no-cache upgrade

RUN pip install -r requirements.txt

EXPOSE 4000
CMD ["python3", "url.py"]


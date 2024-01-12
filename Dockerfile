FROM python:alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 4000
CMD ["python3", "url.py"]


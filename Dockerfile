FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

COPY . .

EXPOSE 8000

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
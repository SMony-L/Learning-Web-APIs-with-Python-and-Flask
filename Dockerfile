# alpine image
FROM python:3.8-slim-buster

# Working dir
WORKDIR /app
ADD . /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY . .

CMD ["python3", "app.py"]
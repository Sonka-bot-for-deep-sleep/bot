FROM python:3.12-alpine3.20
WORKDIR /app

COPY requirements.txt ./
RUN pip install requirements.txt

COPY . .

ENTRYPOINT [ "python3", "./src/main.py" ]
FROM  python:3.8.10

COPY requirements.txt requirements.txt

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

#CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "5000", "--reload"]
FROM python:3.8.9-slim

WORKDIR /

COPY /21-03-iterators .

CMD ["python3", "main.py"]
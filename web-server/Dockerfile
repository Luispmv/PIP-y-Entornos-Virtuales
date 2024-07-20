FROM python:3.10

WORKDIR /Server
COPY requirements.txt /Server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Server/requirements.txt

COPY . /Server

CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","80"]
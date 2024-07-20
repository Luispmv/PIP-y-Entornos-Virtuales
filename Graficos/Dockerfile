FROM python:3.9

WORKDIR /Graficos
COPY requirements.txt /Graficos/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Graficos/requirements.txt

COPY . /Graficos

CMD bash -c "while true; do sleep 1; done"

FROM python:3

EXPOSE 3000

WORKDIR /var/server

COPY ./requirements.txt /var/server/
COPY ./*.py /var/server/
COPY ./core /var/server/core
COPY ./module /var/server/module

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
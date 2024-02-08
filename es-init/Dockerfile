FROM python:3.11.7
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./transfer_script.py /app/
COPY ./init_es.sh /app/
CMD ["/bin/bash", "-c", "/app/init_es.sh"]

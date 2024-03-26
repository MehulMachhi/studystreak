
# Use the official Python base image
FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get -y update
 
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install supervisor
COPY ./ /app/

COPY ./entrypoint.sh /
RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "sh", "/entrypoint.sh" ]
EXPOSE 8000
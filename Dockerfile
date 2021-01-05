#Platform
FROM python:3.8-alpine

#Install OS dependencies
RUN set -ex && apk add --no-cache gcc
RUN set -ex && apk add --no-cache musl-dev

#Install Python Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#Start API
COPY api.py /
CMD [ "python", "./api.py" ]
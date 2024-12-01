ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache --update \
  python3 py3-pip

COPY requirements.txt /requirements.txt
WORKDIR /


RUN python3 -m venv venv
RUN source ./venv/bin/activate && \
    pip install -r requirements.txt

COPY . /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
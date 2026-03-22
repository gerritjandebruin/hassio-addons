ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache py3-pip && \
    pip3 install --no-cache-dir fava==1.27.1

COPY run.sh /
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

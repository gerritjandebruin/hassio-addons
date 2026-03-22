ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache --virtual .build-deps build-base python3-dev && \
    pip3 install --no-cache-dir --break-system-packages uv && \
    uv pip install --system --no-cache fava==1.30.12 && \
    apk del .build-deps

COPY run.sh /
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

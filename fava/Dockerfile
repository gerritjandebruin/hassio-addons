ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache --virtual .build-deps build-base python3-dev bison flex && \
    wget -qO- https://astral.sh/uv/install.sh | sh && \
    uv pip install --system --no-cache fava==1.30.12 && \
    apk del .build-deps

COPY fava_ingress.py /
COPY run.sh /
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

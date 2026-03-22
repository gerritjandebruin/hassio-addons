ARG BUILD_FROM
FROM $BUILD_FROM

RUN pip3 install --no-cache-dir --break-system-packages uv && \
    uv pip install --system --no-cache fava==1.30.12

COPY run.sh /
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

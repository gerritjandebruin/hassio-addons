#!/usr/bin/with-contenv bashio

BEANCOUNT_FILE=$(bashio::config 'beancount_file')
INGRESS_PORT=$(bashio::addon.ingress_port)
INGRESS_ENTRY=$(bashio::addon.ingress_entry)

bashio::log.info "Starting Fava with file: ${BEANCOUNT_FILE}"

if [ ! -r "${BEANCOUNT_FILE}" ]; then
    bashio::log.fatal "Beancount file not found or not readable: ${BEANCOUNT_FILE}"
    exit 1
fi

exec fava --host 0.0.0.0 --port "${INGRESS_PORT}" --prefix "${INGRESS_ENTRY}" "${BEANCOUNT_FILE}"

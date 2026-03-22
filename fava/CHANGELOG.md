# Changelog

## 1.0.9

- Fix ingress not reachable by binding to `0.0.0.0` instead of `127.0.0.1`.
- Use `pathlib` in `fava_ingress.py`.
- Log message when Fava is started.

## 1.0.8

- Fix `uv` not found during Docker build by adding `/root/.local/bin` to `PATH`.

## 1.0.7

- Update base images from Python 3.12 / Alpine 3.18 to Python 3.13 / Alpine 3.21.
- Bind server to `127.0.0.1` instead of `0.0.0.0` for ingress-only access.
- Add `SIGTERM` signal handling for clean shutdown.
- Translate all documentation to English.

## 1.0.6

- Add beancount file directory to `sys.path` so local plugins can be found.

## 1.0.5

- Change share mapping from `ro` to `rw` so Fava can edit transactions.

## 1.0.4

- Fix white screen when opening Web UI via ingress.
- Add WSGI wrapper (`fava_ingress.py`) that correctly sets `SCRIPT_NAME` for Home Assistant ingress.

## 1.0.3

- Add build dependencies (`build-base`, `python3-dev`, `bison`, `flex`) for beancount 3.x compilation.
- Remove build dependencies after installation to reduce image size.
- Add share mapping (`share:ro`) so the add-on can read files from `/share`.
- Pass ingress prefix (`--prefix`) to Fava for correct URL generation.

## 1.0.2

- Update base images to Python 3.12 on Alpine 3.18.

## 1.0.1

- Update Fava from 1.27.1 to 1.30.12.
- Change base images from `base` to `base-python`.
- Switch package installation to `uv`.

## 1.0.0

- Initial release of the Fava add-on for Home Assistant.
- Support all architectures: aarch64, amd64, armhf, armv7, i386.
- Ingress support for direct access via the Home Assistant sidebar.
- Configurable path to the Beancount file.

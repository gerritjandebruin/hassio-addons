# Changelog

## 1.0.5

- Share-mapping gewijzigd van `ro` naar `rw` zodat Fava transacties kan bewerken.

## 1.0.4

- Wit scherm bij openen Web UI via ingress opgelost.
- WSGI-wrapper (`fava_ingress.py`) toegevoegd die `SCRIPT_NAME` correct instelt voor Home Assistant ingress.

## 1.0.3

- Build-dependencies (`build-base`, `python3-dev`, `bison`, `flex`) toegevoegd voor compilatie van beancount 3.x.
- Build-dependencies worden na installatie weer verwijderd om image-grootte te beperken.
- Share-mapping (`share:ro`) toegevoegd zodat de add-on bestanden uit `/share` kan lezen.
- Ingress-prefix (`--prefix`) doorgegeven aan Fava voor correcte URL-generatie.

## 1.0.2

- Base images gewijzigd naar Python 3.12 op Alpine 3.18.

## 1.0.1

- Fava geüpdatet van 1.27.1 naar 1.30.12.
- Base images gewijzigd van `base` naar `base-python`.
- Package-installatie overgeschakeld naar `uv`.

## 1.0.0

- Eerste versie van de Fava add-on voor Home Assistant.
- Ondersteunt alle architecturen: aarch64, amd64, armhf, armv7, i386.
- Ingress-ondersteuning voor directe toegang via de Home Assistant zijbalk.
- Configureerbaar pad naar het Beancount bestand.

# Fava - Home Assistant Add-on

Fava is een webinterface voor [Beancount](https://beancount.github.io/), een double-entry boekhoudprogramma op basis van platte tekstbestanden.

## Vereisten

Je hebt een geldig `.beancount` bestand nodig. Plaats dit bestand in de `/share` map van Home Assistant, zodat de add-on er toegang toe heeft.

Voorbeeld:
```
/share/beancount/finances.beancount
```

## Configuratie

| Optie | Type | Standaard | Beschrijving |
|---|---|---|---|
| `beancount_file` | `str` | `/share/beancount/finances.beancount` | Volledig pad naar het Beancount bestand |

### Voorbeeld configuratie

```yaml
beancount_file: /share/beancount/finances.beancount
```

## Gebruik

1. Stel het pad naar je `.beancount` bestand in via de add-on configuratie.
2. Start de add-on.
3. Open Fava via de zijbalk van Home Assistant (Ingress) of via `http://<ha-ip>:5000`.

## Beancount bestand aanmaken

Een minimaal `.beancount` bestand ziet er als volgt uit:

```beancount
option "title" "Mijn Financiën"
option "operating_currency" "EUR"

2024-01-01 open Assets:Bank:Betaalrekening  EUR
2024-01-01 open Expenses:Boodschappen       EUR
2024-01-01 open Income:Salaris              EUR
```

Zie de [Beancount documentatie](https://beancount.github.io/docs/) voor meer informatie.

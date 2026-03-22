# Fava - Home Assistant Add-on

Fava is a web interface for [Beancount](https://beancount.github.io/), a double-entry bookkeeping system based on plain text files.

## Requirements

You need a valid `.beancount` file. Place this file in the `/share` directory of Home Assistant so the add-on can access it.

Example:
```
/share/beancount/finances.beancount
```

## Configuration

| Option | Type | Default | Description |
|---|---|---|---|
| `beancount_file` | `str` | `/share/beancount/finances.beancount` | Full path to the Beancount file |

### Example configuration

```yaml
beancount_file: /share/beancount/finances.beancount
```

## Usage

1. Set the path to your `.beancount` file in the add-on configuration.
2. Start the add-on.
3. Open Fava via the Home Assistant sidebar (Ingress).

## Creating a Beancount file

A minimal `.beancount` file looks like this:

```beancount
option "title" "My Finances"
option "operating_currency" "EUR"

2024-01-01 open Assets:Bank:Checking  EUR
2024-01-01 open Expenses:Groceries    EUR
2024-01-01 open Income:Salary         EUR
```

See the [Beancount documentation](https://beancount.github.io/docs/) for more information.

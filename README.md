# Currency Converter (Python)

A small command-line tool that converts an amount from one currency to another — handy for quick estimates (e.g. USD → PKR).

## How to run

```bash
python currency_converter.py
```

Example:

```
Amount: 100
From currency (e.g. USD): USD
To currency (e.g. PKR): PKR
100.00 USD = 27800.00 PKR
```

Supported currencies: USD, PKR, EUR, GBP, AED, SAR, INR, AUD.

## Static demo rates

The exchange rates in this project are **static demo values** hard-coded in `currency_converter.py` — they are **NOT live market rates** and will drift from the real market over time. For real transactions, always check a live rate source (bank, exchange app, or a rates API).

## How it works

Every currency is converted via USD:

```
amount_in_usd = amount / rate[from_currency]
result = amount_in_usd * rate[to_currency]
```

## What was practiced

- Dictionaries as lookup tables
- Input validation and clear error messages
- Converting through a common base currency

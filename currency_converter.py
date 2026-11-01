#!/usr/bin/env python3
"""Currency Converter — convert between currencies using static rates.

Rates are STATIC demo rates (labelled in the README) — they are NOT live
market rates. For real transactions, always check a live rate source.

Usage:
    python currency_converter.py
"""

# Static demo rates: how many units of each currency equal 1 USD.
# Clearly labelled as demo data — update these values for real use.
RATES_TO_USD = {
    "USD": 1.0,
    "PKR": 278.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "AED": 3.67,
    "SAR": 3.75,
    "INR": 83.5,
    "AUD": 1.52,
}


def convert(amount: float, from_currency: str, to_currency: str) -> float:
    """Convert amount from one currency to another via USD."""
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in RATES_TO_USD:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_currency not in RATES_TO_USD:
        raise ValueError(f"Unsupported currency: {to_currency}")
    amount_in_usd = amount / RATES_TO_USD[from_currency]
    return amount_in_usd * RATES_TO_USD[to_currency]


def main() -> None:
    print("=== Currency Converter ===")
    print("Supported:", ", ".join(sorted(RATES_TO_USD)))
    print("NOTE: rates are static demo rates, not live market rates.\n")
    try:
        amount = float(input("Amount: "))
        from_cur = input("From currency (e.g. USD): ").strip()
        to_cur = input("To currency (e.g. PKR): ").strip()
        result = convert(amount, from_cur, to_cur)
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return
    print(f"\n{amount:.2f} {from_cur.upper()} = {result:.2f} {to_cur.upper()}")


if __name__ == "__main__":
    main()

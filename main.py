import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert_currency(from_currency, to_currency, amount):
    API_KEY = os.getenv("EXCHANGE_API_KEY")
    
    if not API_KEY:
        print("❌ API key not found. Please set it in your .env file.")
        return None

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or data.get("result") != "success":
        print("❌ Error fetching conversion rate.")
        return None
    
    return data["conversion_result"]

def main():
    print("💱 Currency Converter App 💱")
    from_currency = input("From Currency (e.g., USD): ").upper()
    to_currency = input("To Currency (e.g., EUR): ").upper()
    
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("❌ Please enter a valid number for amount.")
        return

    result = convert_currency(from_currency, to_currency, amount)

    if result is not None:
        print(f"\n✅ {amount} {from_currency} = {result:.2f} {to_currency}\n")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk, messagebox
import requests

# --- Configuration ---
API_KEY = "CDL7E5QQXNXD02ON" 
BASE_URL = r"https://www.alphavantage.co/query?"


# ---------------------


def validate_digit_input(new_value):
    if new_value == "":
        return True
    elif new_value.isdigit():
        return True
    else:
        return False
def get_exchange_rate(from_currency, to_currency):
    """Fetches the real-time exchange rate from Alpha Vantage API."""
    function = "CURRENCY_EXCHANGE_RATE"
    # Constructing the URL with parameters
    main_url = f"{BASE_URL}function={function}&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"
    print (main_url)

    try:
        # Making the API call using the requests library
        req_ob = requests.get(main_url)
        result = req_ob.json()
        print(f"API Status Code: {req_ob.status_code}")
        print(f"API Response Text: {req_ob.text}")

        # Parsing the JSON response
        if "Realtime Currency Exchange Rate" in result:
            exchange_rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
            return exchange_rate
        elif "Error Message" in result:
            messagebox.showerror("API Error", result["Error Message"])
            return None
        else:
            messagebox.showerror("API Error", "Could not retrieve exchange rate. Check currencies or API key.")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Could not connect to API: {e}")
        return None


def convert_currency():
    """Performs the currency conversion and updates the GUI."""
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = "RUB"  # Fixed target currency

        if from_currency == to_currency:
            converted_amount_label.config(text=f"Конвертирован в: {amount:.2f} Рулбей")
            return

        rate = get_exchange_rate(from_currency, to_currency)

        if rate is not None:
            new_amount = round(amount * rate, 2)
            converted_amount_label.config(text=f"Конвертирован в: {new_amount:.2f} Рублей")
    except ValueError:
        return


# --- Окно-заполнитель ---
root = tk.Tk()
root.title("Конвертор нескольких валют")
root.geometry("400x250")
root.resizable(False, False)
validate_digit_command =root.register(validate_digit_input)

# Процесс ввода валюты
tk.Label(root, text="Количество:").pack()
amount_entry = tk.Entry(root, width=20, validate="key", validatecommand=(validate_digit_command, '%P'))
amount_entry.pack()

# From Currency Selection
tk.Label(root, text="Выберете валюту:").pack()
# Лист перечисленных валют
currencies = ["USD", "EUR", "GBP", "JPY", "CNY", "AUD"]
from_currency_var = tk.StringVar(root)
from_currency_var.set("EUR")  # Настраивает валюту на старте

from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=currencies, state="readonly")
from_currency_menu.pack(pady=5)

# Кнопка которая конвертирует
convert_button = tk.Button(root, text="Convert to RUB", command=convert_currency)
convert_button.pack(pady=20)

# Вывод конвертора
converted_amount_label = tk.Label(root, text="Converted Amount: ", font=("Helvetica", 12, "bold"))
converted_amount_label.pack(pady=10)

if __name__ == "__main__":
    if API_KEY == "YOUR_API_KEY":
        messagebox.showwarning("API Key Required",
                               "Please replace 'YOUR_API_KEY' with your actual Alpha Vantage key in the script.")
    root.mainloop()
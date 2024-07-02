# Crypto Currency Price Tracker with Selenium and smtplib

This Python script allows you to track the prices of various cryptocurrencies by using Selenium for web scraping and smtplib for sending email alerts. It fetches the latest prices from a selected website and sends an email notification whenever the price of a specified cryptocurrency falls below or rises above a certain threshold.

## Requirements

To run the script, you need the following dependencies:

- Python 3.x
- Selenium library
- Chrome App Password (available after 2 step verification)
- smtplib library (comes with Python)

## Installation

1. **Python**: If you don't have Python installed, download and install the latest version from the official website: https://www.python.org/downloads/

2. **Selenium**: You can install Selenium using pip with the following command:
   ```
    pip install selenium
   ```
## Usage

1. Open the `cryptotracker.py` file in a text editor.

2. Set up your email configurations:
- Replace `'sender@gmail.com'` with your Gmail address (the address from which you want to send alerts).
- Replace `'app password'` with the app password generated from chrome after 2 step verification.
- Replace `'receiver@gmail.com'` with the recipient's email address (where you want to receive the alerts).

3. Define the cryptocurrency you want to track and the price threshold for alerts:
- Replace `'Bitcoin'` with the name of your desired cryptocurrency.
- Set `'threshold_low'` with the desired price thresholds.
4. Change the tracking period which is default set as 3 seconds to desireable period.

5. Save the changes to the file.

6. Run the script using the following command:
   ```
     Python PriceTracker.py
   ```


## Important Note

- This script uses Gmail's SMTP server to send email alerts. Make sure to enable "Allow less secure apps" in your Gmail account settings for the script to work. Alternatively, you can use an app password for authentication if you have two-factor authentication enabled for your Gmail account.

- Be cautious when providing your email credentials in the script. It's recommended to use a dedicated email account for this purpose.

## Disclaimer

This script is intended for educational purposes and personal use only. Use it responsibly and at your own risk. The prices fetched from websites might not always be accurate or up-to-date. Always double-check the information from reliable sources before making any financial decisions.

Happy crypto tracking! 🚀

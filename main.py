# -------------------------------------------------Amazon Price Alert---------------------------------------------------

import requests
from bs4 import BeautifulSoup
import smtplib

# ----------------------------------Set Price Alert---------------------------------------------------------------------
set_target = 0

# -----------------sender's Email-----------------------------------Provide receiver's email----------------------------
HOST_MAIL = "from email here"
SEND_TO = "to email here"
# --------------------------------sender's password --------------------------------------------------------------------
password = "from email password"


# -------------->>>>>Copy Product Url and Paste here inside "" to Keep it as a String.<<<<------------------------------
AMAZON_PRODUCT_URL = "Product url here"


# ------>>for mozilla users, User-Agent is : 'Mozilla' & mac : '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'<<--------
HEADER = {
    "User-Agent": "537.36 (KHTML, like Gecko) Chrome",
    "Accept-Language": "en-IN"
}

response = requests.get(AMAZON_PRODUCT_URL, headers=HEADER)
Html_page_source = response.text

soup = BeautifulSoup(Html_page_source, "html.parser")
price = float(soup.find("span", class_="a-size-medium a-color-price priceBlockDealPriceString").
              get_text().replace("₹", "").replace(",", ""))
product = soup.find("span", class_="a-size-large product-title-word-break").get_text().rstrip().lstrip()

# Target Alert check
if price <= float(set_target):
    smtp = smtplib.SMTP("smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(user=HOST_MAIL, password=password)
    smtp.sendmail(from_addr=HOST_MAIL,
                  to_addrs=SEND_TO,
                  msg=f"Subject: Low Price Alert"
                      f"\n\nProduct Title:{product}"
                      f"\n\nPrice Drop at @ Rs.{price}"
                      f"\n\nlink:{AMAZON_PRODUCT_URL}")

    smtp.close()

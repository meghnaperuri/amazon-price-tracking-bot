# import smtplib
# import requests
# from bs4 import BeautifulSoup
# import lxml
#
# headers={
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
# }
#
# response= requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# text=response.text
#
# soup=BeautifulSoup(text, "html.parser")
# array=soup.select(selector="span.a-price > span.a-offscreen")
# priceArray=[]
# for x in array:
#     price=float(x.getText().split("$")[1])
#     priceArray.append(price)
#
# print(priceArray[1])


import smtplib
import requests
from bs4 import BeautifulSoup
import lxml
my_email="meghnaperuri222@gmail.com"
password="awjqsxdrmduedxus"

headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language":"Accept-Language:en-US,en;q=0.9"
}
url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response= requests.get(url, headers=headers)
text=response.content
# print(text)

soup=BeautifulSoup(text, "lxml")
# print(soup.prettify())
array=soup.find_all("span", class_="a-price-whole")
priceArray=[pe.get_text() for pe in array]
price=int(priceArray[0].split(".")[0])

if price<100:
    print("price is less than 100.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mperuri@gmu.edu",
            msg=f"subject: whoohoo! check out this new price\n\nThe price is {price}!!\n{url} \n Go head and purchase it!"
        )






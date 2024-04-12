from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/search/businesses/@27.4810697,77.687969,15z?entry=ttu')
html_text = driver.page_source
driver.quit()
soup = BeautifulSoup(html_text, 'html.parser')
businesses = soup.find_all('div', class_='lI9IFe')

for business in businesses:
    name = business.find("div", class_="qBF1Pd").text.strip()

    rating_element = business.find("span", class_="MW4etd")
    rating = rating_element.text.strip() if rating_element else "No rating available"

    business_type_element = business.find("span", class_="W4Efsd")
    business_type = business_type_element.text.strip() if business_type_element else "Business type not available"

    address_element = business.find("span", class_="W4Efsd")
    address = address_element.find_next("span").text.strip() if address_element else "Address not available"

    opening_hours_element = business.find("span", class_="W4Efsd")
    opening_hours = opening_hours_element.find_next("span").text.strip() if opening_hours_element else "Opening hours not available"

    phone_number_element = business.find("span", class_="UsdlK")
    phone_number = phone_number_element.text.strip() if phone_number_element else "Phone number not available"

    print("Business Name:", name)
    print("Rating:", rating)
    print("Type:", business_type)
    print("Address:", address)
    print("Opening Hours:", opening_hours)
    print("Phone Number:", phone_number)
    print('-')

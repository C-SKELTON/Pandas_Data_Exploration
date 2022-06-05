import requests
from bs4 import BeautifulSoup
import pandas as pd

url_ = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
results = url_.text
soup = BeautifulSoup(results, "html.parser")

new_data = []

for x in range(24):
    for row in soup.select('.data-table__row'):
        new_row = [cell.getText() for cell in row.select(".data-table__value")]
        new_data.append(new_row)

df = pd.DataFrame(new_data, columns=['Rank', 'Major', 'Degree', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning'])
clean_df = df.drop_duplicates(subset=['Major'])
print(clean_df[['Major', 'Mid-Career Pay']])


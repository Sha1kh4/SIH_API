from datetime import date
import requests
from bs4 import BeautifulSoup
import warnings
import json

# Suppress the InsecureRequestWarning
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def fetch_table_data():
    url = "https://sih.gov.in/sih2024PS"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    
    headers = {"user-agent": USER_AGENT}
    
    # Disable SSL certificate verification
    response = requests.get(url, verify=False, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully fetched the HTML content.")
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the table with the specific class and ID
        table = soup.find("table", {"class": "table table-striped table-bordered", "id": "dataTablePS"})
        
        if table:
            # Remove 'div' with class 'modal-body' from all 'td' elements
            for td in table.find_all('td'):
                modal_body_div = td.find('div', class_='modal-body')
                if modal_body_div:
                    modal_body_div.decompose()  # Remove the div from the tree
            
            # Extract headers
            headers = [header.text.strip() for header in table.find_all('th')]
            
            # Extract rows
            rows = []
            for row in table.find_all('tr'):
                cells = row.find_all('td')
                if cells:
                    cell_data = [cell.text.strip() for cell in cells]
                    rows.append(cell_data)
            
            # Convert to dictionary format
            table_dict = [dict(zip(headers, row)) for row in rows]

            
            return table_dict
        else:
            return ("Table not found.")
    else:
        return (f"Failed to retrieve the page. Status code: {response.status_code}")
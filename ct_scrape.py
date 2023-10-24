import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import os
import sys

def scrape_outcome_measures(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return None

    # Parse the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_outcomes(soup, nct_number, project_name):
    outcomes = []

    # Extract Primary Outcomes
    primary_outcomes = soup.find('span', {'data-term': 'Primary Outcome Measure'}).find_next('ol').find_all('li')
    for outcome in primary_outcomes:
        description = outcome.contents[0]  # Get the first direct content (excluding children) of the <li>
        outcomes.append(("Primary", description.strip()))

    # Extract Secondary Outcomes
    secondary_outcomes = soup.find('span', {'data-term': 'Secondary Outcome Measure'}).find_next('ol').find_all('li')
    for outcome in secondary_outcomes:
        description = outcome.contents[0]  # Get the first direct content (excluding children) of the <li>
        outcomes.append(("Secondary", description.strip()))

    # Total outcomes
    total_outcomes = len(primary_outcomes) + len(secondary_outcomes)

    # Write to CSV inside the project directory
    with open(os.path.join(project_name, f"{nct_number}.csv"), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Outcome Type", "Description", "Total Outcomes"])
        for outcome in outcomes:
            writer.writerow([outcome[0], outcome[1], total_outcomes])

def extract_intervention_treatment(soup):
    intervention_treatments = []
    table = soup.find('table', {'class': 'ct-data_table tr-data_table'})
    
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) >= 2:
                cell_content = cols[1]
                # Find all text within spans or isolated by <br> tags
                treatments = [span.get_text(strip=True) for span in cell_content.find_all('span')]
                if not treatments:
                    treatments = cell_content.get_text(strip=True).split('\n')
                intervention_treatments.extend(treatments)
    
    return intervention_treatments

if __name__ == "__main__":
    # Prompt the user for the project name
    project_name = input("Enter the name of the project: ")

    # Create a directory with that project name if it doesn't exist
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    # Input can be a combination of comma and/or space-separated NCT numbers
    nct_numbers_input = input("Enter the list of NCT numbers (comma and/or space-separated): ")
    
    # Split the input based on comma and/or spaces
    nct_numbers = [nct.strip() for nct in nct_numbers_input.replace(",", " ").split() if nct]

    base_url = "https://classic.clinicaltrials.gov/ct2/show/"

    for nct_number in nct_numbers:
        url = base_url + nct_number
        soup = scrape_outcome_measures(url)
        if soup:
            intervention_treatments = extract_intervention_treatment(soup)
            
            for intervention_treatment in intervention_treatments:
                # Create a folder based on intervention/treatment name
                folder_name = os.path.join(project_name, intervention_treatment)
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                
                # Save CSV file within the folder
                extract_outcomes(soup, nct_number, folder_name)

        # Random pause between 1 to 2 seconds
        time.sleep(random.uniform(1, 2))

    sys.exit("Finished processing all NCT numbers.")

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

    # Look for the 'Primary Outcome Measure' span element
    primary_outcome_span = soup.find('span', {'data-term': 'Primary Outcome Measure'})

    # Proceed only if the span element was found
    if primary_outcome_span is not None:
        primary_outcomes = primary_outcome_span.find_next('ol').find_all('li')
        for outcome in primary_outcomes:
            description = outcome.contents[0]  # Get the first direct content (excluding children) of the <li>
            outcomes.append(("Primary", description.strip()))
    else:
        print(f"No primary outcomes found for NCT number {nct_number}")

    # Look for the 'Secondary Outcome Measure' span element
    secondary_outcome_span = soup.find('span', {'data-term': 'Secondary Outcome Measure'})
    
    # Proceed only if the span element was found
    if secondary_outcome_span is not None:
        secondary_outcomes = secondary_outcome_span.find_next('ol').find_all('li')
        for outcome in secondary_outcomes:
            description = outcome.contents[0]  # Get the first direct content (excluding children) of the <li>
            outcomes.append(("Secondary", description.strip()))
    else:
        print(f"No secondary outcomes found for NCT number {nct_number}")

    # Total outcomes
    total_outcomes = 0
    if primary_outcome_span is not None:
        total_outcomes += len(primary_outcomes)
    if secondary_outcome_span is not None:
        total_outcomes += len(secondary_outcomes)

    # Write to CSV inside the project directory
    with open(os.path.join(project_name, f"{nct_number}.csv"), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["OM Index", "Unique Code", "OM Type", "OM Description", "Total Outcomes", "Trial Code"])
        for index, outcome in enumerate(outcomes, 1):
            om_type = outcome[0]
            unique_code = f"{nct_number}_{'P' if om_type == 'primary' else 'S'}{index}"
            writer.writerow([index, unique_code, om_type, outcome[1], total_outcomes, nct_number])

def extract_intervention_treatment(soup):
    intervention_treatments = []
    table = soup.find('table', {'class': 'ct-data_table tr-data_table'})
    
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) >= 2:
                cell_content = cols[1]
                treatments = [span.get_text(strip=True) for span in cell_content.find_all('span')]
                if not treatments:
                    treatments = cell_content.get_text(strip=True).split('\n')
                intervention_treatments.extend(treatments)
    
    return intervention_treatments

if __name__ == "__main__":
    
    project_name = input("Enter the name of the project: ")

    if not os.path.exists(project_name):
        os.makedirs(project_name)

    input_method = input("Would you like to input NCT numbers directly or from a txt file? (Enter 'direct' or 'file'): ")

    nct_numbers = []
    if input_method == 'file':
        file_name = input("Please enter the name of the txt file containing NCT numbers: ")
        with open(file_name, 'r') as file:
            content = file.read()
            nct_numbers = [nct.strip() for nct in content.replace(",", " ").split() if nct.strip()]
    else:
        nct_numbers_input = input("Enter the list of NCT numbers (comma and/or space-separated): ")
        nct_numbers = [nct.strip() for nct in nct_numbers_input.replace(",", " ").split() if nct]
    base_url = "https://classic.clinicaltrials.gov/ct2/show/"

    for nct_number in nct_numbers:
        url = base_url + nct_number
        soup = scrape_outcome_measures(url)
        if soup:
            intervention_treatments = extract_intervention_treatment(soup)
            
            for intervention_treatment in intervention_treatments:
                folder_name = os.path.join(project_name, intervention_treatment)
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                extract_outcomes(soup, nct_number, folder_name)

        time.sleep(random.uniform(1, 2))

    sys.exit("Finished processing all NCT numbers.")

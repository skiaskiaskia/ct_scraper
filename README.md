
# CT Scraper: Advanced Clinical Trials Data Extraction 🌐💉

An advanced Python script designed to scrape clinical trials data from various online platforms. The tool aims to collect and organize outcome measures and intervention treatments based on trial identification numbers (NCT numbers).

## Features 🌟

- Retrieves **Primary and Secondary Outcome Measures** for specific NCT numbers.
- Extracts **Intervention Treatments** associated with the trials.
- Generates more detailed CSV files for each trial number, including unique codes for primary and secondary outcomes.
- Organizes data under separate folders based on **Intervention/Treatment** names.
- Option to import NCT numbers from a text file for batch processing.

## Requirements 📦

1. Python 3.x
2. Libraries:
    - `requests`
    - `BeautifulSoup4`
    - `csv`
    - `time`
    - `random`
    - `os`
    - `sys`

## Quick Start 🚀

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/skiaskiaskia/ct_scraper.git
    ```

2. **Navigate to the directory**:
    ```bash
    cd ct_scraper
    ```

3. **Install required libraries** (preferably in a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the script**:
    ```bash
    python3 ct_scraper.py
    ```

2. **Provide Inputs**:
    - Enter a project name to act as the root directory for storing the scraped data.
    - Choose the input method for NCT numbers (either manually or from a text file).

3. **Automated Scraping**:
    - The script will go through each NCT number, create necessary directories, and save the detailed CSV files for each trial.

4. Sit back and relax ☕️! There's a random delay of 1-2 seconds between each request to minimize the risk of being detected/blocked.

## Notes 📝

- Make sure the target platform is accessible from your location.
- Be aware that the website's structure might change, affecting the scraper's performance.
- Always abide by the platform's terms of use and `robots.txt`.

## Contributions 💡

Contributions are welcome! Feel free to fork, raise issues, or submit pull requests.

## Disclaimer ⚠️

This tool is intended for educational purposes only. Ensure you have the rights to scrape the website before proceeding. The author is not responsible for any misuse or damages resulting from the use of this tool.

---

Happy scraping! 🕷️🌐

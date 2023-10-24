# ct_scraper
# Clinical Trials Scraper 🌐💉

This Python script scrapes the classic Clinical Trials website to retrieve and save outcome measures based on the given list of NCT numbers.

## Features 🌟
- Retrieves **Primary and Secondary Outcome Measures** for specific NCT numbers.
- Extracts **Intervention Treatments** associated with the trials.
- Generates CSV files for each NCT number detailing the outcomes.
- Organizes outcomes under separate folders based on the **Intervention/Treatment** name.
- In theory, you can change this and play with it as you like. This is just what I wanted / liked.

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

## How to use? 🚀

1. **Clone the repository**:
    ```bash
    git clone <repository_link>
    ```

2. **Navigate to the directory**:
    ```bash
    cd <repository_directory>
    ```

3. **Install required libraries** (preferably in a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script**:
    ```bash
    python <script_name>.py
    ```

5. **Provide inputs**:
    - First, enter a project name. This will be used as the root directory where all data will be saved.
    - Next, provide a list of NCT numbers you want to scrape. The NCT numbers can be comma and/or space-separated.

6. Sit back and relax ☕️! The script will process each NCT number, create necessary directories, and save CSV files for the outcomes. There's a random delay of 1-2 seconds between processing each NCT number to mimic human behavior and reduce the chance of being detected/blocked.

## Notes 📝
- The script uses the `classic.clinicaltrials.gov` URL. Ensure it's accessible from your location.
- Be aware of potential changes to the website's structure, which might affect the scraper's performance.
- Always respect the website's `robots.txt` and terms of use.

## Contribution 💡

Feel free to fork, improve, raise issues, or submit pull requests. Contributions are always welcome! 💖

## Disclaimer ⚠️

This tool is meant for educational purposes only. Ensure you have the rights to scrape a website before proceeding. The author is not responsible for any misuse or any damages that may arise from using this tool.

---

Happy scraping! 🕷️🌐

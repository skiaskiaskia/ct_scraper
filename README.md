

# Generic Clinical Trials Scraper 🌐💉

This Python script is designed to scrape clinical trials data from various online sources to retrieve and save outcome measures based on given trial identification numbers.

## Features 🌟
- Retrieves **Primary and Secondary Outcome Measures** for specific trial identification numbers.
- Extracts **Intervention Treatments** associated with the trials.
- Generates CSV files for each trial number detailing the outcomes.
- Organizes outcomes under separate folders based on the **Intervention/Treatment** name.
- You can edit / add to it to suit your needs.

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

4. **Run the script**:
    ```bash
    python ct_scraper.py
    ```

5. **Provide inputs**:
    - First, enter a project name. This will be used as the root directory where all data will be saved.
    - Next, provide a list of trial identification numbers you want to scrape. These numbers can be comma and/or space-separated.

6. Sit back and relax ☕️! The script will process each trial number, create necessary directories, and save CSV files for the outcomes. There's a random delay of 1-2 seconds between processing each number to mimic human behavior and reduce the risk of being detected/blocked.

## Notes 📝
- Ensure the target website or source is accessible from your location.
- Be aware of potential changes to the website's structure, which might affect the scraper's performance.
- Always respect the website's `robots.txt` and terms of use.

## Contribution 💡

Feel free to fork, improve, raise issues, or submit pull requests. Contributions are always welcome! 💖

## Disclaimer ⚠️

This tool is meant for educational purposes only. Ensure you have the rights to scrape a website before proceeding. The author is not responsible for any misuse or damages that may arise from using this tool.

---

Happy scraping! 🕷️🌐

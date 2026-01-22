# Internship-Project
A Python-based web scraping and data processing project for collecting and analyzing product information from Dafiti and Falabella e-commerce websites. The project includes:
- Automated scraping scripts
- Data cleaning scripts
- A dashboard for visualizing and exploring the collected data

Developed as part of a summer internship.

## Project Structure
- `abc_*.py` – Web scraping scripts for Dafiti and Falabella
- `June/Week_*` – Data cleaning scripts organized by week
- `dashboard/` – Dashboard code for data visualization
- `dafiti_products.csv`, `falabella_products.csv` – Collected product data

## Setup
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install selenium scrapy pandas
   ```
   (Add other packages if your dashboard requires them, e.g., streamlit, dash, matplotlib, etc.)
3. Make sure you have the appropriate WebDriver for Selenium (e.g., ChromeDriver).

## Usage
- Run the scraping scripts to collect product data:
  ```bash
  python abc_3.py
  python abc_4.py
  ```
- Run cleaning scripts in the `June/Week_*` folders as needed.
- Launch the dashboard (see dashboard/README or script for instructions).

## Notes
- Some CSV files may be large; consider adding them to `.gitignore` if not needed in the repo.
- Update the dashboard section with specific launch instructions if required.

## License
This project was developed for educational purposes during a summer internship.

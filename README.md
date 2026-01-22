# Internship-Project

A Python-based web scraping and data processing project for collecting and analyzing product information from **Dafiti** (Colombia) and **Falabella** (Chile) e-commerce websites.

## 🎯 Project Overview

This project automates the extraction of product data (watches, electronics, and other items) from two major Latin American e-commerce platforms:
- **Dafiti Colombia** - Watch products
- **Falabella Chile** - Electronics and household items

The scraped data is processed and stored in CSV format for analysis.

## 📁 Project Structure

```
Internship-Project/
├── src/                          # Source code directory
│   ├── dafiti_demo.py           # Demo scraper for single Dafiti product
│   ├── dafiti_scraper.py        # Dafiti scraper using requests
│   ├── dafiti_scraper2.py       # Dafiti scraper using Selenium (batch processing)
│   ├── falabella_scraper.py     # Falabella scraper using Selenium
│   └── main/                     # Additional modules (if any)
├── dashboard/                    # Dashboard for data visualization (in development)
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Features

✅ **Automated Web Scraping** - Extracts product details from dynamic JavaScript-rendered pages  
✅ **Headless Browser Support** - Uses Selenium with Chrome in headless mode  
✅ **Data Extraction** - Captures:
  - Product brand/title
  - Model numbers/product codes
  - Prices (current and original)
  - Product colors
  - Product URLs

✅ **CSV Export** - Saves scraped data in structured CSV format  
✅ **Error Handling** - Gracefully handles scraping errors  

## 🛠️ Setup

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (automatically managed with webdriver-manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RahulDubey1807/Internship-Project.git
   cd Internship-Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python -c "import selenium, scrapy, pandas; print('All packages installed successfully!')"
   ```

## 📖 Usage

### Running the Scrapers

#### 1. Dafiti Demo (Single Product)
```bash
python src/dafiti_demo.py
```
Scrapes a single product from Dafiti and displays the results in the console.

#### 2. Dafiti Batch Scraper
```bash
python src/dafiti_scraper2.py
```
Scrapes multiple watch products from Dafiti and saves to `dafiti_products.csv`

#### 3. Falabella Scraper
```bash
python src/falabella_scraper.py
```
Scrapes electronics products from Falabella and saves to `falabella_products2.csv`

### Output Files

After running the scrapers, you'll find CSV files in the project root:
- `dafiti_products.csv` - Dafiti watch data
- `falabella_products2.csv` - Falabella electronics data

## 📊 Data Schema

### Dafiti Products
| Column | Description |
|--------|-------------|
| URL | Product page URL |
| Brand | Product brand name |
| Model Number | Product model/SKU |
| Color | Product color |
| Current Price | Discounted/current price |
| Original Price | Original/MRP price |

### Falabella Products
| Column | Description |
|--------|-------------|
| URL | Product page URL |
| Brand/Title | Product title |
| Product Code | Internal product code |
| Current Price | Current selling price |
| Original Price | Original/list price |

## 🔧 Technical Details

### Technologies Used
- **Selenium** - Browser automation for JavaScript-rendered content
- **Scrapy Selector** - XPath-based HTML parsing
- **Pandas** - Data manipulation and CSV export
- **Requests** - HTTP requests (for simple scraping)

### Scraping Approach
1. **Headless Chrome** - Runs browser in background without GUI
2. **XPath Selectors** - Precisely targets HTML elements
3. **Wait Strategy** - Uses time delays to ensure page loads
4. **Error Handling** - Try-except blocks for resilient scraping

## ⚠️ Important Notes

- **Legal Compliance**: This project is for educational purposes. Always respect website terms of service and robots.txt
- **Rate Limiting**: Add delays between requests to avoid overwhelming servers
- **Data Privacy**: Do not scrape personal or sensitive information
- **CSV Files**: Large CSV files are ignored by git (see `.gitignore`)

## 🚧 Future Enhancements

- [ ] Complete dashboard implementation
- [ ] Add data cleaning and preprocessing scripts
- [ ] Implement retry logic for failed requests
- [ ] Add logging for better debugging
- [ ] Create scheduled scraping jobs
- [ ] Add data visualization and analytics

## 📝 License

This project was developed for educational purposes during a summer internship. Feel free to use and modify for learning purposes.

## 👨‍💻 Author

**Rahul Dubey**  
Developed as part of Summer Internship Project

---

**Note**: Make sure to update product URLs in the scraper files if target pages change or become unavailable.
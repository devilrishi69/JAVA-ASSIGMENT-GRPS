# DataForge

DataForge is a Python-based data scraping and processing prototype designed to demonstrate how publicly available data can be collected, cleaned, analyzed, exported, and prepared for potential monetization.

The project runs completely through a terminal interface and is designed as a simple college project.

---

## Features

- Scrape structured data from HTML pages
- Local demo dataset for reliable testing
- Extract product name, price, category, and rating
- Data cleaning and duplicate detection
- Basic data quality calculation
- Dataset analytics
- Category analysis
- Price statistics
- Rating statistics
- Export cleaned data to CSV
- Dataset valuation and simulated monetization
- Terminal-based system status
- Green-on-black terminal interface

---

## Project Workflow

```text
        DATA SOURCE
             |
             v
        HTML SCRAPER
             |
             v
        RAW DATASET
             |
             v
       DATA CLEANING
             |
             v
       DATA ANALYTICS
             |
             v
        CSV EXPORT
             |
             v
      DATA MONETIZATION
```

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- HTML
- CSV
- Terminal / Command Line

### Python Libraries

```text
requests
beautifulsoup4
```

---

## Project Structure

```text
DataForge/
│
├── main.py
├── scraper.py
├── demo_data.html
├── dataforge_dataset.csv
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| `main.py` | Main terminal application |
| `scraper.py` | HTML scraping and data extraction logic |
| `demo_data.html` | Local demo data source |
| `dataforge_dataset.csv` | Generated dataset after export |
| `README.md` | Project documentation |

---

## Installation

Make sure Python is installed on your system.

Check Python:

```bash
python --version
```

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

---

## Running the Project

Open the project folder in a terminal and run:

```bash
python main.py
```

The DataForge terminal will start.

---

## Main Menu

```text
[1] Start Scraper
[2] View Dataset
[3] Clean Dataset
[4] Dataset Analytics
[5] Export Dataset
[6] Monetize Dataset
[7] Earnings
[8] System Status
[0] Exit
```

---

## 1. Start Scraper

The scraper provides two options:

```text
[1] Local Demo Dataset
[2] Public Web URL
```

### Local Demo Dataset

The local HTML file is used as a controlled data source.

This makes the project reliable during demonstrations because it does not depend on an external website.

### Public Web URL

A permitted public webpage can also be provided.

The scraper uses:

```text
Requests
    ↓
HTML Response
    ↓
BeautifulSoup
    ↓
Structured Records
```

The current scraper extracts:

- Product name
- Price
- Category
- Rating

---

## 2. View Dataset

Displays the collected dataset in the terminal.

Example:

```text
ID   PRODUCT                  PRICE       CATEGORY
1    Wireless Mouse           Rs. 899     Computer Accessories
2    Mechanical Keyboard      Rs. 2499    Computer Accessories
3    USB Hub                  Rs. 1299    Computer Accessories
```

---

## 3. Clean Dataset

The cleaning module processes the raw dataset before export or monetization.

It checks for:

- Missing product names
- Duplicate products
- Invalid records

Example:

```text
Original records   : 20
Clean records      : 18
Duplicates removed : 1
Invalid removed    : 1
Data quality       : 90.0%
```

The cleaned dataset is then used for further processing.

---

## 4. Dataset Analytics

The analytics module provides basic statistics about the dataset.

It calculates:

- Total number of records
- Highest price
- Lowest price
- Average price
- Average rating
- Number of products in each category
- Dataset quality

---

## 5. Export Dataset

The processed dataset can be exported as:

```text
dataforge_dataset.csv
```

The CSV contains:

```text
id
name
price
category
rating
```

The exported file can be opened using Excel, Google Sheets, or other data analysis tools.

---

## 6. Monetize Dataset

DataForge demonstrates a simple dataset valuation model.

For the prototype:

```text
Price per record = Rs. 50
```

For example:

```text
18 records × Rs. 50
= Rs. 900
```

The monetization system includes:

- Dataset listing
- Dataset valuation
- CSV export
- Simulated transaction

### Important

The revenue and dataset prices shown by DataForge are **illustrative values for the college prototype** and do not represent actual sales or guaranteed market prices.

---

## 7. Earnings

The earnings section provides a basic demonstration of how revenue could be tracked.

Currently, the displayed revenue is simulated and intended only for demonstration purposes.

---

## 8. System Status

Displays the status of the major DataForge modules.

Example:

```text
Scraper Engine   : ONLINE
HTML Parser      : ONLINE
Cleaning Engine  : ONLINE
Analytics Engine : ONLINE
Dataset Storage  : ONLINE
CSV Export       : ONLINE
Monetization     : ONLINE
```

---

## Data Source and Responsible Use

DataForge is intended for educational purposes.

When using the web scraper:

- Only scrape publicly accessible and permitted data.
- Respect the website's terms of service and applicable laws.
- Do not bypass CAPTCHA or authentication.
- Do not attempt to access private or restricted information.
- Do not collect sensitive personal information.
- Respect robots.txt and reasonable request limits.

The included `demo_data.html` file provides a controlled dataset for demonstrations.

---

## Limitations

This is a prototype and does not currently include:

- Database storage
- User authentication
- Real payment processing
- Real dataset marketplace integration
- Advanced machine learning
- Distributed scraping
- Automatic website discovery
- Large-scale crawling

The monetization system is a simulation rather than a real marketplace.

---

## Future Improvements

Possible future improvements include:

- Database integration
- Scheduled scraping
- More advanced data validation
- Automatic data categorization
- REST API
- Web dashboard
- User authentication
- Dataset marketplace
- Real-time data sources
- Data visualization
- Machine learning based data quality detection

---

## Purpose

DataForge demonstrates a complete basic data pipeline:

```text
Collect
  ↓
Clean
  ↓
Analyze
  ↓
Export
  ↓
Value
```

The main goal is to demonstrate how raw web data can be transformed into a structured and potentially useful dataset.

---

## Author

**Rishi Raj Singh**

DataForge — College Project

---

## License

This project is intended for educational and demonstration purposes.

# Web Scraping Example

This folder contains a web scraping example that extracts hockey team statistics from a website and saves the results to a CSV file.

## Contents

- `WebScraping.ipynb` — Jupyter notebook that demonstrates the web scraping workflow using `requests`, `BeautifulSoup`, and `pandas`.
- `Hockey.csv` — exported dataset containing the scraped hockey team statistics.

## Notebook Summary

The notebook covers:

- Loading a web page using `requests`
- Parsing HTML content with `BeautifulSoup`
- Locating and extracting a table of hockey statistics
- Building a `pandas` DataFrame from extracted table rows
- Inspecting the resulting data and checking its structure
- Saving the cleaned DataFrame to `Hockey.csv`

## CSV Summary

The generated `Hockey.csv` file contains hockey team performance metrics, including:

- Team Name
- Year
- Wins
- Losses
- OT Losses
- Win %
- Goals For (GF)
- Goals Against (GA)
- + / -

## How to Use

1. Open `WebScraping.ipynb` in Jupyter Notebook or JupyterLab.
2. Run the notebook cells sequentially to execute the scraping workflow.
3. Review the extracted DataFrame and confirm the table contents.
4. Save the dataset to `Hockey.csv` and open it for further analysis.

## Requirements

The notebook uses the following Python libraries:

- requests
- beautifulsoup4
- pandas

Install dependencies with:

```bash
pip install requests beautifulsoup4 pandas
```

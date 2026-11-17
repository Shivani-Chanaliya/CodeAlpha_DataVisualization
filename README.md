# CodeAlpha Data Visualization

This project turns the quotes snapshot into a two-chart dashboard. The author bar chart shows counts in the sample; the histogram shows the distribution of quote character lengths. Neither chart implies author popularity or represents all quotations.

## Run

From this folder:

```powershell
python -m pip install pandas matplotlib seaborn
python visualize_data.py
```

The script saves `data_visualization_dashboard.png` beside the input CSV. It validates the required columns and excludes incomplete or duplicate quote-author records before plotting. The histogram avoids a smoothed density curve because the sample is small and the measurements are discrete.

The notebook can also be run from this folder. In a notebook, the project paths are based on the kernel's current working directory because `__file__` is not defined there.

## Files

- `visualize_data.py` — data preparation and dashboard generation
- `scraped_quotes.csv` — input sample
- `data_visualization_dashboard.png` — generated dashboard

To keep the projects reproducible, refresh the sample from the Web Scraping task before comparing chart output across runs.

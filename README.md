# food-delivery-data-analysis
This project analyzes food delivery data by merging and processing datasets from orders, users, and restaurants.

## Project Structure

- `data/`: Contains raw data files
  - `orders.csv`: Order details
  - `users.json`: User information
  - `restaurants.sql`: Restaurant data
- `scripts/`: Python scripts for data processing
  - `data_merger.py`: Script to merge and analyze data
- `output/`: Processed data outputs
  - `final_food_delivery_dataset.csv`: Final merged dataset

## Requirements

- Python 3.x
- pandas
- sqlite3 (for SQL data)

Install dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Place your data files in the `data/` directory
2. Run the data merger script:
   ```
   python scripts/data_merger.py
   ```
3. Check the output in the `output/` directory

## Data Analysis

The analysis includes:
- Merging order, user, and restaurant data
- Data cleaning and preprocessing
- Generating insights on food delivery patterns

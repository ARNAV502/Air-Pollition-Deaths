# Air Pollution Deaths Analysis

This project visualizes death rates caused by air pollution across different regions using a CSV dataset. The data is grouped and filtered to highlight patterns by world region, income level, and socio-demographic index (SDI). The final output is a line graph showing trends over time.

## Features

- Reads and processes a dataset on death rates from air pollution.
- Cleans the data by handling missing values and filtering out unwanted rows.
- Separates data into multiple categories such as:
  - Global regions
  - High-income countries
  - Socio-demographic index (SDI) groups
  - UK constituent countries
- Visualizes trends using a multi-line plot.

## Visualization

The script generates a line graph:
- **X-axis**: Year  
- **Y-axis**: Deaths per 100,000 people  
- **Lines**: Represent different world regions

The `fivethirtyeight` style is used for clear, professional visuals.

## Dependencies

- `pandas`
- `numpy`
- `matplotlib`

Install them via pip if needed:
```bash
pip install pandas numpy matplotlib

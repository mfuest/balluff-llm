# Data Directory

This directory contains the data used for training and evaluating the Balluff LLM model.

## Directory Structure

```
data/
├── raw/              # Raw data files (not tracked in git)
├── processed/        # Processed data ready for training
└── README.md         # This file
```

## Data Processing

The raw data consists of Balluff product datasheets and documentation. The processing pipeline:

1. Data cleaning and normalization
2. Conversion to JSON format
3. Application of TinyLlama chat template
4. Train/validation split

## Data Format

Processed data is stored in JSON format with the following structure:

```json
{
    "system": "You are a helpful assistant for Balluff products.",
    "user": "What is the minimum distance between two BIS M-408-045-001-07-S4 Read/Write Devices?",
    "assistant": "The minimum distance between two BIS M-408-045-001-07-S4 Read/Write Devices is 40mm."
}
```

## Data Privacy

- Raw data files are not tracked in git
- Processed data is anonymized and contains no sensitive information
- All data is used in accordance with Balluff's data usage policies

## Data Processing Scripts

The data processing scripts are located in `src/data/`:

- `clean_data.py`: Cleans and normalizes raw data
- `convert_to_json.py`: Converts cleaned data to JSON format
- `apply_template.py`: Applies the TinyLlama chat template
- `split_data.py`: Splits data into train and validation sets

## Usage

To process new data:

1. Place raw data files in `data/raw/`
2. Run the processing pipeline:
```bash
python src/data/clean_data.py
python src/data/convert_to_json.py
python src/data/apply_template.py
python src/data/split_data.py
```

The processed data will be available in `data/processed/`. 
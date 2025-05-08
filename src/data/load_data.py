"""
Data loading and preprocessing utilities for Balluff LLM.

This module provides functions to load and preprocess Balluff product data
from various sources (Excel, JSON) into a format suitable for model training.
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict, List, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_excel_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load data from Excel file containing Balluff product information.
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        DataFrame containing the product data
        
    Raises:
        FileNotFoundError: If the Excel file doesn't exist
        ValueError: If the Excel file is not properly formatted
    """
    try:
        df = pd.read_excel(file_path)
        logger.info(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        logger.error(f"Excel file not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading Excel file: {str(e)}")
        raise ValueError(f"Invalid Excel file format: {str(e)}")

def preprocess_data(df: pd.DataFrame) -> List[Dict]:
    """
    Preprocess the raw data into a format suitable for model training.
    
    Args:
        df: DataFrame containing raw product data
        
    Returns:
        List of dictionaries containing processed examples
    """
    processed_data = []
    
    for _, row in df.iterrows():
        # Create context from product information
        context = f"Product: {row.get('product_name', '')}\n"
        context += f"Type: {row.get('product_type', '')}\n"
        context += f"Specifications: {row.get('specifications', '')}"
        
        # Create example
        example = {
            "context": context,
            "prompt": row.get('question', ''),
            "response": row.get('answer', '')
        }
        processed_data.append(example)
    
    logger.info(f"Processed {len(processed_data)} examples")
    return processed_data

def save_processed_data(data: List[Dict], output_path: Union[str, Path]):
    """
    Save processed data to JSON file.
    
    Args:
        data: List of processed examples
        output_path: Path to save the JSON file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    logger.info(f"Saved processed data to {output_path}")

def main():
    """Main function to demonstrate data loading and preprocessing."""
    # Example usage
    data_dir = Path("data")
    raw_data_path = data_dir / "raw" / "Data_Balluff.xlsx"
    processed_data_path = data_dir / "processed" / "processed_data.json"
    
    # Load and process data
    df = load_excel_data(raw_data_path)
    processed_data = preprocess_data(df)
    save_processed_data(processed_data, processed_data_path)

if __name__ == "__main__":
    main() 
"""
Tests for data loading and preprocessing functionality.
"""

import unittest
from pathlib import Path
import pandas as pd
import json
import tempfile
import os

from src.data.load_data import load_excel_data, preprocess_data, save_processed_data

class TestDataLoading(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        
        # Create sample Excel data
        self.sample_data = pd.DataFrame({
            'product_name': ['BIS M-408-045-001-07-S4', 'BNI EIP-507-005-Z040'],
            'product_type': ['Read/Write Device', 'Ethernet/IP Gateway'],
            'specifications': ['40mm min distance', 'IP67 rating'],
            'question': ['What is the minimum distance?', 'What is the IP rating?'],
            'answer': ['40mm', 'IP67']
        })
        
        # Save sample data
        self.excel_path = self.test_path / 'test_data.xlsx'
        self.sample_data.to_excel(self.excel_path, index=False)
        
        # Create processed data directory
        self.processed_dir = self.test_path / 'processed'
        self.processed_dir.mkdir()

    def tearDown(self):
        """Clean up test data."""
        self.test_dir.cleanup()

    def test_load_excel_data(self):
        """Test loading data from Excel file."""
        df = load_excel_data(self.excel_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertEqual(list(df.columns), list(self.sample_data.columns))

    def test_preprocess_data(self):
        """Test data preprocessing."""
        processed_data = preprocess_data(self.sample_data)
        self.assertIsInstance(processed_data, list)
        self.assertEqual(len(processed_data), 2)
        
        # Check structure of processed data
        example = processed_data[0]
        self.assertIn('context', example)
        self.assertIn('prompt', example)
        self.assertIn('response', example)
        
        # Check content
        self.assertIn('BIS M-408-045-001-07-S4', example['context'])
        self.assertIn('40mm', example['response'])

    def test_save_processed_data(self):
        """Test saving processed data."""
        processed_data = preprocess_data(self.sample_data)
        output_path = self.processed_dir / 'test_processed.json'
        
        save_processed_data(processed_data, output_path)
        
        # Check if file exists
        self.assertTrue(output_path.exists())
        
        # Check if file can be loaded
        with open(output_path) as f:
            loaded_data = json.load(f)
        
        self.assertEqual(len(loaded_data), len(processed_data))
        self.assertEqual(loaded_data[0]['response'], processed_data[0]['response'])

    def test_invalid_excel_file(self):
        """Test handling of invalid Excel file."""
        invalid_path = self.test_path / 'nonexistent.xlsx'
        with self.assertRaises(FileNotFoundError):
            load_excel_data(invalid_path)

if __name__ == '__main__':
    unittest.main() 
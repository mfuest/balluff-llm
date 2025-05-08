# Balluff LLM Pipeline

This document describes the execution order and purpose of each notebook in the project.

## Pipeline Overview

1. **Data Preparation** (`data_preparation.ipynb`)
   - Loads raw Balluff product data
   - Cleans and normalizes the data
   - Converts to the TinyLlama chat template format
   - Splits into train/validation sets

2. **Model Training** (`finetuning_framework.ipynb`)
   - Loads the TinyLlama base model
   - Applies LoRA fine-tuning
   - Saves the fine-tuned model

3. **Model Evaluation** (`evaluation.ipynb`)
   - Measures memory usage and inference speed
   - Evaluates accuracy on validation set
   - Assesses response quality

4. **Edge Deployment** (`edge_inference/quantization.ipynb`)
   - Quantizes the model for edge devices
   - Tests inference on Raspberry Pi
   - Measures performance metrics

## Execution Order

1. First, run `data_preparation.ipynb` to prepare your training data
2. Then, run `finetuning_framework.ipynb` to train the model
3. Use `evaluation.ipynb` to validate the model's performance
4. Finally, use `edge_inference/quantization.ipynb` for edge deployment

## Requirements

Each notebook has its own requirements section, but generally:
- `data_preparation.ipynb`: pandas, openpyxl
- `finetuning_framework.ipynb`: transformers, peft, torch
- `evaluation.ipynb`: transformers, psutil, datasets
- `edge_inference/quantization.ipynb`: onnxruntime, torch

## Expected Outputs

1. `data_preparation.ipynb`:
   - `data/processed/train.json`
   - `data/processed/validation.json`

2. `finetuning_framework.ipynb`:
   - `models/tinyllama-finetuned/`

3. `evaluation.ipynb`:
   - Performance metrics
   - Evaluation results

4. `edge_inference/quantization.ipynb`:
   - Quantized model
   - Edge device performance metrics 
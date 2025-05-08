# Balluff LLM - Fine-tuned TinyLlama

A lightweight, fine-tuned model for answering questions about Balluff sensors and industrial automation products. This project uses the TinyLlama 1.1B base model with LoRA fine-tuning for efficient adaptation to the industrial automation domain.

## Table of Contents
1. [Quick Start](#quick-start)
2. [Project Overview](#project-overview)
3. [Installation](#installation)
4. [Development Pipeline](#development-pipeline)
5. [Project Structure](#project-structure)
6. [Data Handling](#data-handling)
7. [Model Performance](#model-performance)
8. [Contributing](#contributing)
9. [Limitations](#limitations)

## Quick Start

### Prerequisites
- [Ollama](https://ollama.ai/download) installed
- 4GB RAM minimum for inference
- Python 3.10 or higher
- Conda (recommended) or pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/balluff-llm.git
cd balluff-llm
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate balluff-llm
```

Or install with pip:
```bash
pip install -r requirements.txt
```

### Running Inference
```bash
# Pull and run the model
ollama run balluff-sensors

# Or use the API
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "balluff-sensors",
  "prompt": "What sensors does Balluff offer for level detection?"
}'
```

## Project Overview

This project aims to create a lightweight language model specifically trained for Balluff product documentation. The model is optimized for edge devices with limited resources (4GB RAM) while maintaining high accuracy on product-specific queries.

### Example Queries
```
> What is the minimum distance between two BIS M-408-045-001-07-S4 Read/Write Devices?
> What is the factory IP address of the BNI EIP-507-005-Z040?
> Can I use the BNI EIP-507-005-Z040 in applications with ambient temperatures of 80°C?
> What does it mean when the status LED US flashes red on a BNI XG5-508-0B5-R067?
```

## Development Pipeline

The project follows a structured development pipeline:

1. **Data Preparation** (`notebooks/data_preparation.ipynb`)
   - Loads raw Balluff product data
   - Cleans and normalizes the data
   - Converts to the TinyLlama chat template format
   - Splits into train/validation sets

2. **Model Training** (`notebooks/finetuning_framework.ipynb`)
   - Loads the TinyLlama base model
   - Applies LoRA fine-tuning
   - Saves the fine-tuned model

3. **Model Evaluation** (`notebooks/evaluation.ipynb`)
   - Measures memory usage and inference speed
   - Evaluates accuracy on validation set
   - Assesses response quality

4. **Edge Deployment** (`edge_inference/quantization.ipynb`)
   - Quantizes the model for edge devices
   - Tests inference on Raspberry Pi
   - Measures performance metrics

### Training Process
- **Technique:** Parameter-Efficient Fine-Tuning (LoRA) via PEFT on a quantized TinyLlama backbone
- **Infrastructure:** Google Colab with NVIDIA A100 and T4 GPUs
- **Split:** ~90% train / 10% validation
- **Duration & Cost:** 8.47 A100-GPU h (~1 h 56 m) and 1.66 T4-GPU h (~3 h 47 m)
- **Hyperparameters:** 
  - LoRA adapters on attention projections
  - Frozen base weights
  - Low-rank matrices trained over multiple epochs

## Project Structure
```
📦 balluff-llm
├── 📂 edge_inference/         # Edge device deployment
│   └── 📜 quantization.ipynb  # Model quantization for edge
├── 📂 models/                 # Fine-tuned models
│   ├── 📂 tinyllama-finetuned/# LoRA adapter weights
│   └── 📂 tinyllama-merged/   # Merged model
├── 📂 data/                   # Training data
│   ├── 📂 raw/               # Raw data (not tracked)
│   └── 📂 processed/         # Processed training data
├── 📂 notebooks/             # Jupyter notebooks
│   ├── 📜 data_preparation.ipynb
│   ├── 📜 finetuning_framework.ipynb
│   └── 📜 evaluation.ipynb
├── 📂 src/                   # Source code
│   └── 📂 data/             # Data processing scripts
├── 📂 tests/                 # Test files
├── 📜 environment.yml        # Conda environment
├── 📜 requirements.txt       # Pip requirements
└── 📜 README.md             # This file
```

## Data Handling

### Data Format
Processed data is stored in JSON format:
```json
{
    "context": "Product information and specifications",
    "prompt": "User question about the product",
    "response": "Accurate answer based on specifications"
}
```

### Data Processing
The `src/data/load_data.py` script handles:
- Loading raw Excel data
- Cleaning and normalization
- Converting to training format
- Splitting into train/validation sets

## Model Performance

The fine-tuned model shows significant improvements:

| Model | Accuracy on Validation Set | Strong Performance Areas |
|-------|----------------------------|--------------------------|
| TinyLlama 1.1B (base) | 18.75% | General knowledge questions |
| Balluff-sensors (fine-tuned) | 37.50% | Product specifications, temperature ranges, distances, IP addresses |

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repo and create your branch from `main`
2. Add tests for any new functionality
3. Ensure tests pass and code is properly formatted
4. Submit a pull request

### Development Process
- Use [black](https://github.com/psf/black) for code formatting
- Use [flake8](https://flake8.pycqa.org/) for linting
- Use [mypy](https://mypy.readthedocs.io/) for type checking
- Write tests for new features
- Update documentation for changes

### Data Privacy and Security
- All contributions must respect Balluff's data privacy policies
- Do not include sensitive product information in commits
- Follow Balluff's guidelines for handling product documentation
- Ensure all data processing follows Balluff's data handling procedures

## Limitations

The current fine-tuned model:
- Shows improvement (37.50% vs 18.75%) over the base model on validation tests
- Works best for direct questions about product specifications
- May provide incorrect information for complex technical questions
- Requires tuning generation parameters for optimal results (temperature: 0.7, top_p: 0.9)

## Contributors
- Maximilian Fuest
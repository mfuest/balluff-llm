# Edge-Optimized LLM for Local Inference

A lightweight, fine-tuned Large Language Model (LLM) optimized for deployment on resource-constrained edge devices. This project uses **TinyLlama** fine-tuned with **Low-Rank Adaptation (LoRA)** to enable local inference while ensuring data privacy and low-latency responses. The Model was built for answering product related questions about BALLUFF Sensors.

## Quick Start

### Prerequisites
- Python 3.8 or higher
- At least 4GB RAM (for edge devices)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/mfuest/balluff-llm.git
cd balluff-llm
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Model
To run inference on your device:
```bash
python src/model/run_model.py --model_path models/tinyllama-finetuned/
```

## Project Structure
```
📦 balluff-llm
├── 📂 src/                      # Source code
│   ├── 📂 model/               # Model-related code
│   │   └── 📜 run_model.py     # Inference script
│   ├── 📂 data/                # Data processing code
│   └── 📂 utils/               # Utility functions
├── 📂 models/                   # Model files
│   └── 📂 tinyllama-finetuned/ # Fine-tuned model
├── 📂 data/                     # Data directory
│   ├── 📜 Data_Balluff.xlsx    # Raw data
│   └── 📂 processed/           # Processed data
├── 📂 notebooks/               # Jupyter notebooks
├── 📂 tests/                   # Test files
├── 📜 requirements.txt         # Dependencies
├── 📜 setup.py                 # Package setup
└── 📜 README.md               # Documentation
```

## Model Details

### Performance Characteristics
- Inference Speed: ~13 tokens per second
- Memory Usage: ~2.2GB (quantized)
- Validation Accuracy: ~75% on domain-specific tasks

### Technical Specifications
- Base Model: TinyLlama
- Fine-tuning Method: LoRA (Low-Rank Adaptation)
- Quantization: Applied for edge deployment
- Target Devices: Low-memory devices (e.g., Raspberry Pi 5 with 4/8GB RAM)

## Development

### Running Tests
```bash
python -m unittest discover tests
```

### Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Submit a pull request with improvements
3. Open an issue for bug reports or feature requests

## References
- 🔗 [Fine-Tuned Model on Hugging Face](https://huggingface.co/YusufGun/Final)

## Contributors
- Maximilian Fuest
- Yusuf A. Gün
- Yufei Xu


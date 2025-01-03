# TinyLlama Fine-Tuning with LoRA (PEFT)

This repository contains a Jupyter notebook and accompanying scripts to fine-tune **TinyLlama** on Apple Silicon (M1/M2) or CPU using LoRA (PEFT). By training only a small set of additional parameters, LoRA drastically reduces GPU memory usage—making it possible to fine-tune a 1.1B-parameter model on machines with limited VRAM.

## Contents

- **`notebook.ipynb`**: A Jupyter notebook demonstrating:
  - Loading the TinyLlama model
  - Applying LoRA (PEFT) for parameter-efficient training
  - Tokenizing a JSON dataset (with "context", "prompt", "response")
  - Fine-tuning on Apple Silicon GPU (MPS) or CPU fallback
- **`data/validation_checklist_context.json`** (example): A JSON dataset containing custom training data.

## Requirements

- Python 3.10 or 3.11 recommended
- `torch` (with MPS support if on macOS)
- `transformers >= 4.30`
- `datasets`
- `sentencepiece`
- `peft` (for LoRA)
- A machine with at least 8GB of RAM (preferably more)

**Install dependencies**:

```bash
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip install transformers datasets sentencepiece peft
# Balluff LLM - Fine-tuned TinyLlama

A lightweight, fine-tuned model for answering questions about Balluff sensors and industrial automation products. This project uses the TinyLlama 1.1B base model with LoRA fine-tuning for efficient adaptation to the industrial automation domain.

## Performance Overview

The fine-tuned model shows significant improvements over the base model:

| Model | Accuracy on Validation Set | Strong Performance Areas |
|-------|----------------------------|--------------------------|
| TinyLlama 1.1B (base) | 18.75% | General knowledge questions |
| Balluff-sensors (fine-tuned) | 37.50% | Product specifications, temperature ranges, distances, IP addresses |

## Quick Start with Ollama

### Prerequisites
- [Ollama](https://ollama.ai/download) installed
- 4GB RAM minimum for inference

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

## Example Queries

```
> What is the minimum distance between two BIS M-408-045-001-07-S4 Read/Write Devices?
> What is the factory IP address of the BNI EIP-507-005-Z040?
> Can I use the BNI EIP-507-005-Z040 in applications with ambient temperatures of 80°C?
> What does it mean when the status LED US flashes red on a BNI XG5-508-0B5-R067?
```

## Advanced Usage

### Creating Your Own Model

If you have the fine-tuned LoRA weights, you can create your own Ollama model:

1. Merge LoRA weights with base model:
```bash
python merge_lora.py \
  --adapter_path models/tinyllama-finetuned \
  --output_dir models/tinyllama-merged \
  --base_model TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

2. Create Ollama model:
```bash
python convert_to_ollama.py --model_path models/tinyllama-merged --name balluff-sensors
ollama create balluff-sensors -f Modelfile
```

### Fine-tuning Your Own Version

For best results with LoRA fine-tuning, we recommend:
```bash
python finetune_lora.py \
  --base_model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
  --dataset your-balluff-data \
  --lora_r 8 \
  --lora_alpha 16 \
  --lora_dropout 0.1 \
  --learning_rate 5e-5 \
  --weight_decay 0.001 \
  --num_train_epochs 5
```

## Project Structure
```
📦 balluff-llm
├── 📂 models/                  # Fine-tuned models
│   ├── 📂 tinyllama-finetuned/ # LoRA adapter weights
│   └── 📂 tinyllama-merged/    # Merged model (created by merge_lora.py)
├── 📂 data/                    # Training data
│   └── 📂 processed/           # Processed training data
├── 📜 merge_lora.py            # Script to merge LoRA weights with base model
├── 📜 convert_to_ollama.py     # Script to convert model to Ollama format
└── 📜 README.md                # This file
```

## Fine-Tuning Process
- **Technique:** Parameter-Efficient Fine-Tuning (LoRA) via PEFT on a quantized TinyLlama backbone.
- **Data Preparation:** Balluff product datasheets were cleaned, normalized, and converted into JSON records using the TinyLlama chat template (`<|system|>`, `<|user|>`, `<|assistant|>`).
**Training Setup:**
- **Infrastructure:** Google Colab with NVIDIA A100 and T4 GPUs  
- **Split:** ~90 % train / 10 % validation  
- **Duration & Cost:** 8.47 A100‑GPU h (~1 h 56 m) and 1.66 T4‑GPU h (~3 h 47 m)  
- **Hyperparameters:** LoRA adapters on attention projections, frozen base weights, low‐rank matrices trained over multiple epochs  

## Limitations

The current fine-tuned model:
- Shows improvement (37.50% vs 18.75%) over the base model on validation tests
- Works best for direct questions about product specifications
- May provide incorrect information for complex technical questions
- Requires tuning generation parameters for optimal results (temperature: 0.7, top_p: 0.9)

## Contributors
- Maximilian Fuest
# Edge-Optimized LLM Fine-Tuning and Deployment

## Overview
This repository contains the code and data for fine-tuning a lightweight Large Language Model (LLM) for deployment on resource-constrained edge devices. The project focuses on adapting the **TinyLlama** model using **Low-Rank Adaptation (LoRA)** for parameter-efficient fine-tuning. The primary objective is to achieve **on-device inference** while ensuring **data privacy** and **low-latency responses** without reliance on cloud services.

---

## Features
- **Fine-Tuning with LoRA** – Efficient adaptation of a pre-trained TinyLlama model.
- **Quantization for Edge Deployment** – Optimized memory and computational efficiency.
- **Edge Device Compatibility** – Runs on low-memory devices (e.g., Raspberry Pi 5).
- **Domain-Specific Data** – Fine-tuned on structured, domain-specific datasets.
- **Performance Evaluations** – Benchmarks include speed, accuracy, and memory usage.

---

## Repository Structure
```
📦 edge-llm-finetuning
 ┣ 📂 4GB_edge_device/        # Fine-tuned model files and checkpoints
 ┣ 📂 data/                   # Preprocessed training and validation datasets
 ┣ 📜 run_model.py            # Script to run inference on the edge device
 ┣ 📜 README.md               # Documentation file
 ┣ 📜 .gitignore              # Git ignore rules
 ┗ 📜 Data_Sample.xlsx        # Example dataset file
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mfuest/edge-llm-finetuning.git
cd edge-llm-finetuning
```

### 2. Install Dependencies
Ensure you have **Python 3.8 or higher**, then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Running the Model on an Edge Device
Execute the following command:
```bash
python run_model.py --model_path 4GB_edge_device/tinyllama-finetuned/
```

---

## Fine-Tuning Process

### Model Selection
Several models were initially evaluated under strict memory constraints. Due to the **limited resources of edge devices**, the **TinyLlama** model was selected as the best candidate for fine-tuning.

### Data Preprocessing
- **Data Extraction** – Text and tabular data were extracted from documentation sources.
- **Normalization** – The extracted data was cleaned and formatted into a structured JSON format.
- **Formatting** – Data was transformed into a **context-prompt-response** structure to align with the model's expected input.

### Fine-Tuning Implementation
- **Methodology** – LoRA was used for efficient parameter adaptation.
- **Training Environment** – Training was performed on **cloud-based GPUs**.
- **Model Deployment** – The final model was **quantized and optimized** for edge inference.

---

## Performance & Evaluation

- **Inference Speed** – ~13 tokens per second.
- **Validation Accuracy** – ~75% correctness in domain-specific test cases.
- **Memory Usage** – The quantized model requires ~2.2GB, making it suitable for low-memory devices.

---

## Alternative Approaches

A **Retrieval-Augmented Generation (RAG)** approach was also explored. While **RAG offered faster inference speeds**, it delivered **lower accuracy** on domain-specific queries. Therefore, **fine-tuning** was chosen as the preferred method.

---

## Limitations & Future Work
- **Data Augmentation** – Increasing dataset size and diversity could enhance accuracy.
- **Model Compression** – Further quantization and pruning could improve deployment efficiency.
- **Hybrid Strategies** – Combining fine-tuning with RAG could provide a balance between adaptability and accuracy.
- **Scalability** – Further optimization is needed for broader deployment across different edge devices.

---

## Contributors

- **Maximilian Fuest** – Edge device testing, fine-tuning implementation, technical documentation.
- **Yufei Xu** – Implementation of alternative methods and evaluation.
- **Yusuf A. Gün** – Data preprocessing, model training, validation, and performance analysis.

---

## References

- 🔗 [Fine-Tuned Model on Hugging Face](https://huggingface.co/YusufGun/Final)

---

## Contributing
Contributions are welcome!  
To contribute:
1. **Fork the repository**  
2. **Submit a pull request** with improvements  
3. **Open an issue** for bug reports or feature requests  


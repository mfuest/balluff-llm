You’re right! Here’s the properly formatted README.md with correct code blocks, bullet points, and structure for a clean and professional presentation.

⸻

README.md

# Edge-Optimized LLM Fine-Tuning and Deployment

## Overview
This repository contains the code and data for fine-tuning a lightweight Large Language Model (LLM) for deployment on resource-constrained edge devices. The project focuses on adapting the TinyLlama model using a parameter-efficient fine-tuning technique known as Low-Rank Adaptation (LoRA). The primary objective is to achieve on-device inference without reliance on cloud services, ensuring data privacy and reducing latency in industrial applications.

---

## Features
- **Fine-Tuning with LoRA**: Efficient adaptation of a pre-trained TinyLlama model using PEFT methods.
- **Quantization for Edge Deployment**: Model quantization reduces memory and computational requirements.
- **Edge Device Compatibility**: Optimized for low-memory devices (4GB and 8GB RAM).
- **Structured Training Data**: Preprocessed datasets formatted for fine-tuning.
- **Performance Evaluation**: Benchmarks include response speed, accuracy, and resource usage.

---

## Repository Structure

📦 edge-llm-finetuning
┣ 📂 4GB_edge_device/        # Fine-tuned model files and checkpoints
┣ 📂 data/                   # Preprocessed training and validation datasets
┣ 📜 run_model.py            # Script to run inference on the edge device
┣ 📜 README.md               # This documentation file
┣ 📜 .gitignore              # Git ignore rules
┗ 📜 Data_Sample.xlsx        # Example dataset file

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mfuest/edge-llm-finetuning.git
cd edge-llm-finetuning

2️⃣ Install Dependencies

Ensure you have Python 3.8 or higher, then install the required packages:

pip install -r requirements.txt

3️⃣ Running the Model on an Edge Device

Execute the following command to run the model:

python run_model.py --model_path 4GB_edge_device/tinyllama-finetuned/



⸻

Fine-Tuning Process

Model Selection

Initial experiments evaluated several models under strict memory constraints. Due to the limited resources of edge devices, the TinyLlama model was selected as the best candidate for fine-tuning.

Data Preprocessing
	•	Data Extraction: Text and tabular data were extracted from various documentation sources.
	•	Normalization: Data were cleaned and converted into a structured context-prompt-response format.
	•	Formatting: The dataset was prepared according to the model’s expected input template.

Fine-Tuning Implementation
	•	Methodology: The fine-tuning utilizes LoRA for parameter-efficient adaptation.
	•	Training Environment: Conducted on cloud-based GPU resources.
	•	Model Deployment: The final model was quantized and validated for efficient deployment.

⸻

Performance and Evaluation
	•	Inference Speed: The fine-tuned model processes an average of ~13 tokens per second.
	•	Validation Accuracy: Approximately 75% of domain-specific queries return correct responses.
	•	Resource Usage: The quantized model requires ~2.2GB of storage, fitting within the constraints of typical low-memory edge devices.

⸻

Alternative Approaches

An alternative approach using Retrieval-Augmented Generation (RAG) was explored. While RAG offered faster inference speeds, it resulted in lower accuracy on domain-specific queries. Consequently, fine-tuning was chosen as the preferred approach.

⸻

Limitations and Future Work
	•	Data Augmentation: Expanding and diversifying the training dataset could further improve performance.
	•	Model Compression: Additional quantization or pruning techniques may reduce memory usage further.
	•	Hybrid Strategies: Combining fine-tuning with retrieval-based methods might enhance adaptability without retraining.
	•	Scalability: Future work will investigate optimizing for a broader range of edge devices.

⸻

Contributors
	•	Maximilian Fuest – Edge device testing, fine-tuning implementation, technical documentation.
	•	Yufei Xu – Implementation of alternative methods and evaluation.
	•	Yusuf A. Gün – Data preprocessing, model training, validation, and performance analysis.

⸻

References
	•	📄 Project Report (PDF)
	•	🔗 Fine-Tuned Model on Hugging Face

⸻

License

This project is licensed under the MIT License. See the LICENSE file for details.

⸻

Contributing

Contributions are welcome!
To contribute:
	1.	Fork the repository
	2.	Submit a pull request with improvements
	3.	Open an issue for bug reports or feature requests

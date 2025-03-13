# Balluff-LLM: Fine-Tuning LLMs for Edge Deployment

## Overview
This project explores the **fine-tuning and deployment of Large Language Models (LLMs) on resource-constrained edge devices**, specifically **Raspberry Pi 5 (4GB & 8GB RAM)**, for **industrial applications at Balluff**. 

We fine-tuned **TinyLlama**, a lightweight model, using **Low-Rank Adaptation (LoRA)** to optimize it for **on-device inference**. The primary goal was to **enable privacy-preserving LLM deployments** without relying on cloud services, making it viable for **industrial environments with strict data regulations**.

## Features
- ✅ **Fine-tuning**: Applied **LoRA-based PEFT** to efficiently adapt TinyLlama with minimal resources.
- ✅ **Quantization**: Optimized the model for edge deployment using **BitsAndBytes**.
- ✅ **Raspberry Pi 5 Deployment**: Evaluated feasibility on both **4GB and 8GB** versions.
- ✅ **Industrial Use Case**: Trained on **Balluff product-specific data** for real-world industrial applications.
- ✅ **Performance Evaluations**: Benchmarked response speed, accuracy, and feasibility.

---

## Project Structure

📦 balluff-llm
┣ 📂 4GB_rpi5_LLM/      # TinyLlama fine-tuned model & checkpoints
┣ 📂 data/              # Preprocessed Balluff product data
┣ 📜 RAG.ipynb          # Alternative RAG-based approach (not used in final version)
┣ 📜 README.md          # This file
┣ 📜 .gitignore         # Git ignore rules
┗ 📜 Data_Balluff.xlsx  # Sample dataset (if applicable)

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/mfuest/balluff-llm.git
cd balluff-llm

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Model on Raspberry Pi

python run_model.py --model_path 4GB_rpi5_LLM/tinyllama-finetuned-mps/



⸻

🏗️ Fine-Tuning Process

Model Selection

We initially tested Mistral 7B and TinyLlama, but due to memory constraints on Raspberry Pi 5, we focused on TinyLlama.

Data Preprocessing
	•	Extracted Balluff product data (PDF datasheets)
	•	Converted to structured context-prompt-response format
	•	Cleaned and normalized data using ChatGPT-assisted preprocessing

Fine-Tuning Approach
	•	LoRA (Low-Rank Adaptation) for parameter-efficient fine-tuning
	•	Training performed on Google Colab (A100, T4 GPUs)
	•	Final model uploaded to Hugging Face: Final Model

⸻

🏁 Results & Performance
	•	Response Speed: ~13 tokens/sec
	•	Validation Accuracy: ~75% correct responses on industrial test cases
	•	Memory Usage: 2.2GB fine-tuned model (fits within Raspberry Pi 5 constraints)
	•	Trade-offs: LLM struggles with numerical data consistency (e.g., IP addresses)

⸻

🔄 Alternative Approaches: Retrieval-Augmented Generation (RAG)

We also explored RAG (Retrieval-Augmented Generation) but found:
	•	Faster inference (~49 tokens/sec)
	•	Lower accuracy (0% correct responses in test cases)
	•	Higher adaptability (no fine-tuning required)

Ultimately, we chose fine-tuning over RAG due to better domain-specific accuracy.

⸻

📌 Limitations & Future Work
	•	🚧 Data Augmentation: More training data could improve accuracy
	•	🚧 Model Compression: Further quantization to reduce RAM footprint
	•	🚧 Hybrid Approach: Combining RAG + fine-tuning for dynamic queries
	•	🚧 Multi-device Optimization: Scaling to other edge devices beyond Raspberry Pi

⸻

👨‍💻 Contributors
	•	Maximilian Fuest – Raspberry Pi LLM testing, fine-tuning code, report writing
	•	Yufei Xu – RAG implementation, evaluation, report writing
	•	Yusuf A. Gün – Data preprocessing, fine-tuning, model training, validation

⸻

📜 References
	•	TUM x Balluff AI Project Report
	•	Fine-Tuned Model on Hugging Face
### **Next Steps**
✅ **Copy this `README.md` to your GitHub repo**  
✅ **Update any missing details (e.g., dataset access, additional dependencies)**  
✅ **Add installation & usage details based on your actual code structure**  

Let me know if you'd like any modifications! 🚀

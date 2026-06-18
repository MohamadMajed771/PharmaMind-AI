# PharmaMind AI

PharmaMind AI is an AI-powered drug information assistant designed for pharmacy students and pharmacists. It generates detailed drug monographs, dosing information, contraindications, interactions, counseling points, and exam-focused study notes using a locally hosted Large Language Model (LLM).

## Features

* Drug monograph generation
* Mechanism of action explanations
* Indications and therapeutic uses
* Adult and pediatric dosing information
* Contraindications and precautions
* Drug-drug and drug-food interactions
* Side effects and adverse reactions
* Pregnancy and lactation information
* Patient counseling points
* Pharmacist clinical pearls
* Exam-focused study notes
* Drug name validation and correction

## Technologies

* Python
* Streamlit
* Ollama
* Llama 3.2
* RapidFuzz

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MohamadMajed771/PharmaMind-AI.git
cd PharmaMind-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama:

https://ollama.com

### 6. Download the Llama 3.2 model

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

### 7. Run the application

```bash
streamlit run app.py
```

## Example Drugs

* Paracetamol
* Amoxicillin
* Metformin
* Dapagliflozin
* Atorvastatin
* Warfarin
* Omeprazole

## Disclaimer

This application is intended for educational purposes only. Drug information should always be verified using official references, clinical guidelines, and professional judgment before making healthcare decisions.

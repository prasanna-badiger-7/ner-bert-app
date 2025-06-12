
# 🧠 Named Entity Recognition (NER) with BERT

This is a web-based Named Entity Recognition (NER) tool powered by a fine-tuned BERT model, built using PyTorch, Hugging Face Transformers, and Streamlit.

## 🚀 Demo

Try the live app:  
👉 Huggingface[https://prasannabadiger7-bert-ner-gradio.hf.space/?logs=container&__theme=system&deep_link=-08HBmLAbfc]

---

## 📌 Features

- 🔎 Extracts and highlights entities in raw text (PER, LOC, ORG, etc.)
- 💬 Clean and interactive Streamlit UI
- 🧠 Fine-tuned on the CoNLL-2003 dataset
- ☁️ Deployable via Streamlit Cloud or Hugging Face Spaces

---

## 🖥️ Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/prasanna-badiger-7/ner-bert-app.git
   cd ner-bert-app
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

```
ner-bert-app/
│
├── app.py               # Streamlit frontend
├── ner_model/           # Saved model & tokenizer
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🧠 Model

Fine-tuned `bert-base-cased` on the CoNLL-2003 dataset using Hugging Face Transformers and Datasets.

---

## 📦 Dependencies

- `gradio`
- `transformers`
- `torch`

Install all with:
```bash
pip install -r requirements.txt
```

---

## 📸 Example

![Demo Screenshot](demo.jpg)

---

## 🧑‍💻 Author

Made with ❤️ by [Prasanna](https://github.com/prasanna-badiger-7)

---

## 📜 License

MIT License

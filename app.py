from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import streamlit as st

model = AutoModelForTokenClassification.from_pretrained('./ner_model')
tokenizer = AutoTokenizer.from_pretrained('./ner_model')
label_list = model.config.id2label


def predict_entities(text):
    tokens = tokenizer(text, return_tensors='pt', truncation=True, is_split_into_words=False)
    with torch.no_grad():
        outputs = model(**tokens)

    predictions = torch.argmax(outputs.logits, dim=2)
    tokens = tokens['input_ids'][0]
    prediction_ids = predictions[0]

    result = []
    for token_id, pred_id in zip(tokens, prediction_ids):
        token = tokenizer.decode([token_id])
        label = label_list[pred_id.item()]
        if token not in ['[CLS]', '[SEP]', '[PAD]']:
            result.append((token, label))
    return result

st.set_page_config(page_title="NER App", layout="wide")

st.title("🧠 Named Entity Recognition (NER) with BERT")
text_input = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    if text_input:
        results = predict_entities(text_input)
        st.markdown("### 🔍 Extracted Entities:")
        for word, label in results:
            if label != "O":
                st.markdown(f"**{word}** → `{label}`")
    else:
        st.warning("Please enter some text.")
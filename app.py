import gradio as gr
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Model repo on Hugging Face Hub
model_repo = "prasannabadiger7/ner-bert-model"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_repo)
model = AutoModelForTokenClassification.from_pretrained(model_repo)

# Define ID to label mapping (in case model config lacks it)
id2label = {
    0: "O",
    1: "B-PER",
    2: "I-PER",
    3: "B-ORG",
    4: "I-ORG",
    5: "B-LOC",
    6: "I-LOC",
    7: "B-MISC",
    8: "I-MISC"
}

# Attach to model config if needed
model.config.id2label = id2label
model.config.label2id = {v: k for k, v in id2label.items()}

# Create NER pipeline with aggregation
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Function to highlight entities in text
def ner_predict(text):
    entities = ner_pipeline(text)
    highlighted_text = text
    offset = 0

    for ent in entities:
        start, end = ent["start"], ent["end"]
        word = text[start:end]
        label = ent.get("entity_group", id2label.get(str(ent.get("entity", "UNK")), "UNK"))

        tag = (
            f"<mark style='background-color: #ffeaa7; padding: 2px 4px; border-radius: 4px;'>"
            f"{word} <sub style='color:#636e72; font-size: 0.8em;'>[{label}]</sub></mark>"
        )

        before = highlighted_text[:start + offset]
        after = highlighted_text[end + offset:]
        highlighted_text = before + tag + after
        offset += len(tag) - len(word)

    return highlighted_text

# Gradio interface
iface = gr.Interface(
    fn=ner_predict,
    inputs=gr.Textbox(lines=4, placeholder="Enter text here...", label="Input Text"),
    outputs=gr.HTML(label="Named Entities"),
    title="🧠 Named Entity Recognition with BERT",
    description="Enter a sentence to extract named entities (PER, LOC, ORG, etc.) using a BERT model fine-tuned on NER.",
    examples=[
        ["Barack Obama was born in Hawaii."],
        ["Apple Inc. is based in Cupertino."]
    ],
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()

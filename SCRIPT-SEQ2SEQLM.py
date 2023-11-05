import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the BART model
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")

# Generate text
text = model.generate(
    input_ids=tokenizer("The video script is as follows:", return_tensors="pt").input_ids,
    max_length=1024,
    temperature=8.0,
    eos_token_id=1,
    do_sample=True,
    top_k=50,
    top_p=0.9,
)


# Print the generated text
print(text)

# Decode the output tokens
decoded_text = tokenizer.decode(text[0], skip_special_tokens=True)

# Change the encoding to UTF-8
cleaned_text = decoded_text.encode("utf-8")

# Print the cleaned text
print(cleaned_text)
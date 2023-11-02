import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the BART model
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")

# Generate text
text = model.generate(
    input_ids=tokenizer("The video script is as follows:", return_tensors="pt").input_ids,
    max_length=512,
    eos_token_id=1,
    do_sample=True,
    top_k=50,
    top_p=0.9,
)

# Print the generated text
print(text)

# Convert the output tensor to a string
text_string = text.decode("utf-8")

# Print the generated text
print(text_string)


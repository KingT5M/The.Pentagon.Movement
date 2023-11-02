import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the BigBird model as a causal language model
model = AutoModelForCausalLM.from_pretrained("google/bigbird-roberta-base", prefix="bigbird-roberta-base", is_decoder=True)
tokenizer = AutoTokenizer.from_pretrained("google/bigbird-roberta-base")


# Generate text
text = model.generate(
    input_ids=None,
    max_length=512,
    eos_token_id=1,
    do_sample=True,
    top_k=50,
    top_p=0.9,
)

# Print the generated text
print(text)
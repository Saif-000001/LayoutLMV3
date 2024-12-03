from transformers import LayoutLMv3TokenizerFast

# Specify the local directory
local_dir = "./layoutlmv3Microsoft/"

# Download the tokenizer and save it locally
tokenizer = LayoutLMv3TokenizerFast.from_pretrained("microsoft/layoutlmv3-base")
tokenizer.save_pretrained(local_dir)

print(f"Tokenizer downloaded and saved at {local_dir}")

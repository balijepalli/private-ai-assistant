import os

USE_OLLAMA = os.getenv("USE_OLLAMA", "true").lower() == "true"

if USE_OLLAMA:
    from llm.ollama_llm import generate_response as ollama_generate
    generate_response = ollama_generate
else:
    from llm.transformer_llm import generate_response as transformer_generate
    generate_response = transformer_generate

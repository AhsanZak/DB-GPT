# Use DB-GPT base image
FROM eosphorosai/dbgpt-openai:latest

# Copy your configs into the image
COPY configs /app/configs

# Optional: install your RAG example
# RUN dbgpt app install awel-flow-rag-chat-example

# Default command
CMD ["dbgpt", "start", "webserver", "--config", "/app/configs/dbgpt-proxy-ollama.toml"]

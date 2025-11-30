# 🌱 Digital Roots - Docker Compose Configuration

services:
  digital-roots:
    build: .
    container_name: digital-roots-app
    ports:
      - "8501:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY:-}
...
      start_period: 40s

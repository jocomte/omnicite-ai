FROM python:3.12-slim

WORKDIR /app

# Zero external dependencies required (runs on Python standard library)
COPY server.py index.html /app/

ENV PORT=8000
EXPOSE 8000

CMD ["python", "server.py"]

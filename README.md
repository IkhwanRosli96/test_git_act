# Docker CI Sample

A tiny FastAPI app to test GitHub Actions with Docker and Docker Compose.

## Run locally

```bash
# Build
docker compose build

# Run
docker compose up -d

# Test
curl http://localhost:8000/
curl http://localhost:8000/health

# Stop
docker compose down -v
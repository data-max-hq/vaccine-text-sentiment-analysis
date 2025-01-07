FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync

COPY vaccine_analysis_app.py .
COPY images images

EXPOSE 8501

CMD ["uv", "run", "python", "-m", "streamlit", "run", "vaccine_analysis_app.py"]
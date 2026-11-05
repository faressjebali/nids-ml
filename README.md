# nids-ml

Machine learning for network intrusion and anomaly detection,
trained on UNSW-NB15 and evaluated for generalization on CIC-IDS2017.

> Work in progress.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12.

```bash
uv sync           # create .venv and install pinned dependencies
uv run pytest     # run tests
uv run ruff check .
```

Equivalent `make` targets: `make setup`, `make test`, `make lint`, `make format`.

## License

MIT

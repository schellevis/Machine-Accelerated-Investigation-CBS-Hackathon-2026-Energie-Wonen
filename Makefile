.PHONY: help setup setup-geo update jupyter test test-live clean

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Install core + visualisation + dev dependencies (recommended)
	uv sync --group dev --group viz
	@echo ""
	@echo "Setup complete. Run: make jupyter"

setup-geo: ## Install all dependencies including geographic mapping (geopandas)
	uv sync --all-groups
	@echo ""
	@echo "Full setup complete (incl. geopandas). Run: make jupyter"

update: ## Pull latest version of all skills (submodules)
	git submodule update --remote --merge

jupyter: ## Start JupyterLab
	uv run jupyter lab

test: ## Run unit tests (no network required)
	uv run pytest .kilo/skills/cbs-statline-skill/test_cbs_client.py \
		.kilo/skills/data-viz-journalism/tests/test_journalism_style.py -v

test-live: ## Run live CBS endpoint smoke tests (requires network)
	uv run python scripts/test_live_endpoints.py

clean: ## Remove virtual environment and cache files
	rm -rf .venv
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

# API Tests

API autotests for backend services.

## Stack
- Python
- Pytest
- Requests

## How to run
```bash
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

$env:BASE_URL="https://kz-lci-830.bb-online-stage.com/api/site_api/v1"

pytest

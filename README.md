# API Tests

API autotests for backend services.

## Stack
- Python
- Pytest
- Requests

## How to run
```bash
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

$env:BASE_URL="https://kz-lci-830.bb-online-stage.com/api/site_api/v1"
$env:TEST_ACCESS_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnYW1ibGVyX2lkIjoxNCwiZ2FtYmxlcklkIjoxNCwidXNlcl9pZCI6MSwiaGFsbF9pZCI6NTUwMiwid2FsbGV0X2lkIjoxNjE5ODMsIm5hbWUiOiJsb3RvMSIsImFjY291bnRfaWQiOiI0NTg5MDUiLCJpYXQiOjE3NzAyMjkyMTcsImV4cCI6MTc3MDQwOTIxN30.sENox661fk96Mh5W2-mKvQHhA9ox2Q8vkx0q8Rm95GE"
$env:DB_PASSWORD="*****"


pytest

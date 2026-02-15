# Test Automation Framework - LIA Pre-assignment
# valuelogic_test

Simple test automation solution using Python and Pytest.

## Requirements
- Python 
- pytest
- requests

## Installation
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run with verbose output:
```bash
pytest -v
```

## Test Cases

1. **test_one** - Basic sanity test
2. **test_that_file_data_is_correct** - File validation test that reads `testdata/hello.txt` and validates content
3. **test_get_posts** - API test that fetches a specific post and validates response
4. **test_get_all_posts** - API test that validates all posts are retrieved

## CI/CD

Tests run automatically on push via GitHub Actions. See `.github/workflows/` for pipeline configuration.

## API Used

JSONPlaceholder (https://jsonplaceholder.typicode.com) - Free fake REST API for testing.

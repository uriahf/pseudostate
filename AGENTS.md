This file provides instructions for AI agents to contribute to this project.

## Project Overview

The `pseudostate` library is a Python package for computing pseudo-observations in survival analysis, specifically for state occupation probabilities. It is designed for use in methodological work, simulations, and moderate sample sizes.

## Coding Style and Conventions

- **Docstrings**: All exported functions must have `numpydoc`-style docstrings to ensure compatibility with `quartodoc`.
- **Formatting**: Code should be formatted with `ruff format`.
- **Linting**: Code should be checked with `ruff check`.

## Testing

- All new features and bug fixes must be accompanied by unit tests.
- Tests are located in the `tests/` directory.
- To run the tests, use the following command: `pytest tests/`

## Continuous Integration

The project uses GitHub Actions for CI/CD. The CI pipeline runs on every push and pull request and executes the following checks:

- Runs the test suite with `pytest`.

## How to Contribute

1. Create a new branch for your feature or bug fix.
2. Make your changes, ensuring you follow the coding style and conventions.
3. Add or update tests as needed.
4. Run the pre-commit hooks to ensure your changes pass all checks.
5. Push your changes and create a pull request.

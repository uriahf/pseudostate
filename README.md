# pseudostate

[![PyPI version](https://badge.fury.io/py/pseudostate.svg)](https://badge.fury.io/py/pseudostate)

`pseudostate` is a Python library for computing Aalen-Johansen pseudo-observations at a fixed time horizon. This technique is useful in survival analysis for assessing covariate effects on cumulative incidence or state occupation probabilities.

## Installation

You can install `pseudostate` directly from PyPI:

```bash
pip install pseudostate
```

## Usage

The primary function in this library is `calculate_pseudostates`, which computes jackknife pseudo-observations for state occupation probabilities. Here is a basic example of how to use it:

```python
import polars as pl
from pseudostate import calculate_pseudostates

# Sample data with event times and states
# Each row corresponds to a single individual
times_and_reals = pl.DataFrame({
    "time": [10, 20, 30, 40, 50],
    "state": [1, 2, 1, 3, 2],
})

# Define a fixed time horizon
fixed_time_horizon = 35

# Calculate pseudo-observations
pseudo_observations = calculate_pseudostates(
    times_and_reals,
    fixed_time_horizon,
)

print(pseudo_observations)
```

## Contributing

Contributions are welcome! Please see the `AGENTS.md` file for guidelines on how to contribute to this project.

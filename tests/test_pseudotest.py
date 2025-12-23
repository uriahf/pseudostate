import polars as pl
from pseudostate import calculate_pseudostates


def test_calculate_pseudostates():
    """Test the calculate_pseudostates function with a simple case."""
    # Sample data with event times and states
    times_and_reals = pl.DataFrame(
        {
            "times": [10, 20, 30, 40, 50],
            "reals": [1, 2, 1, 3, 2],
        }
    )

    # Define a fixed time horizon
    fixed_time_horizon = 35

    # Calculate pseudo-observations
    pseudo_observations = calculate_pseudostates(
        times_and_reals,
        fixed_time_horizon,
    )

    # Check that the output has the correct shape and columns
    assert pseudo_observations.shape[0] == 5
    expected_cols = [
        "estimate_origin",
        "times",
        "state_occupancy_probability_0",
        "state_occupancy_probability_1",
        "state_occupancy_probability_2",
        "row_id",
    ]
    assert all(col in pseudo_observations.columns for col in expected_cols)

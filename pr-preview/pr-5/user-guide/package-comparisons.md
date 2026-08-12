# Package comparisons

`pseudostate` follows the same pseudo-observation idea used by established R packages, but provides a focused, Polars-native Python interface. The packages below overlap, but they are not interchangeable in every analysis.


# At a glance

|  | `pseudostate` | R `pseudo` | R `survival::pseudo()` |
|----|----|----|----|
| Main interface | Polars DataFrame | R vectors | A fitted `survfit` object |
| Calculation | Delete-one jackknife | Delete-one jackknife | Infinitesimal jackknife |
| State probabilities | Yes | CIFs by cause; survival separately | Yes |
| Horizons per call | One fixed horizon | One or more | One or more |
| Other estimands | No | Restricted mean and years lost | Cumulative hazard and sojourn time |
| Natural fit | Focused Python/Polars workflow | Established R pseudo-observation workflow | Fast integration with R `survival` |

> **Note: Exact and infinitesimal-jackknife values**
>
> `pseudostate` and R's `pseudo` package construct ordinary delete-one jackknife pseudo-observations. `survival::pseudo()` uses an infinitesimal-jackknife approximation. Its documentation notes that the two are nearly identical for moderate to large samples, but they need not be exactly equal in a small example.


# The same competing-risk data

The tabs below express the same task: calculate subject-level pseudo-observations for state probabilities at time 5.


- <a href="" id="tabset-1-1-tab" class="nav-link active" data-bs-toggle="tab" data-bs-target="#tabset-1-1" role="tab" aria-controls="tabset-1-1" aria-selected="true">pseudostate (Python 🐍)</a>
- <a href="" id="tabset-1-2-tab" class="nav-link" data-bs-toggle="tab" data-bs-target="#tabset-1-2" role="tab" aria-controls="tabset-1-2" aria-selected="false">pseudo (R 🔵)</a>
- <a href="" id="tabset-1-3-tab" class="nav-link" data-bs-toggle="tab" data-bs-target="#tabset-1-3" role="tab" aria-controls="tabset-1-3" aria-selected="false">survival (R 🔵)</a>


``` python
import polars as pl
from pseudostate import calculate_pseudostates

observations = pl.DataFrame(
    {
        "times": [1, 2, 2, 3, 4, 5, 6],
        "reals": [1, 0, 2, 1, 0, 2, 1],
    }
)

calculate_pseudostates(
    observations,
    fixed_time_horizon=5,
)
```

The result is a Polars DataFrame with one row per observation and a pseudo-observation for every state.


``` r
library(pseudo)

time <- c(1, 2, 2, 3, 4, 5, 6)
event <- c(1, 0, 2, 1, 0, 2, 1)

values <- pseudoci(
  time = time,
  event = event,
  tmax = 5
)

values$pseudo
```

`pseudoci()` returns a list of matrices indexed by event cause. For ordinary survival pseudo-observations, the package instead provides `pseudosurv()`.


``` r
library(survival)

observations <- data.frame(
  time = c(1, 2, 2, 3, 4, 5, 6),
  event = factor(
    c(1, 0, 2, 1, 0, 2, 1),
    levels = c(0, 1, 2),
    labels = c("censor", "event", "competing")
  )
)

fit <- survfit(
  Surv(time, event) ~ 1,
  data = observations
)

pseudo(
  fit,
  times = 5,
  type = "pstate",
  data.frame = TRUE
)
```

This route first creates an Aalen-Johansen `survfit` object and then derives infinitesimal-jackknife pseudo-values from it.


# Which should you use?

Use `pseudostate` when the surrounding workflow is Python and Polars and you need transparent state-probability pseudo-observations at a fixed horizon. Use R's `pseudo` when you need its broader set of pseudo-observation estimands or several horizons in one call. Use `survival::pseudo()` when the analysis already uses `survfit`, or when its fast infinitesimal-jackknife calculation and richer multi-state infrastructure are useful.


# References

- [R `pseudo` package manual](https://cran.r-project.org/package=pseudo)
- [R `survival::pseudo()` documentation](https://rdrr.io/cran/survival/man/pseudo.html)

### Schedule

**9:00 am**: :coffee: :coffee: :coffee:

**9:15 am**: [Pair Problem](pair.md)

**10:00 am**: Null Hypothesis!

**11:00 am**: Minimum Viable Products! [Just do it!](https://www.youtube.com/watch?v=UhRXn2NRiWI)

 * [How to](mvp_instructions.md) make an MVP, right now, before lunch.
 * [Example](mvp_example.md) MVP.

**12:00 pm**: Lunch of champions.

**1:30 pm**: Investigation Presentation

**1:45 pm**: Make Products even more viable.


#### Some example code to plot Q-Q plots

(For example, to inspect the normality of residuals.)

```Python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

measurements = np.random.normal(loc = 20, scale = 5, size=100)
stats.probplot(measurements, dist="norm", plot=plt)
plt.show()
```

### Additional Resources

 * [More on hypothesis testing](https://dataiap.github.io/dataiap/day3/hypothesis_testing.html)
 * [Scipy has functions for many hypothesis tests](http://docs.scipy.org/doc/scipy/reference/stats.html#statistical-functions)
 * [Which statistical to use](http://www.ats.ucla.edu/stat/stata/whatstat/whatstat.htm)

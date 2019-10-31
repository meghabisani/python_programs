Calculate Population!!
----------------------------------------------------------------
Print all the years in which population was lower then preceding year


Introduction
----------------------------------------------------------------

Members of a population are represented as a collection of lifespans. Each lifespan represents a year of birth and, if the individual has died, a year of death. For example:

Born     Died
1902     1991
1941     1978
2004
1957
1989     2008
1909     2005
1918
1913     2010
1979
1961     2002
1977     2003
1909     1991

Program will take the above information and returns every year in which the population was lower than the preceding year.

For the example, a correct implementation will return the following years: 1992, 2003, 2006, 2009, 2011.

Notes:
 
1) If a member of the population was born in a given year, they count towards the population for that year.
2) Likewise, if a member of the population died in a given year, they count towards the population for that year.


Execution
----------------------------------------------------------------
To run the game:
python calculate_population.py
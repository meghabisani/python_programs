# Python version : 3.X
from collections import OrderedDict

# This function takes population in a type string as a input and then convert into list of list format
# then after computation returns every year in which the population was lower than the preceding year


def calculate_population(population):

    result, birth_list, death_list = [], [], []
    members = [line.strip().split() for line in population.split('\n') if line.strip() != '']

    for lifespan in members[1:]:

        if len(lifespan) == 2:

                if int(lifespan[0]) == int(lifespan[1]):
                    members.remove(lifespan)

                else:
                    death_list.append(int(lifespan[1]))
                    birth_list.append(int(lifespan[0]))

        else:
            birth_list.append(int(lifespan[0]))

    for year in death_list:

        if death_list.count(year) > (birth_list.count(year) + birth_list.count(year + 1)):
            result.append(year + 1)

    return list(OrderedDict.fromkeys(result))


# Input Format for calculate_population: Input String must have only two columns,
# first row contains the column names, next all the rows represent the lifespan,
# born and death year should be separated by space and each contains 4 digit integer


resultant_years = calculate_population('''
    Born Death
    1902 1991
    1941 1978
    2004
    1957
    1989 2008
    1909 2005
    1918
    1913 2010
    1979
    1961 2002
    1977 2003
    1909 1991
    ''')


print(*resultant_years, sep=', ')

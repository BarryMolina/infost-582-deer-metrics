import pandas

metrics = pandas.read_csv('deer_metrics_by_county.csv', delimiter='|')
pop = pandas.read_csv('deer_population_by_county_2023.csv', delimiter='|')

joined = metrics.set_index('county').join(pop.set_index('County'), how='outer')
joined.to_csv('deer_metrics_with_population.csv')
import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency


# 1 - load and inspect species dataframe
species = pd.read_csv('species_info.csv')
print(species.head())
# This dataframe has information on the conservation status of a variety of species categorized by broad species type. The data is text - conservation_status allows for null values (representing species not in danger of extinction).


# 2 - inpsect species dataframe
species_count = species.scientific_name.nunique()
species_type = species.category.unique()
conservation_statuses = species.conservation_status.unique()
print species_count
print species_type
print conservation_statuses


# 3 - analyze conservation status
conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts


# 4 - analyze conservation status ii
species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts_fixed


# 5 - plot bar chart of conservation status
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

print species.head()
print protection_counts.head()
    
plt.figure(figsize=(10,4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)), protection_counts.scientific_name)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()
plt.savefig('conservation_by_species.png')


# 6 - pivot endangered species data
species['is_protected'] = species.conservation_status != 'No Intervention'

category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()

print category_counts.head()

category_pivot = category_counts.pivot(
		columns='is_protected',
		index='category',
		values='scientific_name').reset_index()

print category_pivot


# 7 - further pivot manipulation
category_pivot.columns = ['category', 'not_protected', 'protected']

category_pivot['percent_protected'] = (category_pivot['protected'] / (category_pivot['protected'] + category_pivot['not_protected']))

print category_pivot


# 8 - chi-squared testing for all category pairs

# Bird vs Amphibian
contingency_3 = [[75, 413], 
                [7, 72]]

chi2, pval_amphib_bird, dof, expected = chi2_contingency(contingency_3)
print pval_amphib_bird

# Fish vs Amphibian
contingency_4 = [[11, 115], 
                [7, 72]]

chi2, pval_amphib_fish, dof, expected = chi2_contingency(contingency_4)
print pval_amphib_fish

# Mammals vs Amphibian
contingency_5 = [[30, 146], 
                [7, 72]]

chi2, pval_amphib_mammal, dof, expected = chi2_contingency(contingency_5)
print pval_amphib_mammal

# Nonvas vs Amphibian
contingency_6 = [[5, 328], 
                [7, 72]]

chi2, pval_amphib_nonvas, dof, expected = chi2_contingency(contingency_6)
print pval_amphib_nonvas

# Reptiles vs Amphibian
contingency_7 = [[5, 73], 
                [7, 72]]

chi2, pval_amphib_reptile, dof, expected = chi2_contingency(contingency_7)
print pval_amphib_reptile

# Plant vs Amphibian
contingency_8 = [[46, 4216], 
                [7, 72]]

chi2, pval_amphib_plant, dof, expected = chi2_contingency(contingency_8)
print pval_amphib_plant

# Fish vs Birds
contingency_9 = [[11, 115], 
               [75, 413]]

chi2, pval_bird_fish, dof, expected = chi2_contingency(contingency_9)
print pval_bird_fish

# Mammals vs Birds
contingency = [[30, 146], 
               [75, 413]]

chi2, pval, dof, expected = chi2_contingency(contingency)
print pval

# Nobvas vs Birds
contingency_10 = [[5, 328], 
               [75, 413]]

chi2, pval_bird_nonvas, dof, expected = chi2_contingency(contingency_10)
print pval_bird_nonvas

# Reptile vs Birds
contingency_11 = [[5, 73], 
               [75, 413]]

chi2, pval_bird_reptile, dof, expected = chi2_contingency(contingency_11)
print pval_bird_reptile

# Plants vs Birds
contingency_12 = [[46, 4216], 
               [75, 413]]

chi2, pval_bird_plant, dof, expected = chi2_contingency(contingency_12)
print pval_bird_plant

# Mammals vs Fish
contingency_13 = [[30, 146], 
                [5, 73]]

chi2, pval_reptile_mammal, dof, expected = chi2_contingency(contingency_13)
print pval_reptile_mammal

# Fish vs Nonvas
contingency_14 = [[11, 115], 
                [5, 328]]

chi2, pval_nonvas_fish, dof, expected = chi2_contingency(contingency_14)
print pval_nonvas_fish

# Fish vs Reptile
contingency_15 = [[11, 115], 
                [5, 73]]

chi2, pval_reptile_fish, dof, expected = chi2_contingency(contingency_15)
print pval_reptile_fish

# Fish vs Plant
contingency_16 = [[11, 115], 
                [46, 4216]]

chi2, pval_plant_fish, dof, expected = chi2_contingency(contingency_16)
print pval_plant_fish

# Mammals vs Nonvas
contingency_17 = [[30, 146], 
                [5, 328]]

chi2, pval_nonvas_mammal, dof, expected = chi2_contingency(contingency_17)
print pval_nonvas_mammal

# Mammals vs Reptiles
contingency_2 = [[30, 146], 
                [5, 73]]

chi2, pval_reptile_mammal, dof, expected = chi2_contingency(contingency_2)
print pval_reptile_mammal

# Mammals vs Plant
contingency_18 = [[30, 146], 
                [46, 4216]]

chi2, pval_plant_mammal, dof, expected = chi2_contingency(contingency_18)
print pval_plant_mammal

# Nonvas vs Reptile
contingency_19 = [[5, 328], 
                [5, 73]]

chi2, pval_reptile_nonvas, dof, expected = chi2_contingency(contingency_19)
print pval_reptile_nonvas

# Nonvas vs Plant
contingency_20 = [[5, 328], 
                [46, 4216]]

chi2, pval_plant_nonvas, dof, expected = chi2_contingency(contingency_20)
print pval_plant_nonvas

# Reptile vs Plant
contingency_21 = [[5, 73], 
                [46, 4216]]

chi2, pval_plant_reptile, dof, expected = chi2_contingency(contingency_21)
print pval_plant_reptile

# ----- End Endangered Species Analysis -----

import codecademylib
import pandas as pd
from matplotlib import pyplot as plt


# code to load and tidy species_info dataframe
species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'


# 10 - load observations datatframe
observations = pd.read_csv('observations.csv')
print observations.head()


# 11 - isolate instances of sheep in dataframe
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)

species_is_sheep = species[species.is_sheep]
print species_is_sheep

sheep_species = species[species.is_sheep & (species.category == 'Mammal')]
print sheep_species


# 12 - merge observation and sheep_species data for analysis
sheep_observations = pd.merge(observations, sheep_species)
print sheep_observations.head()


# 13 - plot sheep sightings by park
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),
        obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()
plt.savefig('observations_by_park.png')


# 14 - sample size determination
baseline = 0.15
minimum_detectable_effect = (100 * 0.05) / 0.15
sample_size_per_variant = 510
yellowstone_weeks_observing = sample_size_per_variant / float(507)
bryce_weeks_observing = sample_size_per_variant / float(250)

print baseline
print minimum_detectable_effect
print sample_size_per_variant
print yellowstone_weeks_observing
print bryce_weeks_observing
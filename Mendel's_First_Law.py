in_data = input("Give your 3 numbers (positive integers): ")
species_1 = in_data.split()[0]
species_2 = in_data.split()[1]
species_3 = in_data.split()[2]

dominant_allele = (int(species_1) * 2) + int(species_2)
recessive_allele = int(species_2) + (int(species_3) * 2)

dominant_phenotype_probability = (dominant_allele/(dominant_allele + recessive_allele))*((dominant_allele - 1)/(dominant_allele + recessive_allele - 1)) + (dominant_allele/(dominant_allele + recessive_allele))*(recessive_allele/(dominant_allele + recessive_allele - 1)) + (recessive_allele/(dominant_allele + recessive_allele))*(dominant_allele/(dominant_allele + recessive_allele - 1))
print(dominant_phenotype_probability)

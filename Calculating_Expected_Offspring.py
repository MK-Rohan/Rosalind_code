genotype = input("Give your dataset: ").split()

one = float(genotype[0])
two = float(genotype[1])
three = float(genotype[2])
four = float(genotype[3])
five = float(genotype[4])
six = float(genotype[5])

# 커플 수 * 자손 수(2 고정) * dominant 자손 확률
dominant_phenotype = (
    one * 2 * 1
    + two * 2 * 1
    + three * 2 * 1
    + four * 2 * 0.75
    + five * 2 * 0.5
    + six * 2 * 0
)

print(dominant_phenotype)

in_data = """GCGCGCCCCTGGCGCCTGGCGAGTGGCCTGGCGACATCTAGCCTGGCGCGACCTGGCGAAGCCCTGGCGCCGAACCTGGCGCCACACCTGGCGTGCCTGGCGCCTGGCGGGGCCTGGCGCTCCTGGCGCCCTGGCGTGCACCACGCCTGGCGCCTGGCGGCCTGGCGTCCTGGCGCCTGGCGCCTGGCGTTTCCTGGCGTTTGCAATCCTGGCGTGACCTGGCGCCGCCTGGCGCCTGGCGTCCTGGCGCCTGGCGGCCTGGCGCCTGGCGCTTCCTGGCGTCCTGGCGTCCTGGCGAGGCCTGGCGCCTGGCGCCCTGGCGTGCTCCTGGCGCCTGGCGCCTGGCGCGCCTGGCGGCCTGGCGTTACCTGGCGAGTTCCTGGCGGCCTGGCGCCCTGGCGACCCTGGCGCCTGGCGCCTGGCGCCCCTGGCGCCCTGGCGCCCTGGCGATTTCCTGGCGATCCCTGGCGATGTGCCTGGCGGAACCCTGGCGCCCTGGCGTCCTGGCGTCCTGGCGCGCCCTGGCGGGATGACCCTGGCGCCTGGCGGAAGAACTTCCAACCTGGCGCCTGGCGCCTGGCGGATGCCCTGGCGACCCCTGGCGCTTTCACTGCCTGGCGGTTTCGCCTGGCGTGGGACCTGGCGCGGCCTGGCGACCTGGCGTCTTGCCTGGCGCCTGGCGATCCGCCTGGCGCCTGGCGTATCCTGGCGAACTCCTGGCGCTCCGCTAGAAGGAAGCCTGGCGCACGTAGCCTGGCGACCTGGCGCCTGGCGCACCCGCCTGGCGACCCTGGCGGCCTGGCGCCCCTGCCTGGCGCCAGCCTGGCGACCTGGCGATTCCATTCCTGGCGTCCACACTGCGTGCCTGGCGGCCTGGCGCTCATGCGACCACCTGGCGCCTGGCGCCTGGCGCCTGGCGTCCTGGCGTTCCTGGCGAACCTGGCGTTTGCCCTGGCGCCTCACCTGGCGCAAGGTTAG
CCTGGCGCC"""
s = in_data.split()[0]
t = in_data.split()[1]
indexing = list()

for line in range(0, len(s) - len(t) + 1):
    if t == s[line:line+len(t)]:
        indexing.append(line+1)
result = " ".join(map(str,indexing))

print(result)
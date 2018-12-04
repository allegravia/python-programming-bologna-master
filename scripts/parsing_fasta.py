# Manipulation of a FASTA file

fasta = open('multiple_seq.fasta')

for line in fasta:
    if line[0] == '>':
        col = line.split('|')
        if col[1] == 'P62258':
            print(line)

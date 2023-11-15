from enum import Enum, IntEnum
from typing import Tuple, List
"""

class N2(IntEnum): 
    'The line below the comment is equivalent to this class'.. The order of the tuple represents 
    the integer value that you see in this class' 
    A = 1
    C = 2
    G = 3
    T = 4

   """
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C','G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] #Codeon expects a Tuple of three nucleotides
Codon2 = Tuple[N2,N2,N2] #Codeon expects a Tuple of three nucleotides
Gene = List[Codon]# Gene expects a list of Codons 
Gene2 = List[Codon2]# Gene expects a list of Codons 

sample_gene = 'ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'

def string_to_gene(s: str) -> Gene: 
    gene: Gene = [] 
    for i in range(0, len(s), 3): 
        if (i+2) >= len(s): #Three nucleotides not available at end
            return gene
        #Create the Codon
        codon: Codon = ([ Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2] ]])
        gene.append(codon)
    return gene

print(string_to_gene(sample_gene), sep='\n')

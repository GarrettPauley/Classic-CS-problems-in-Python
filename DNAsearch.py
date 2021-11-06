import math
from enum import IntEnum
from typing import Tuple, List
"""A nucleotide is represented by one of the letters A, C, G and T. 
A codon is composed of three nucleotides, and a gene is composed of multiple codons""" 
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] #type aliases for Codons 
Gene = List[Codon] 
#A representatoin of the gene_str 
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

#Utility function to convert a str into a Gene

def string_to_gene(s: str) -> Gene: 
    gene: Gene = [] 
    for i in range(0, len(s), 3): 
        if (i + 2) >= len(s):#Dont run off the end of the gene
            return(gene) 
        #initialize codon out of three nucleotides 
        codon: Codon = (Nucleotide[s[i]],Nucleotide[s[i+1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene

my_gene = string_to_gene(gene_str)
print(my_gene)

#Linear search through the gene. Runs in Big O(n)
def linear_contains(gene: Gene, key_codon: Codon) -> bool: 
    for codon in gene: 
        if codon == key_codon: 
            return True 
        return False 
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G) 
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T) 
print(linear_contains(my_gene, gat))

#Binary search through the gene
"""A binary search by working through a sorted list, looking at the middle of the list, 
comparing it to the target. If the middle element is larger than the target... 
we can set the max as the middle value. and repeat the process. 
Consider the following list: [1,2,3,4,5,6,7,8,9,10], and a target value of 4. 
we can start at the midpoint of the list (5), comparing it to the value. Since the 
halfway point is > target value we can set 5 as the new starting point, that is, 
the value that we will halve next.
#Binary search has a worst-case runtime of Big O(log n) """ 

def binary_contains(gene: Gene, key_codon: Codon) -> bool: 
    low = int = 0 
    high: int = len(gene) - 1 
    while low <= high: #While there is still a serach space 
        mid: int = (low + high) // 2

        if gene[mid] < key_codon: 
            low = mid + 1
        elif gene[mid] > key_codon: 
            high = mid - 1 
        else: 
            return True
    return False

sorted_gene = sorted(my_gene)
print(binary_contains(sorted_gene, acg))
print(binary_contains(sorted_gene, gat))

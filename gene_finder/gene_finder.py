# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Tom Heale

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('5')
    ' -Invalid- '
    """

    # Why not test every option? THere are only 5
    #Also, ordering a lizard will not break this function (it's -Invalid- )

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'C':
        return 'G'    
    return ' -Invalid- '

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """

    # There aren't a lot of tricky permutations to input for this function
    # The -Invalid- thing still works, though :)

    length = len(dna)
    inv_comp = ''
    i = 1
    while i <= length:
        index = length - i
        nucleotide = dna[index]
        inv_comp = inv_comp + get_complement(nucleotide)
        i = i + 1
    return inv_comp

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    ['ATG', 6]
    >>> rest_of_ORF("ATGAGATAGG")
    ['ATGAGA', 9]
    >>> rest_of_ORF("ATGAGCTCAA")
    ['ATGAGCTCAA', 10]
    >>> rest_of_ORF("TAG")
    ['', 3]
    """
    # The provided tests all contained stop codons
    # I want to see what it does without a start codon

    stop1 = 'TAG'
    stop2 = 'TAA'
    stop3 = 'TGA'
    i = 0
    length = len(dna)
    tRNA = ''
    while i + 3 <= length:
        codon = dna[i:i+3]
        if codon == stop1 or codon == stop2 or codon == stop3:
            return [tRNA, i + 3]
        tRNA = tRNA + codon
        i = i+3
    return [dna, length]

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """

    # Again, not lots of tricky permutations

    i = 0
    length = len(dna)
    start = 'ATG'
    ORFs = []
    while i + 3 <= length:
        codon = dna[i:i+3]
        if codon == start:
            testDNA = dna[i:length]
            data = rest_of_ORF(testDNA) 
            ORFs.append(data[0])
            i = i + data[1]
        else:
            i = i + 3
    return ORFs


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """

    # It's hard for find_all_ORFs_oneframe to work and not have this function work, too
    # I'm comfortable with the one doctest

    firstFrame = find_all_ORFs_oneframe(dna)
    secondFrame = find_all_ORFs_oneframe(dna[1:])
    thirdFrame = find_all_ORFs_oneframe(dna[2:])
    allFrames = firstFrame + secondFrame + thirdFrame
    return allFrames

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    # This test has an open frame on both strands

    forward = find_all_ORFs(dna)
    backward = find_all_ORFs(get_reverse_complement(dna))
    ORFs = forward + backward
    return ORFs

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("ATGCGAATATGGTAAGGATCCCATCATAGATCAAA")
    'ATGATGGGATCCTTACCATATTCGCAT'
    >>> longest_ORF('')
    ''
    """

    # Base case of empty string
    # My antigen string returns lots o' ORFs
    
    allORFs = find_all_ORFs_both_strands(dna)
    if len(allORFs) > 0:
        return max(allORFs, key = len)
    else:
        return ''

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    
# I tested this function manually by inputting random strings of antigens and gradually increasing the number of trials. At trial number > 1000, the output is VERY consistent

    longest = ''
    for i in range(num_trials):
        stringer = shuffle_string(dna)
        orf = longest_ORF(stringer)
        if len(orf) > len(longest):
            longest = orf
    return len(longest)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents a protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """

    # More test cases would really just test the dictionary, wich I don't plan to do
    
    lastSlice = len(dna)-3
    protein = ''
    i = 0
    while i <= lastSlice:
        codon = dna[i:i+3]
        amino_acid = aa_table[codon]
        protein = protein + amino_acid
        i = i + 3
    return protein

def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # I don't know how I could write a doctest for this
    # But good news, it seems like it works!

    threshold = longest_ORF_noncoding(dna,1500)
    orfs = find_all_ORFs_both_strands(dna)
    allProteins = []
    for frame in orfs:
        if len(frame) > threshold:
            protein = coding_strand_to_AA(frame)
            allProteins.append(protein)
    for i in range(len(allProteins)):
        print allProteins[i]
    return allProteins

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    dna = load_seq("./data/X73525.fa")
    gene_finder(dna)
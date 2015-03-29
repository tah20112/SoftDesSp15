from collections import OrderedDict as odict

class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.nucleotides = nucleotides
 
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return str(self.nucleotides)

    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence
            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """
        rev_comp = ''
        for nucleotide in self.nucleotides[::-1]:
            if nucleotide == 'A':
                opp = 'T'
            if nucleotide == 'T':
                opp = 'A'
            if nucleotide == 'G':
                opp = 'C'
            if nucleotide == 'C':
                opp = 'G' 
            rev_comp += opp
        return DNASequence(rev_comp)

    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        a_count = self.nucleotides.count('A')
        a_prop = a_count/float(len(self.nucleotides))
        t_count = self.nucleotides.count('T')
        t_prop = t_count/float(len(self.nucleotides))
        c_count = self.nucleotides.count('C')
        c_prop = c_count/float(len(self.nucleotides))
        g_count = self.nucleotides.count('G')
        g_prop = g_count/float(len(self.nucleotides))

        keys = ['A','T','C','G']
        props = [a_prop,t_prop,c_prop,g_prop]
        return odict(zip(keys,props))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
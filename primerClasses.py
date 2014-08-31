class sequence(object):
    
    def __init__(self, seq):
        self.seq = seq
        
    def __str__(self):
        return "A DNA sequence of length %s: %s" % (self.length(), self.seq)
    
    def getSequence(self):
        return self.seq
        
    def length(self):
        return len(self.seq)
    
    def GC_content(self):
        seq = self.seq
        A = seq.count("A")
        G = seq.count("G")
        C = seq.count("C")
        T = seq.count("T")
        return (G+C)/(A+C+G+T)
    
class FusionSequence(sequence):
    """This objects contains the joint sequence of the fusion region reported by MSK-IMPACT (Delly)
    200bp from partnerA and 200bp from partnerB is combined and used to create the object"""
    
    def __init__(self, seq):
        self.seq = seq
    
    def getPartnerA(self):
        seq  = self.seq
        l = self.length()
        return seq[0:int(l/2)]
    
    def getPartnerB(self):
        seq  = self.seq
        l = self.length()
        return seq[int(l/2):]



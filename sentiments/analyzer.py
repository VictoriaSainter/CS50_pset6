import nltk



class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        
        self.positiveList = []
        self.negativeList = []
        
        with open(positives) as positivesFile:
            for _ in range(35):
                next(positivesFile)
            for line in positivesFile:
                cleanedLine = line.strip()
                if cleanedLine:
                    
                    self.positiveList.append(cleanedLine)
                    
                
                
        with open(negatives) as negativesFile:
            for _ in range(35):
                next(negativesFile)
            for line in negativesFile:
                cleanedLine = line.strip()
                if cleanedLine:
                    
                    self.negativeList.append(cleanedLine)

        positivesFile.close()
        negativesFile.close()
        
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        #print("text= {}".format(text))
        
        score = 0
        
        textList = text.split()
        
        
        for i in textList:
            i = i.lower()
            for positiveWord in self.positiveList:
                if i == positiveWord:
                    score += 1
        for i in textList:
            i = i.lower()
            for negativeWord in self.negativeList:
                if i == negativeWord:
                    score -= 1
        
                    
            
        
        # TODO
        return score
        

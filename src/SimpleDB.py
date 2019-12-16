

class SimpleDB:
    def __init__(self):
        f = open("rank.db","r")
        self.lst = f.readline().split()
        self.lst = [int(x) for x in self.lst]
        self.lst.sort(reverse=True)
        f.close()
    def addScore(self,score):
        self.lst.append(score)
        self.lst.sort(reverse=True)
        if(len(self.lst)>10):
            self.lst = self.lst[:10]
        f = open('rank.db','w')
        f.write(' '.join(str(x) for x in self.lst))
        f.close()
    def getScores(self):
        return self.lst[:]
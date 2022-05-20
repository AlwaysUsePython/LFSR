import time

class LFSRGenerator4:

    def __init__(self, seed='1001'):
        self.previous = seed
        self.current = ""

    def generate(self):
        self.current = ""
        self.current +=str((int(self.previous[-1]) + int(self.previous[-2]))%2)
        self.current += self.previous[0:3]
        self.previous = self.current
        print(self.current)
        return int(self.current[-1])

class LFSRGenerator16:
    def __init__(self, seed=""):
        if seed != "":
            self.previous = seed
        else:
            f = open('Seed', 'r')
            self.previous = f.read()
            f.close()
        self.seed = self.previous
        self.current = ""
        self.iterations = 0

    def generateBinary(self):
        self.current = ""
        self.current += str(((int(self.previous[-6])) + ((int(self.previous[-4]) +((int(self.previous[-1]) + int(self.previous[-3]))%2)) %2))%2)
        self.current += self.previous[0:15]
        self.previous = self.current
        self.iterations += 1
        return int(self.current[-1])

    def generateStupid(self, start, end):
        possibilities = []
        for num in range(start, end+1):
            possibilities.append(num)

        while len(possibilities) > 1:
            newPossibilities = []
            for num in possibilities:
                if self.generateBinary() == 1:
                    newPossibilities.append(num)
            if len(newPossibilities) != 0:
                possibilities = newPossibilities

        f = open('Seed', 'w')
        f.write(self.previous)
        f.close()

        return possibilities[0]

    def generateSmart(self, start, end):
        self.generateBinary()
        randChoice = (int(self.previous, 2)) % (start-end) + start

        f = open('Seed', 'w')
        f.write(self.previous)
        f.close()

        return randChoice

    def getOriginalSeed(self):
        return self.seed

    def getIterations(self):
        return self.iterations

rand = LFSRGenerator16()

distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

start = time.time()
for i in range(20000):
    distribution[rand.generateStupid(1, 6) + rand.generateStupid(1, 6)-2] += 1
end = time.time()

print("The dumb way took " + str(end-start) + " seconds")

start = time.time()
for i in range(20000):
    distribution[rand.generateSmart(1, 6) + rand.generateSmart(1, 6)-2] += 1
end = time.time()

print("The smart way took " + str(end-start) + " seconds")



print(distribution)
print(rand.getIterations())

"""distribution = [0, 0]
for i in range(100000):
    distribution[rand.generateBinary()] += 1"""

#print(distribution)

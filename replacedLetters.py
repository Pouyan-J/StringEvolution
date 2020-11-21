import datetime
import random
import string
import unittest
import genetic

class StringEvolutionTests(unittest.TestCase):
    geneset = string.ascii_lowercase

    def test_hello(self):
        target = "hello"
        print('\n----------------------------------------------------------------------')
        print('Running test case: \"' + target + '\":\n')
        self.string_evolution(target)

    def test_random(self):
        target = generate_random_string(50)
        print('\n----------------------------------------------------------------------')
        print('Running test case: \"' + target + '\":\n')
        self.string_evolution(target)

    def string_evolution(self, target):

        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return -1 * get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = 0
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(''.join(best.Genes), target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_random)


def get_fitness(input_string: str, target_string: str) -> int:
    sum = abs(len(input_string) - len(target_string))
    for i, j in zip(list(input_string), list(target_string)):
        sum += 0 if i == j else 1
    return sum

def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k = length)) 

def display(candidate, startTime):
    timeD = datetime.datetime.now() - startTime
    print("{0}\t...\t{1}".format(''.join(candidate.Genes), str(timeD)))

if __name__ == "__main__":
    unittest.main()
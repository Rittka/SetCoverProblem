import SCP
import random
import Chromosome
class Population:
      list_Chromosome = list()
      list_Gene = list()
      def __init__(self,numOfUni,numOfChromosomes, numOfSubSets,list_validChromosome):
          listofChromosome = self.list_Chromosome
          listOfGene = self.list_Gene
          self.numOfSubsets = numOfSubSets
          for i in range(numOfChromosomes):
             
          list_validChromosome = self.ValidChromosome(numOfUni,numOfChromosomes, numOfSubSets,listofChromosome)
          



      def ValidChromosome(self,numOfUni,numOfChromosomes, numOfSubSets,listOfChromosome):
          resault = list()
          
          scp = SCP.SCP(numOfUni,numOfSubSets)
          for i in range(numOfChromosomes):
              for j in range(numOfSubSets):
                  if (listOfChromosome[i][j] == 1):
                      resault = resault | scp.listOfSubsets[j]
              if (resault.__len__() != numOfUni):
                  invalidChromosome = listOfChromosome[i]

                  listOfChromosome.remove(invalidChromosome)
          return listOfChromosome

      def PrepareInvalidChromosome()

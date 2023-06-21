import PyPluMA
import PyIO

class CSV2LEfSePlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

        self.csvfile = open(PyPluMA.prefix()+"/"+self.parameters["csvfile"])
        self.metadata = open(PyPluMA.prefix()+"/"+self.parameters["metadata"])

    def run(self):
        self.metadata.readline()
        self.mapping = dict()
        for line in self.metadata:
            contents = line.strip().replace('\"', '').split(',')
            self.mapping[contents[0]] = contents[1]
    
    def output(self, outputfile):
        outfile = open(outputfile, 'w')

        firstline = self.csvfile.readline()
        contents = firstline.strip().replace('\"', '').split(',')
        contents[0] = 'sample_id'
        for i in range(len(contents)):
           outfile.write(contents[i])
           if (i != len(contents)-1):
               outfile.write('\t')
           else:
               outfile.write('\n')
        outfile.write('Group\t')
        for i in range(1, len(contents)):
           outfile.write(self.mapping[contents[i]])
           if (i != len(contents)-1):
               outfile.write('\t')
           else:
               outfile.write('\n')
        for line in self.csvfile:
           outfile.write(line.replace('\"', '').replace(',','\t'))

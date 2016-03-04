import commands
import argparse

class GetRecords:
    def __init__(self, query, path):
        self.query = str(query)
        self.path = str(path)

    def get_records(self):
        cmd = "cat " + self.path + " | grep " + self.query
        output = commands.getoutput(cmd).split("\n")
        for i in range(len(output)):
            output[i] = output[i].split(',')
        return output

if __name__ == "__main__":
    records = GetRecords("Hippocampal", "datasets/nature13186-s2.csv")
    print records.get_records()

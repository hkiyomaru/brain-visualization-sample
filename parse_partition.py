from get_records import GetRecords

class ParsePartition(GetRecords):
    def __init__(self, query, path):
        GetRecords.__init__(self, query, path)
        self.records = self.get_records()

    def parse_partition(self):
        partitions = []
        for r in self.records:
            partitions.append(r[2])
        return partitions

if __name__ == "__main__":
    parser = ParsePartition("Hippocampal", "datasets/nature13186-s2.csv")
    print parser.parse_partition()

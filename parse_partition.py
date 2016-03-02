from get_records import GetRecords 

class ParsePartition:
    def __init__(self):
        r = GetRecords()
        self.records = r.get_records()

    def parse_partition(self):
        partitions = []
        for r in self.records:
            partitions.append(r[2])
        return partitions

if __name__ == "__main__":
    parser = ParsePartition()
    print parser.parse_partition()

from mrjob.job import MRJob

class OrderCount(MRJob):

    def mapper(self, _, line):
        if "order_id" in line:
            return
        yield "Total Orders", 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    OrderCount.run()
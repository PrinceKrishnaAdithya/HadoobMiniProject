from mrjob.job import MRJob

class TopProducts(MRJob):

    def mapper(self, _, line):
        if "order_id" in line:
            return
        data = line.split(",")
        product = data[1]
        revenue = float(data[3]) * int(data[4])
        yield product, revenue

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    TopProducts.run()
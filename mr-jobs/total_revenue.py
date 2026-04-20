from mrjob.job import MRJob

class TotalRevenue(MRJob):

    def mapper(self, _, line):
        if "order_id" in line:
            return
        data = line.split(",")
        revenue = float(data[3]) * int(data[4])
        yield "Total Revenue", revenue

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    TotalRevenue.run()
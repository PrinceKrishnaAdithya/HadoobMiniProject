from mrjob.job import MRJob

class SalesByCategory(MRJob):

    def mapper(self, _, line):
        if "order_id" in line:
            return
        data = line.split(",")
        category = data[2]
        revenue = float(data[3]) * int(data[4])
        yield category, revenue

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    SalesByCategory.run()
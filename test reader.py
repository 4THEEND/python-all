import csv

def csv_reader(ind, file):
    search = csv.DictReader(open(file, 'r'))
    s = [dict(l) for l in search]
    return s[0].get(ind)

print(csv_reader("Moyenne", "csv/G G.csv"))

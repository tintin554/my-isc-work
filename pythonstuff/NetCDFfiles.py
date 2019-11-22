#Writing and plotting to NetCDF files exercise (starting from 7)

from datetime import datetime
from csv import reader

def convert_time(tm) :
    tm = datetime.strptime(tm, "Y-%m-%dT%H:%M:%S.%f")
    return tm

def convet_temp(temp)
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

infile = 'sample-serial-temperature-2h.tsv'
outfile = 'sensor-data.nc'

times = []
temps = [] #2 empty lists

#open infile and read into lists

with open(infile, 'rt') as tsvfile :
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader :
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))


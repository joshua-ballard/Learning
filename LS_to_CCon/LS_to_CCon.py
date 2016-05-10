#Convert LakeShore *.curve files into CryoCon *.crv files

import csv

def find_serial(filename):
  return filename[:-4]

headerlines = [['ACR'], ['-1.0'], ['ohms']]
temperature = []
resistance = []

readfile = 'x100335.dat'

with open(readfile, 'r') as csvfile:
  serial_number = [find_serial(readfile)]
  curvereader = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
  for rownum, row in enumerate(curvereader):
    if rownum > 2:
      temperature.append(row[0])
      resistance.append(row[1])

  outfile = 'x100335.crv'

  with open(outfile, 'w') as outfilehandle:
    curvewriter = csv.writer(outfilehandle, delimiter=' ', lineterminator='\n')
    curvewriter.writerow(serial_number)
    for line in headerlines:
      curvewriter.writerow(line)
    for i, temp in enumerate(temperature):
      datapoint = [resistance[i], temperature[i]]
      curvewriter.writerow(datapoint)

    curvewriter.writerow([';'])

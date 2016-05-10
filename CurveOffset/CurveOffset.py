# Convert LakeShore Cernox *.curve files into CryoCon *.crv files

import argparse
import csv
import sys

def main(readfile, offset):
  writefile = readfile[:-4] + 'plus' + str(offset) + '.crv'

  # file reads & writes
  with open(readfile, 'r') as infilehandle, open(writefile, 'w') as outfilehandle:
    curvereader = csv.reader(infilehandle, delimiter=' ', skipinitialspace=True)
    curvewriter = csv.writer(outfilehandle, delimiter='\t', lineterminator='\n')

    for rownum, row in enumerate(curvereader):
        if rownum < 5:
            curvewriter.writerow([row[0]])
        elif rownum >= 5 and rownum < 60:
            curvewriter.writerow([str(float(row[1]) + offset), row[0]])
    # standard .crv file ends with semicolon
    curvewriter.writerow([';'])


if __name__ == '__main__':
  # deal with input arguments
  parser = argparse.ArgumentParser(description='Convert LS .dat to Cryocon .crv')
  parser.add_argument('-i', '--input', help='Input file name', required=True)
  parser.add_argument('-O', '--offset', help='Offset value (ohms)', required=True)
  args = parser.parse_args()

  readfile = args.input
  offset = args.offset

  sys.exit(main(readfile, offset))

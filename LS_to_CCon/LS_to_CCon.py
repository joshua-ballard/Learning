# Convert LakeShore Cernox *.curve files into CryoCon *.crv files

import argparse
import csv
import sys

def main(readfile):
  writefile = readfile[:-4] + '.crv'
  # build the header (fixed by CryoCon for Cernox sensors)
  headerlines = [['ACR'], ['-1.0'], ['ohms']]

  # file reads & writes
  with open(readfile, 'r') as infilehandle, open(writefile, 'w') as outfilehandle:
    curvereader = csv.reader(infilehandle, delimiter=' ', skipinitialspace=True)
    curvewriter = csv.writer(outfilehandle, delimiter='\t', lineterminator='\n')

    # set up and write the header
    curvewriter.writerow([readfile[:-4]])
    for line in headerlines:
      curvewriter.writerow(line)

    for rownum, row in enumerate(curvereader):
      if rownum > 2:
        curvewriter.writerow([row[1], row[0]])
    # standard .crv file ends with semicolon
    curvewriter.writerow([';'])


if __name__ == '__main__':
  # deal with input arguments
  parser = argparse.ArgumentParser(description='Convert LS .dat to Cryocon .crv')
  parser.add_argument('-i', '--input', help='Input file name', required=True)
  args = parser.parse_args()

  readfile = args.input
  sys.exit(main(readfile))

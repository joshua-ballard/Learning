# Convert LakeShore Cernox *.curve files into CryoCon *.crv files

import argparse
import csv
import sys

def main(readfile, offset):
  writefile = readfile[:-4] + 'plus' + offset + '.crv'
  offset = float(offset)

  # file reads & writes
  with open(readfile, 'r') as infile, open(writefile, 'w') as outfile:

    for linenum, line in enumerate(infile.readlines()):
        if linenum == 0:
            firstline = line[:-1] + ' offset\n'
            outfile.write(firstline)
        elif linenum < 4:
            outfile.write(line)
        else:
            row = line.split( )
            if len(row) < 2:
                outfile.write(row[0])
            else:
                row[0] = str(float(row[0]) + offset)
                outfile.write('\t'.join(row) + '\n')

if __name__ == '__main__':
  # deal with input arguments
  parser = argparse.ArgumentParser(description='Convert LS .dat to Cryocon .crv')
  parser.add_argument('-i', '--input', help='Input file name', required=True)
  parser.add_argument('-O', '--offset', help='Offset value (ohms)', required=True)
  args = parser.parse_args()

  readfile = args.input
  offset = args.offset

  sys.exit(main(readfile, offset))

import re
import os
import csv

def find_Serial(content):
    for line in content:
        match = re.findall('\d{6}', line)
        if len(match) > 0:
            serial_number = match[0]
            return serial_number

def grab_cal_data(lines):
    data = []
    for i in range(10, 16, 1):
        line = lines[i].split(',')
        data.append(float(line[1]))
    return data

csv_files = []
serial_numbers = []
cal_data_list = []

for subdir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.csv'):
            filename = os.path.join(subdir, file)
            with open(filename, 'r') as base_file:
                file_lines = base_file.readlines()
                # print "processing %s" % filename
                sn = find_Serial(file_lines)
                cal_data = grab_cal_data(file_lines)
            if sn not in serial_numbers:
                serial_numbers.append(sn)
                csv_files.append(filename)
                cal_data_list.append(cal_data)

for i, datapoint in enumerate(cal_data_list):
    datapoint.insert(0, serial_numbers[i])

print len(serial_numbers), " unique sensor calibrations.\n"

outfile = 'LC_Futek_Cals.txt'

with open(outfile, 'w') as filehandle:
    csvWriter = csv.writer(filehandle, delimiter='\t', lineterminator='\n')
    for index in range(7):
        csv_row = []
        for datapoint in cal_data_list:
            csv_row.append(datapoint[index])
        #print csv_row
        csvWriter.writerow(csv_row)

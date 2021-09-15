
import csv

fileName = 'Road_Crashes_for_five_Years_-_Victoria.csv'
rows = [[],[], [], []]

year = [0] * 7
with open(fileName, 'r') as input:
    with open('surburb_count.csv', 'w', newline='') as output:
        with open('crashes_no_nulls.csv', 'w', newline='') as output2:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, ['LGA', 'Accidents', 'Longitude', 'Latitude'])
            writer2 = csv.DictWriter(output2, reader.fieldnames)
            writer2.writeheader()
            writer.writeheader()
            for row in reader:
                if row['LONGITUDE'] != '-1' and row['LONGITUDE'] != 'null' and row['LONGITUDE'] != '' and not ',' in row['LGA_NAME_ALL'] and '2014' not in row['ACCIDENT_DATE'] and '2019' not in row['ACCIDENT_DATE']:
                    writer2.writerow(row)
                    if row['LGA_NAME_ALL'] in rows[0]:
                        lgaIdx = rows[0].index(row['LGA_NAME_ALL'])
                        rows[1][lgaIdx] += 1
                        rows[2][lgaIdx] = (rows[2][lgaIdx] * rows[1][lgaIdx] + float(row['LONGITUDE']))/(rows[1][lgaIdx] + 1)
                        rows[3][lgaIdx] = (rows[3][lgaIdx] * rows[1][lgaIdx] + float(row['LATITUDE']))/(rows[1][lgaIdx] + 1)
                    else:
                        rows[0].append(row['LGA_NAME_ALL'])
                        rows[1].append(1)
                        rows[2].append(float(row['LONGITUDE']))
                        rows[3].append(float(row['LATITUDE']))
                if '2021' in row['ACCIDENT_DATE']:
                    year[0] += 1
                elif '2020' in row['ACCIDENT_DATE']:
                    year[1] += 1
                elif '2019' in row['ACCIDENT_DATE']:
                    year[2] += 1
                elif '2018' in row['ACCIDENT_DATE']:
                    year[3] += 1
                elif '2017' in row['ACCIDENT_DATE']:
                    year[4] += 1
                elif '2016' in row['ACCIDENT_DATE']:
                    year[5] += 1
                elif '2015' in row['ACCIDENT_DATE']:
                    year[6] += 1
            print(year)
            for idx, LGA in enumerate(rows[0]):
                writer.writerow({'LGA': LGA, 'Accidents': rows[1][idx], 'Longitude': rows[2][idx], 'Latitude': rows[3][idx]})

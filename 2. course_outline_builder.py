import csv

# use course outline builder Google spreadsheet to develop outline
# run course_outline_builder.py to read .csv to create outline text file
# copy and paste outline from text file to Google Doc to build course

filename = 'course_outline_builder.txt'

with open('course_outline_builder.csv') as f:
    reader = csv.reader(f)
    with open(filename, 'wt') as file_object:

        for row in reader:
            if row[0] == 'Course Outline Item':
                continue
            elif row[0] == '...':
                file_object.write(row[1] + '\n')
            elif row[0] == 'Course title':
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1].title() + '\n')
                file_object.write('' + '\n')
            elif row[0] == 'Course objectives':
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Duration':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Section title':
                file_object.write('\n\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Section body':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Steps':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Bullet points':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Example':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Illustration':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Vocabulary':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Tip':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'Bespoke content':
                file_object.write(',' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'TBD':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == '?':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            elif row[0] == 'n/a':
                file_object.write('' + '\n')
                file_object.write(row[0].upper() + '\n')
                file_object.write(row[1] + '\n')
            else:
                file_object.write(row[1] + '\n')

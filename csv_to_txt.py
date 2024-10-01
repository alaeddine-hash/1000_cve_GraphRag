import csv

def csv_to_txt(input_csv, output_txt):
    with open(input_csv, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(output_txt, 'w') as txt_file:
            for row in csv_reader:
                txt_file.write('\t'.join(row) + '\n')

input_csv = '1000CVE.csv'  # Replace with your input CSV file name
output_txt = '1000CVE.txt'  # Replace with your desired output TXT file name

csv_to_txt(input_csv, output_txt)
print(f"Converted {input_csv} to {output_txt}")

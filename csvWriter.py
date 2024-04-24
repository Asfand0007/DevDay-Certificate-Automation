import csv
import pandas as pd

def writeRecordsToCsv(records, logFilePath):
    # in case records are empty
    if not records:
        return False

    with open(logFilePath, mode="w", newline="") as csvFile:
        writer = csv.writer(csvFile, delimiter=",")

        # Write the fields, which are the keys of the dictionary
        fields = list(records[0].keys())
        writer.writerow(fields)

        totalRecords = len(records)

        for record in records:
            row = []
            for field in fields:
                row.append(record[field])

            writer.writerow(row)

    csvFile.close()
    return True

def readRecordsFromCsv(logFilePath):

    records = []

    try:
        with open(logFilePath, mode="r", newline="") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=",")

            lineCount = 0
            fields = []

            for row in csvReader:

                # If first row, initialize the dictionary keys as field values with arrays
                if lineCount == 0:
                    fields = row

                # For the next rows, write each row's field data to the respective array
                else:
                    fieldIndex = 0
                    memberData = {}
                    for field in fields:
                        memberData[field] = row[fieldIndex]
                        fieldIndex += 1
                    records.append(memberData)
                lineCount += 1
    except FileNotFoundError:
        pass

    return records


def readRecordsFromExcel(excelFilePath):
    records = []
    try:
        
        allSheetsDict = pd.read_excel(excelFilePath, sheet_name=None)
        dfs = []
        for sheetName, df in allSheetsDict.items():
            df['Team Name'] = sheetName
            dfs.append(df)

        combinedDF = pd.concat(dfs, ignore_index=True)

        records = combinedDF.to_dict('records')
    except FileNotFoundError:
        pass
    return records
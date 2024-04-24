from csvWriter import readRecordsFromCsv, writeRecordsToCsv

records= readRecordsFromCsv("csvfile.csv")
newRecords=[]
maxLength=0
for record in records:
    competition= record["Competition"]
    teamName= record["Team_Name"]
    if len(competition)>maxLength:
        maxLength=len(competition)

    newRecords.append({'Team Name':teamName,'Name':record["Leader_name"], 'Competition':competition})
    for i in range(1,5):
        if record[f'mem{i}_name']:
            newRecords.append({'Team Name':teamName, 'Name':record[f"mem{i}_name"], 'Competition':competition})
        

writeRecordsToCsv(newRecords,"participants.csv")
print(maxLength)
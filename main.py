from csvWriter import writeRecordsToCsv, readRecordsFromCsv, readRecordsFromExcel
from createCertificate import getCertificate
from sendLetterAttachedMail import sendPdfAttachmentMail
import easygui

def getHtmlContent(name):
    return f'''
        <html>
        <body style="padding: 0px; margin: 0px; justify-content: center; align-items: center; color: black;">
            <div style="display: block; width: 100%; justify-content: center; align-items: center; background-color: white;">
                <div style="padding: 25px 30px; border-style: solid; border-radius: 10px; border-width: 5px; border-color: lightblue; text-align: center; background-color: transparent;">
                    <img src="https://github.com/thenoisyninga/dev-day-attendence-admin-panel/blob/main/logo.png?raw=true" style="width: 400px; margin: -40px;">
                    
                    <div style="overflow-wrap: break-word;">
                        <p style="text-wrap: stable; text-align: left;">
                            Dear {name}, <br> <br>

                            We hope this email finds you well. We wanted to take a moment to express our gratitude and appreciation for your participation in e.ocean Developer's Day. It was an absolute pleasure to have you be a part of this event, and we're thrilled to have had the opportunity to share it with you.
                            <br>
                            As a token of our appreciation, we're delighted to present you with a participation certificate. This certificate serves as a testament to your enthusiasm and dedication to the world of tech and development.
                            <br>
                            Please find attached your personalized certificate, which includes your name and the event details. We hope you'll display it proudly as a reminder of your involvement in this exciting event.
                            <br>
                            Once again, thank you for being a part of e.ocean Developer's Day. We look forward to seeing you at future events and continuing to support your journey in the tech community.
                            <br>
                            <br> 
                            Best regards,<br>
                            E.ocean Developers' Day
                        </p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        '''


print("================================================")
print("         DEV DAY CERTIFICATE MANAGER")
print("================================================\n")

dataCsvPath= easygui.fileopenbox()
unsentMailsCsvPath = "unsentRecords.csv"
sentMailsCsvPath = "sentRecords.csv"
lengthIssueCsvPath= "lenghtIssueRecords.csv"

unsentRecords = readRecordsFromCsv(dataCsvPath)
sentRecords = readRecordsFromCsv(sentMailsCsvPath)
lengthIssueRecords = readRecordsFromCsv(lengthIssueCsvPath)


totalRecords = len(unsentRecords)
unsentLength = totalRecords
lengthIssueCount=0

try:

    i = 0

    while i < unsentLength:
        record = unsentRecords[i]
        name= record['Name']    
        name=name.lower().title()
        competition= record['Competition']

        if len(name)>22 or len(competition)>23:
            print(f"[-] Name/Competition name is too long: {name}")
            unsentRecords.remove(record)
            lengthIssueRecords.append(record)
            unsentLength -= 1
            i-=1
            lengthIssueCount+=1
            i += 1
            continue
        
        certificate=getCertificate(name, competition)
        htmlContent= getHtmlContent(name)
        # sort the data according to if the mail was sent or not
        if sendPdfAttachmentMail(record['Email Address'],certificate,htmlContent) == True:
            unsentRecords.remove(record)
            sentRecords.append(record)
            i -= 1
            unsentLength -= 1

        i += 1


except Exception as ex:
    print("[!] AN ERROR OCCOURED:-")
    print(ex)

finally:
    print("[+] Writing data to files before exiting...")

    if writeRecordsToCsv(sentRecords, sentMailsCsvPath):
        print("   [+] Sent records written to file")
    else:
        print("   [+] No sent records to write.")

    if writeRecordsToCsv(lengthIssueRecords, lengthIssueCsvPath):
        print("   [+] Names with lenght issues written to file")
    else:
        print("   [+] No names with lenght issues.")

    if writeRecordsToCsv(unsentRecords, unsentMailsCsvPath):
       print("   [+] Unsent records written to file")
    else:
        print("   [+] No unsent records to write.")


print("\n\n======== OPERATION SUMMARY ========")
print(f"\nTotal records to send: {totalRecords}")

print(f"\nSuccessful mails: {totalRecords - unsentLength - lengthIssueCount}")
print(f"--> Saved in: {sentMailsCsvPath}")

print(f"\nRecord with lenght issues: {lengthIssueCount}")
print(f"--> Saved in: {lengthIssueCsvPath}")

print(f"\nUnsuccessful mails: {unsentLength}")
print(f"--> Saved in: {unsentMailsCsvPath}")
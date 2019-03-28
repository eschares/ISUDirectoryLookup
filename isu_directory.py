#Use the online ISU Directory to look up ISU emails when given name
#
#Use Python module mechanize to interact with web forms
#Take list of authors
#Read in csv file
#pass author name to mechanize webform "individuals" field and submit
#Save off HTML output as .txt file
#For single person result, email appears as eschares (at) iastate (dot) edu
#Run through output file to look for "mailto:\' + ([\'eschares\', \'iastate.edu\']
#or (at) - email address

import csv               #open csv input files
import mechanize    #create browswer instance
import re           #be able to search
import os           #be able to delete files

filename = "ISU_author_mini.txt"
final_output_filename = "ISU_authors_with_email.txt"
heading="Name"

def check_for_old_file(filename):
        if os.path.exists(filename):
                os.remove(filename)
                print("Removing old " + filename)
        else:
                print("Creating " + filename)

check_for_old_file(final_output_filename)




def lookup_directory_webform(name):
        br = mechanize.Browser()
        br.open("https://www.info.iastate.edu/")
        br.select_form(nr=1)                    #select the second non-zero form, hard-coded for ISU Directory case
        br.form["individuals"] = name      #pass name to Search box
        br.submit()                        #submit query
        url= br.geturl()
        checkURL=re.split("search",url)
        contentB = br.response().read()
        content=(contentB.decode())
        if len(checkURL)>1:
                numContacts =re.findall("/individuals\/info", content)
                result= str(len(numContacts)) + " matches on that name\n"
        else:
                netidR=content.index("<noscript><div>")
                netidL=content.index(" (at)")
                netid=content[netidR+15:netidL]
                result=netid + "@iastate.edu\n"
                
        return result

     
with open(filename, mode='r') as csv_file:                  #way better method to open file and read in names
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
                emailLookup=lookup_directory_webform(row[0])
                with open (final_output_filename, 'a') as final_output:
                        for col in row:
                                final_output.write(col + "\t")

                        if row[0]==heading:
                                final_output.write("Email")
                        else:
                                final_output.write(emailLookup)
               

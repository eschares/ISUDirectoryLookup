# ISUDirectoryLookup
Lookup ISU emails given a csv file of names
Heather Lewin
Eric Schares
3/28/19

CSV file must have full name in first column, for example, Abdalla, Ahmed or Ahmed Abdalla
Column must be named "Name"
Other information can be present, will be echoed out to output file

Code process:
Use Python module mechanize to interact with web forms
Take list of authors
Read in csv file
pass author name to mechanize webform "individuals" field and submit
Get resulting URL
Multiple person result has "search" in URL
For single person result, email appears as eschares (at) iastate (dot) edu
Run through output file to look for "noscript><div>", pull netid

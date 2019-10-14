Create text file containing a list of IPs that you want to scan
Run the following nmap scan against that file to find which ssh keys are in use
	nmap -oA c:\temp\test --script ssh-hostkey -iL c:\temp\ips2.txt -T5 -p 22
		Change the output file (c:\temp\test) and input (c:\temp\ips2.txt) to the text file that has the list of IPs
That nmap scan will output an xml file (c:\temp\test)
Convert that xml file to a json file in powershell
	python -m xmljson -o c:/temp/data -d xmldata c:/temp/test.xml 
		Change the output file(c:/temp/data) and input file (c:/temp/test.xml) to the file created by the nmap scan
Change output name to 'filename'.json
Open ssh_keys.py
	Add correct file path to data_folder
	Add correct input file name to input_file
	Add correct output file name to output_file
Run ssh_keys.py to extract what ssh keys the devices with those IPs are using
	Script will read and write from/to the file path folder

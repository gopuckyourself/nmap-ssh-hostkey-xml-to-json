import json

#open json file (data.json) and write data to a new text file (ssh_keys_2048.txt) 
with open('data.json') as f, open('ssh_keys_2048.txt', 'w') as t:
    j_data = json.load(f)

    hosts = j_data['nmaprun']['host']

    for host in hosts:
        host_ip = host['address']['addr']
        try:
            keys = host['ports']['port']['script']['output']
            keys = keys.split('\n')
            #look for the key size in data and then write the host IP
            for key in keys:
                if '2048' in key:
                    t.write('{0}\n'.format(host_ip))
                    #you can parse more fields to export here
					#t.write(key)
                    #t.write('\n')
        except:
            continue
    


#!usr/bin/env python3

# Date: 02-21-18, Feb ~ 21th 2018 | Synchronocy
# Project: Discord Invite Checker
# Just for reference. you will need to cancel the checker inorder to write to file. please do not ALT+F4.

#~ #ChangeDiscord

import requests

web = 'https://discordapp.com/api/v6/invite/'

def check(invite):
    gurt = requests.get(web+invite)
    if int(gurt.status_code) == 200:
        print('https://discord.gg/'+invite)
        return 'https://discord.gg/'+invite
    if int(gurt.status_code) == 404:
        pass # I mean I tried using a continue but was out of loop >:(
    else:
        print('Unable to retrieve info from discordapp servers. https://discordapp.com/api threw a '+str(gurt.status_code)+' Status code.')
            

def bulkcheck():
    inputfile = input('Please enter the directory where your file is located. (we are in the directory you ran me in)\n:')
    with open(inputfile,'r') as infile:
        b = infile.readlines()
        with open('valid.txt','a') as outfile:
            for x in b:
                x = x.rstrip()
                if len(x) > 30:
                    x = x[30:] # invite code is typically 7 char
                    try: # now with this is the way I found that worked to rid the 'None' in writing to the file.
                        outfile.write(check(x))
                        outfile.write('\n')
                    except Exception:
                        continue
                elif len(x) < 30: # basically discord.gg links
                    x = x[19:]
                    try:
                        outfile.write(check(x))
                        outfile.write('\n')
                    except Exception:
                        continue
                elif len(x) == 7:
                    try:
                        outfile.write(check(x))
                        outfile.write('\n')
                    except Exception:
                        continue
                else:
                    print('Error loading invite code: '+x)
                    
def singlecheck():
    i = input('Discord Invite\n:')
    if len(i) > 30:
        i = i.replace('https://discordapp.com/invite/','')
        check(i)
    elif len(i) < 30:
        i = i.replace('https://discord.gg/','')
        check(i)
    elif len(i) == 7:
        check(i)
    else:
        print('Error')
        
def main():
    choice = int(input('1.) Bulk Check\n2.) Single Check\n:'))
    if choice == 2:
        singlecheck()
    elif choice == 1:
        bulkcheck()
    else:
        print('Please choose a number from 1 - 2.\n\n')
        main()

main()

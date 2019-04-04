# Writeup 2 - OSINT

Name: Kenton Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Kenton Wong

## Assignment Writeup

### Part 1 (45 pts)

1. name: Elizabeth Moffet

2. work: Cybersecurity/Blockchain/Finance/Banking CEO at 13/37th National Bank
website: http://1337bank.money/

3. personal info:
v0idcache is the username of the Twitter user Elizabeth Moffet. This account was found using the Twitter Tool on IntelTechniques. The tool was chosen by chance and the username "v0idcache" was inputted. Moffet lives in Waterland, Netherlands. This was found using who.is by entering the URL 1337bank.money found on Moffet's Twitter page. In addition to her Twitter page, her Reddit account @v0idcache was found as well.
![Reddit 1](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/reddit.png "Reddit 1")
![Reddit 2](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/reddit2.png "Reddit 2")
Both the Twitter and Reddit accounts were confirmed using SocialSearcher. No other social media accounts were found. This is confirmed by both NameVine and UserSherlock.
fl1nch and Dev0id_cache are two contacts found connected to v0idcache. fl1nch was found by searching "v0idcache" on pastebin.com, and a conversation between the two came up. In this conversation, a file called AB4300.txt was mentioned. This file will later be found to be a file in Part 2 in the /home/files directory saying "CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}". Dev0id_cache was found using SocialSearcher; it appears as if Dev0id_cache is male, for he tried to shoot his shot on Twitter but was, unfortunately, ghosted by Moffet (but hey it's 2019). No other contacts were found.
Some emails associated with v0idcache are v0idcache@protonmail.com, v0idcache@gmail.com, v0idcache@hotmail.com, v0idcache@aol.com, and v0idcache@yahoo.com. The ProtonMail account was found on her website. The other four emails were found using PeekYou and Spokeo.
![Emails](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/emails.png "Emails")

4. IP address: 142.93.136.81
This IP address was found on who.is. The domain name was inputted into who.is and the traceroute led to this IP. The location of the server is in Amsterdam, Netherlands. This was found using HostingChecker. The URL was entered and this location was the result. The DNS history was discovered using mxtoolbox. the URL was entered in the DNS lookup tool and this was the result:
![DNS](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/dns_records.png "DNS")
Other related IP addressed were found using ThreatIntel. The domain name was entered and this was the result:
![IPs](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/ips.png "IPs")

5. hidden files/directories:
Two hidden files/directories were found: secret_directory and a hidden .txt file. secret_directory was found using the /robots.txt extension in the URL. A directory named "secret_directory" was disallowed. It was then added to the URL and a flag (CMSC389R-{h1ding_fil3s_in_r0bots_L0L}) showed up. The hidden .txt file was found using the TXT lookup tool in mxtoolbox:
![TXT](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/txt_files.png "TXT")
Though not a file/directory, another flag (CMSC389R-{h1dd3n_1n_plain_5ight}) was found using the Inspect Element feature in Google Chrome. Furthermore, some code was found to be commented out. After uncommenting them, a white rectangular space and a black/gray rectangular space appeared in the background image of the website.
![Hidden Comment](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/hidden_comment.png "Hidden Comment")
![Hidden Images](https://github.com/kdubbs0/389Rspring19/tree/master/assignments/2_OSINT/writeup/pics/hidden_imgs.png "Hidden Images")

6. ports: 22, 80, 1337
Port 22 had SSH running behind it, port 80 had http running behind it, and 1337 had TCP running behind it. These were found using nmap in the Kali terminal. The command "nmap -v -p 1-65535 -O -sS -T5 142.93.136.81" was used to obtain this information. Ports 22 and 80 were protected, so port 1337 was used in Part 2.

7. OS: Ubuntu-4ubuntu0.2
This was found when attempting Part 2. When in the terminal in Kali, the command "telnet 142.93.136.81 22" was run, and it coincidentally gave me the OS.

8. I believe all discovered flags are listed throughout the assignment either in text or in an attached image(final flag is in Part 2).
Much other information was collected on the side, including the domain ID 3373e5a94f364689b318a49d97c33f1e-DONUTS, the website Registrar and registration info, server language, and sites that have 1337bank.money blacklisted.

### Part 2 (75 pts)

final flag: CMSC389R-{brut3_f0rce_m4ster}

My stub.py program has a main method that calls the bruteforce method in a loop, iterating through each "fleming," or line in the wordlist file. Each call to the bruteforce method passes the next fleming as a parameter and inputs that fleming into the password prompt after inputting "v0idcache\n" as the username. The newline character has the same purpose as a manual "enter" key. The "data" variable then stores the output given when the username and password are both entered. It can be one of two options: "Fail\n" or "Success!\n" (discovered later). I programmed it so it would output each username/password tried and try them until the output was not "Fail\n". The last outputted password is the correct password.

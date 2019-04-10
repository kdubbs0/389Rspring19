# Writeup 6 - Forensics

Name: Kenton Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Kenton Wong

## Assignment Writeup

### Part 1 (45 Pts)

1. 142.93.168.81 was attacked

2. nmap was used to find the open port; a SecList was used to bruteforce the password by connecting to the server on the vulnerable port; command injections were used to retrieve the jpeg

3. The hackers' IP addresses are 159.203.113.181 and 185.199.110.153. Other IP addresses found from the pcap file are 113.176.70.179, 37.237.212.29, 178.19.107.42, and 184.22.161.10. The hackers are connecting from 101 Ave of the Americas, 10th Floor, New York, NY 10013.

4. Port 20 was used to steal the files on the server.

5. The file find_me.jpeg was stolen. It is a jpeg file of a picture taken in Rambla General Jose Artigas, 20100 Punta del Este, Departamento de Maldonado, Uruguay, 4.5 meters below sea level, on Sunday, December 23, 2018, 5:16:24 PM on an Apple iPhone 8 camera.

6. The file greetz.fpff was left on the server by the hackers.

7. A possible countermeasure to prevent this kind of intrusion from happening again is switching from http to https.

### Part 2 (55 Pts)

1. greetz.fpff was generated on March 27, 2019 at 4:15:05

2. The author of the file is fl1nch

3. SECTIONS:
	- 1	(ASCII)	Hey you, keep looking :)
	- 2	(COORD)	52.336035, 4.880673
	- 3	(PNG)	a png file
	- 4	(ASCII)	first flag listed below (found when parsing)
	- 5	(ASCII)	second flag listed below (found by converting section value to base 64 ASCII)

4. FLAGS:
	- CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R} (but backwords)
	- CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}

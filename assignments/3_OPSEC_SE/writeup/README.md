# Writeup 3 - Operational Security and Social Engineering

Name: Kenton Wong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Kenton Wong

## Assignment Writeup

### Part 1 (40 pts)

A possible pretext would be if I were a leader of Girl Scouts troop number 7331 based in Whynot, North Carolina trying to sell Girl Scout cookies internationally online through a "new website" that I will have created. The website will be "in progress" so that it would not be as suspicious if it is low quality/effort. In the website, javascript code can be embedded to determine the app that is being used, giving us an answer to 1 of the 5 questions. To make a purchase on the website, an account must first be created. To make an account, information needed will be: username, 4-digit passcode, and answers to 3 security questions. The 4-digit passcode will be assumed to be the same as her ATM PIN code since her password was among the most commonly used (meaning she is generally not very digitally secure). The 3 security questions that will be asked will be the last 3 questions we need answers to (mother's maiden name, birth city, name of her first pet). With this, we are able to collect answers to all 5 questions using this website.

The social engineering part will start with a phone call spoofed from a random number with area code 336 (area code for Whynot, NC). This peculiar town name may throw Moffet off and be suspicious, but once verified, her trust in me will increase. I can inform her about a sale that is going on for the cookies we are selling for people who create accounts and order in the next hour or so, making it more appealing to make an account. I can also include that some of the proceeds will be donated to a local charity.

There will be background noise similar to a Girl Scout meeting; this may be produced from a website online. Occasional fake communication between members and myself can be used to more successfully emulate the environment.

Once Moffet is on the site and creating the account, she may have some suspicions. If she questions my use of a 4-digit passcode, I can say that it is being implemented for the sake of ease of access. If she question the security questions, I can say that because we are accepting payments through the site with features that allow the saving of credit card information, we are taking a little extra precautions if any fishy transactions are made (or if she loses her login info).

### Part 2 (60 pts)

The first weakness that I thought of was, of course, the password. This is a problem because it was easily identified using wordlist, which makes it one of the most commonly used passwords and easily accessible. To cover this weakness, the most obvious solution is to strengthen then password; Moffet could add numbers/special characters, uppercase letters, less common phrases, etc rather than a simple phrase in all lowercase letters. This will work because the chances of multiple other people using the same password with the same exact insertions/replacements is much slimmer, meaning it will likely not be on the wordlist, preventing successful bruteforce attempts to compromise the account.

The second weakness would be the exposed port used to access the login. This is a problem because with the port number, I was able to send information directly to the server and ultimately gain access to it. By using nmap, I easily found that port 1337 was open and vulnerable; it just took a little bit of waiting to scan the ports. A possible fix to this problem would be to protect it by setting up a firewall. This is a solution because the reason why I had access to port 1337 was because it was unprotected; putting up a firewall on that port would make it protected and deny information that I may try to send it.

Another weakness that I noticed was that the username "v0idcache" was given to us. The hint "use OSINT" in the homework description was vague but proved to not require any effort at all, as it was given to us. This is a problem because, similar to the password, this information was extremely easy to figure out (since it was given). To combat this problem, a different username can be used insteaed of the same one she uses for literally everything else. Moffet does not necessarily need to make all of her usernames different, but she should at least have a unique work username (maybe an ID number or employee ID, or something more professional than "v0idcache"). This is a solution because if her username on the server was not "v0idcache" then I would probably not have gotten access to the server at all (at least not without much more effort).

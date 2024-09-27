# telefonkatalogen-veiledning

Åpne terminalen med CTRL + ALT + T (her skriver du kommandoene under)
Se etter og installer oppdateringer til all programvare som er installert
 a. sudo apt update (finner oppdateringer)
 b. sudo apt upgrade (installerer oppdateringer)

Sett opp brannmur med UFW (uncomplicated firewall)
 a. sudo apt install ufw (installerer UFW)
 b. sudo ufw enable (aktiverer brannmuren ved oppstart)
 c. sudo ufw allow ssh (tillater SSH-tilkoblinger gjennom brannmuren)
 d. Senere kan du sjekke statusen på brannmuren ved å skrive sudo ufw status

Skru på ssh
 a. sudo apt install openssh-server (installerer SSH-serveren)
 b. sudo systemctl enable ssh (gjør sånn at SSH skrur seg på ved oppstart)
 c. sudo systemctl start ssh (starter SSH her og nå)

Finn IPen din – den trenger du når du skal bruke SSH
 a. ip a
 b. Hvis du har kablet nettverk, vil IP vises ved eth0: linje. Hvis du kun har trådløst, vil ipvises ved wlan0: linje. IP-adresse er vanligvis 10.2.3.x eller noe lignende (hvor x er etnummer mellom 2 og 254)

Installer Git, Python og MariaDB
 a. sudo apt install python3-pip
 b. sudo apt install git
 c. sudo apt install mariadb-serverd. sudo mysql_secure_installation

Lag ny database-bruker og sett riktige rettigheter
 a. Logg inn i MariaDB >i. sudo mariadb –u root
 b. Lag ny bruker >i. CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
 c. Gi ny bruker rettigheter >i. GRANT ALL PRIVILEGES ON *.* TO 'username'@’localhost’IDENTIFIED BY 'password';
 d. Oppdater rettigheteri. FLUSH PRIVILEGES;

Installer annen programvare du ønsker. For eksempel VS Code, en annen nettleser,wireshark, nmap, etc
 a. Hvis du får trøbbel med VS Code, last ned .deb for arm64 frahttps://code.visualstudio.com/docs/setup/linux Naviger til mappen du lastetned filen
 b. Skriv sudo apt install ./code og trykk tab, så enter

9. Kjør sudo apt update og sudo apt upgrade igjenStyr maskinen fra laptopen med SSHI fremtiden kan du styre Pien fra laptopen din med SSH, f.eks. i CMD eller PowerShell. Hvis du vil koble til med ssh fra laptop skriver du:
 a. ssh brukernavn@ip
 b. (bytt ut brukernavn og ip med dine)
PS: Skru av maskinen med sudo shutdown now og vent litt før du eventuelt tar strømmen

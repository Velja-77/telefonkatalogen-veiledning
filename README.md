Sett opp Raspberry Pi med operativsystem 
Bruk 'Raspberry Pi Imager' til å installere operativsystem på SD-kortet, som du så putter inn i Pi-en.

Installer programmer
I operativsystemet Linux installerer man programmer i terminalen med denne kommandoen:
brukernavn@maskinnavn:~$ sudo apt install [programnavn]

Ofte er det lurt å kjøre disse to linjen først, for å få siste versjon av programmene:
sudo apt update (finner oppdateringer)
sudo apt upgrade (installerer oppdateringer)

Så programmene:
sudo apt install git (versjonshåndtering og overføring av filer)
sudo apt install openssh-server (installerer SSH-serveren)
sudo apt install mariadb (databaseprogrammet)
sudo apt install ufw (brannmur)

Konfigurer programmer
Noen av programmene krever litt innstillinger før de kan brukes.

For at SSH skal startes automatisk hver gang du skrur på serveren skriver du disse to linjene: 
sudo systemctl enable ssh (gjør sånn at SSH skrur seg på ved oppstart)
sudo systemctl start ssh (starter SSH her og nå)

Brannmur (ufw)
For at andre maskiner skal kunne snakke med programmer på serveren åpner vi porten som programmet kjører på. Her åpner vi port 22, som er den porten SSH kommuniserer på.
sudo ufw enable (aktiverer brannmuren ved oppstart)
sudo ufw allow ssh (tillater SSH-tilkoblinger gjennom brannmuren. Port 22.)

Database (MariaDB)
Før vi oppretter en database med tabeller, må vi lage en bruker i databasen.
sudo mariadb (logg inn med superbruker første gang)
CREATE USER '[username]'@'%' IDENTIFIED BY '[password]';
GRANT ALL PRIVILEGES ON *.* TO '[username]'@’%’ IDENTIFIED BY '[password]';
FLUSH PRIVILEGES;
Logg ut ved å skrive exit
Logg inn den nye brukeren:
mariadb -u [brukernavn] -p

På din PC:
Logg inn på serveren (Pi) gjennom cmd i Windows
Åpne cmd og kjør: ssh [brukernavn]@[ip-adresse]
Microsoft Windows [Version 10.0.22631.4112]
(c) Microsoft Corporation. All rights reserved.
C:\Users\Veljko Tomic>ssh pi@10.2.3.62
pi@10.2.3.62's password:

Første gang du logger på med en ny maskin får du denne:

The authenticity of host '111.222.333.444 (111.222.333.444)' can't be established.
RSA key fingerprint is f3:cf:58:ae:71:0b:c8:04:6f:34:a3:b2:e4:1e:0c:8b.
Are you sure you want to continue connecting (yes/no)? 

Skriv yes

Når du er logget inn ser terminalen slik ut:

Linux raspberrypi 5.10.103-v7l+ #1529 SMP Tue Mar 8 12:24:00 GMT 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Sep 4 14:35:08 2024 from 10.2.1.89
pi@raspberrypi:~ $

Det betyr at du nå er logget inn på Raspberry Pi-en og styrer den via terminalen/cmd i Windows.
pi er brukernavnet du er logget inn med, raspberrypi er maskinnavnet

Lag database
Logg inn i MariaDB og skriv/lim inn koden fra de tre første sql-filene:

CREATE DATABASE telefonkatalog;

USE telefonkatalog;
CREATE TABLE person (
 id int NOT NULL AUTO_INCREMENT,
 fornavn VARCHAR(255) NOT NULL,
 etternavn VARCHAR(255) NOT NULL,
 telefonnummer CHAR(8),
 PRIMARY KEY (id)
);

INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES ('Erik', 'Perik', '12345678');
INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES ('Lise', 'Pise', '22334455');
INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES ('Testus', 'Jensen', '11114444');
INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES ('Knut', 'Donald', '31415926');

Test databasen med disse kommandoene:
SELECT * FROM person;
SELECT fornavn, telefonnummer FROM person;
SELECT * FROM person WHERE fornavn = "Erik";
SELECT telefonnummer FROM person WHERE fornavn = "Lise" AND etternavn = "Pise";

Koble Python-koden til databasen
I filene fra GitHub er det en Python-katalog. Hent filen telefonkatalog_oppdater_sql.py og lagre den på laptopen (ikke på Pi-en).
I Python-koden er det flere steder der man skal koble til databasen. De ser slik ut:
 mydb = mysql.connector.connect(
 host="172.29.51.19",
 user="test",
 password="1234",
 database="telefonkatalog"
 )

Endre ip-adresse til Pi-ipen din (bruk ip a i terminalen for å se den).
Endre brukernavn og passord til den databasebrukeren du laget oppe i database-avsnittet (CREATE USER etc.)

Teste prosjektet
Kjør Python-koden telefonkatalog_oppdater_sql.py fra laptopen din, og sjekk om personene fra databasen dukker opp.
Prøv også å legge til nye brukere i programmet, og logg inn i MariaDB på serveren og sjekk om de dukker opp i databasen med SELECT * FROM person.

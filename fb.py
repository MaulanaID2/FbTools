#!/usr/bin/python2
# -*- coding: utf-8 -*-
# coded by MaulanaTeam

try:
    import mechanize,requests,os,sys,subprocess,cookielib,time,random
except ImportError:
    subprocess.call("pip2 install requests mechanize", shell=True)

subprocess.call("clear",shell=True)

#color
green = "\033[1;32m"
normal = "\033[0m"
red = "\033[1;31m"
cyan = "\033[1;36m"
#symbols
good = "\033[1;32m[\033[1;36m+\033[1;32m]\033[0m"
bad = "\033[1;32m[\033[1;31m!\033[1;32m]\033[0m"
#word
success = "\033[1;32mSuccessful\033[0m"
failed = "\033[1;31mFailed\033[0m"

###banner###
banner_menu = """



                                     `oddhhhhyysss
                                    .ydhhhddyyso+/
                                   -hdyssyh-      
//::--..``             ./`  `     -ddhssyy`       
yyhhhhhhdhyyo/.       `s/`-/-    `ydhsss/`        
yyyyyysymddddmms.     -o./+-..   .ddsso.          
+++/-`  .:+shhhdd+`  ..` .`...+o::dhs/`           
         -. `-+yydh://.`.:...-:/shdh+`   -`       
        `+y` `yo`::.-:/:::::/:-..:ydo-``/y-       
         :do `ds::-`.:--``..`..``.-ods:+hy.  `:+` 
         `oh:`o:-:..-.-....```...---+dohho `/yy/  
          `oy.-.`-` ....`. ```....---/ddh:-yhy/`  
        `-+y-``  .  ``````` `  `..-.--hhs+hdo.    
        +hy:` `` -```-`````...``. .`..syyyh:      
       `sy:.  .`.-.``:..`-.....`..` `.shhhhh.     
       `s::.  .`:`-/`-.`..:--::--.  .-hhhhhy-     
       `:++.  `..-o+yo:````--shhy/``.ymdhhhy/`    
       --oo-  ``-:.:/+:`````./++++`--ymmddds/.    
        `+o/``` .o:--.```````.--....-:shhho::.    
         `-/`. ``+/.```o++/-``../:...-:+o+:`.     
          .:-/```-----.-:::---/so....-s+:.`       
       `-//+:::`.`:::::-:://////.`..:///-`        
`````...-++//::--:-:::::::///+:`--::----:+.       
.-.````.:::+++++/++:/:----:-...://///:---+`       
.``````:-....:+yyys+++/:-----://++++++++oo-       



Created.           : {}MaulanaID{}
Github.            : {}https://github.com/MaulanaID{}
-----------------------Menu Bot----------------------
                   1 Login Dulu Disini
                  2 AUTO LIKE! MAX.200!
                     3 AUTO COMMENT!
                  4 AUTO FRIEND REQUEST!
""".format(red,cyan,yellow,green,purple)

banner = """
                                      `oddhhhhyysss
                                    .ydhhhddyyso+/
                                   -hdyssyh-      
//::--..``             ./`  `     -ddhssyy`       
yyhhhhhhdhyyo/.       `s/`-/-    `ydhsss/`        
yyyyyysymddddmms.     -o./+-..   .ddsso.          
+++/-`  .:+shhhdd+`  ..` .`...+o::dhs/`           
         -. `-+yydh://.`.:...-:/shdh+`   -`       
        `+y` `yo`::.-:/:::::/:-..:ydo-``/y-       
         :do `ds::-`.:--``..`..``.-ods:+hy.  `:+` 
         `oh:`o:-:..-.-....```...---+dohho `/yy/  
          `oy.-.`-` ....`. ```....---/ddh:-yhy/`  
        `-+y-``  .  ``````` `  `..-.--hhs+hdo.    
        +hy:` `` -```-`````...``. .`..syyyh:      
       `sy:.  .`.-.``:..`-.....`..` `.shhhhh.     
       `s::.  .`:`-/`-.`..:--::--.  .-hhhhhy-     
       `:++.  `..-o+yo:````--shhy/``.ymdhhhy/`    
       --oo-  ``-:.:/+:`````./++++`--ymmddds/.    
        `+o/``` .o:--.```````.--....-:shhho::.    
         `-/`. ``+/.```o++/-``../:...-:+o+:`.     
          .:-/```-----.-:::---/so....-s+:.`       
       `-//+:::`.`:::::-:://////.`..:///-`        
`````...-++//::--:-:::::::///+:`--::----:+.       
.-.````.:::+++++/++:/:----:-...://///:---+`       
.``````:-....:+yyys+++/:-----://++++++++oo-       
Author : {}MaulanaID{}                                                                     
Facebook : {}Maulana ID{}
Github : {}https://github.com/MaulanaID{}
""".format(red,cyan,yellow,green,purple)
###


br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
info = time.strftime("%S:%M:%H")

def generate_token():
    print banner
    print
    username = raw_input("[+] ID/Username : ")
    password = raw_input("[+] Pass : ")
    print "[{}]{} Sabar Gan ....".format(info,good)
    time.sleep(5)
    if len(username) == 0:
         print "[{}]{} You Must Input Your {}Username{} !!!".format(info,good)
    elif len(password) == 0:
        print "[{}]{} You Must Input Your {}Password{} !!!".format(info,good)
    else:
        token_parsing = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + username + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").read()
        file_token_access = open("token.txt","w")
        file_token_access.write(str(token_parsing))
        file_token_access.close()
        try:
            print "[{}]{} STATUS : {}".format(info,good,success)
            print "[{}]{} Tersimpan: token.txt".format(info,good)
        except:
            print "[{}]{} Error Operation System".format(info,bad)

def autolike():
    print banner
    print
    token = open("token.txt","r").read()
    a = br.open("https://yolikers.com/")
    br.select_form(nr=0)
    br.form["access_token"] = token
    br.submit()
    try:
        react = raw_input("[+] Mau Reaksi Paan njer? ['LIKE','LOVE','HAHA','WOW','SAD','ANGRY'] : ")
        d = br.open("https://yolikers.com/like.php?type=status")
        br.select_form(nr=0)
        br.form["type"] = [""+react]
        br.submit()
        print "[{}][+] Udh Gan..".format(info,good)
    except:
        print "[{}][+] Nanti lagi njink ".format(info,bad)

def comment():
    print banner
    print
    print "[{}]{} sabar yah😙...".format(info,good)
    token = open("token.txt","r").read()
    a = br.open("https://yolikers.com/commenter.php?type=status")
    br.select_form(nr=0)
    br.form["access_token"] = token
    br.submit()
    try:
        b = br.open("https://yolikers.com/commenter.php?type=status")
        br.select_form(nr=0)
        br.submit()
        print "[{}]{} Udh Njink..".format(info,good)
    except:
        print "[{}]{} Nanti lagi yah Bgsd..".format(info,bad)

def friend():
    print banner
    print
    print "[{}]{} sabar yah 😙...".format(info,good)
    token = open("token.txt","r").read()
    a = br.open("https://yolikers.com/")
    br.select_form(nr=0)
    br.form["access_token"] = token
    try:
        b = br.open("https://yolikers.com/autorequest.php?type=profile")
        br.select_form(nr=0)
        br.submit()
        print "[{}]{} Success Njenk...".format(info,good)
    except:
        print "[{}]{} nanti lagi bgsd...".format(info,good)


if __name__=="__main__":
    while True:
        print banner_menu
        print
        pilih_menu = raw_input("[+] Kau mau apaan ?😙: ")
        if len(pilih_menu) == 0:
            print "{} Kau mau paan Tod !!!".format(bad)
        elif pilih_menu == "1":
            generate_token()
            time.sleep(5)
        elif pilih_menu == "2":
            autolike()
            time.sleep(5)
        elif pilih_menu == "3":
            comment()
            time.sleep(5)
        elif pilih_menu == "4":
            friend()
            time.sleep(5)

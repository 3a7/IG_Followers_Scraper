import requests, re, uuid, calendar,time, sys
from time import sleep
from random import choice,randint
from os import system
from colored import fg,attr

g = lambda x : fg('green')+x+attr('reset')
rod = lambda x : fg('red')+x+attr('reset')
b = lambda x : fg('blue')+x+attr('reset')
y = lambda x : fg('yellow')+x+attr('reset')
c = lambda x : fg('cyan')+x+attr('reset')
m = lambda x : fg('magenta')+x+attr('reset')

clear = lambda: system("cls")
clear()
exl = '['+rod('!')+']'
ques = '['+m('?')+']'
ha  ='['+g('#')+']'
mult = '['+c('*')+']'
system('title WELCOME TO IGA7 Scraper !')
print(y('''
  ___    _ _                         ___                            
 | __|__| | |_____ __ _____ _ _ ___ / __| __ _ _ __ _ _ __  ___ _ _ 
 | _/ _ \ | / _ \ V  V / -_) '_(_-< \__ \/ _| '_/ _` | '_ \/ -_) '_|
 |_|\___/_|_\___/\_/\_/\___|_| /__/ |___/\__|_| \__,_| .__/\___|_|  
                                                     |_|            '''))
print(m('                                    CopyRight: https://www.instagram.com/a7.acc\n'))
def ra(length,ty):
    if ty == 'a0':#   Small letters only with numbers
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'A0':# Capital letters only with numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    elif ty == 'Az':# Capital and small letters only
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    elif ty == 'All':#Capital and small letters and numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'a':#  Small letters only
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm')
    elif ty == 'n':#  Numbers only
        randoms = ''.join('1234567890')
    random_str = ''
    for _ in range(int(length)):
        random_str += choice(randoms)
    return random_str


#                TO GENERATE RANDOM USER AGENT
def generate_user_agent():
    useragents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2828.31 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2643.44 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2965.63 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2862.69 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2950.18 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)'
        'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2845.18 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2889.10 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.89 Safari/537.36'
        'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2770.77 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.44 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2751.15 Safari/537.36'
    ]
    return choice(useragents)

    
def login(username,password):
    print(ha+' Trying to log in this account >> '+str(username))
    head = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {ra(16,'a0')}/{ra(16,'a0')}; {ra(16,'a0')}; {ra(16,'a0')}; {ra(16,'a0')}; en_GB;)"}
    data = {
        "jazoest": "22452",
        "phone_id": uuid.uuid4(),
        "enc_password": f"#PWD_INSTAGRAM:0:{calendar.timegm(time.gmtime())}:{password}",
        "username": username,
        "adid": uuid.uuid4(),
        "guid": uuid.uuid4(),
        "device_id": uuid.uuid4(),
        "google_tokens": "[]",
        "login_attempt_count": "0"}
    logged = False
    r1 = ''

    try:
        r1 = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=head, data=data, timeout=5)
        logged = True
    except Exception as exxx:
        print(exl+' Error while logging in with '+c("@"+username)+' >> '+str(exxx))
        sleep(5)
        sys.exit()
    
    username = '@'+username
    if "logged_in_user" in r1.text and logged:
        print(f"{ha} Logged In >> {g(username)}")
        the_cookie = r1.cookies.get_dict()
    elif '"message":"challenge_required"' in str(r1.text):
        print(f"{exl} Failed Login >> {rod(username)} "+'|Secured account|')
        the_cookie = []
    else:
        print(f"{exl} Failed Login >> {rod(username)}")
        print(exl+' Uknown Error! >> '+str(r1.text)+'\n')
        the_cookie = []
    print()
    return the_cookie





def scrape_followers(target,cookie):
    global current_users,tracker
    current_users = set()
    tracker = 0
    
    def scrape(the_cookie,target_id,target):
        global current_users,total_scraped,tracker
        
        cok = ra(3,'a0')
        head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','sec-gpc': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','x-asbd-id': '198387','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR2bDMVPBHbpBmzrjerhUgPejilBDcKVMBzpUlRRdz88n'+cok}

        
        def get_users(users_list):
            for user in users_list:
                us = user['username']
                current_users.add(us)
        leny = 0
        num = 0
        while len(current_users) < 2000 and num < 10:
            things = [
                'QVFCeTQ3dExpdy0tVVFQbHcyYUxmZXVhSFBoVTZZVVFoMFM1WU4yT3lMM3BMQWJJRV9GTU8xZ0JBLTlRR3pMaTFiUDRVU3p5ZXlGNzVWeUMwc1dJeWxlMA',
                'QVFBNWt6QTU4QlNINEotazdZcUJJd0xCY1h6UVd5dzFZX18tOExuQ080Wk14YzE4TlNHdTMtUnFVSjBXVmthSXdDVWw3YTluRWdYcllod05WcXFWTTBsNw',
                'QVFEUzF3Mm8yQ1JwWDNZUWxNSmhLWUNLVld2Q1JPV2VKNXZCSHFqMDY5aWhJYXBrTFc2ZjB6enRrNnI5SkxsQ1drcmNrYm8xUEdRY0pCdFM0Y3ZucjJwSQ',
                'QVFCZjZwMVZqZ0JVYU1rVWFLdkpFakZETG85eV9KV1FVSXJDOXF1QnN4Tm9rSzQ5VjdtMHdqNmc0TVpCbE5rN3hOQ1A5ZzZxQjZIOFMtWEtKekhzeXFtcA',
                'QVFDZ29xNVVnZGppXy1PcGh4a2ZSeG82UlRqaDVYd2VUaXpHMzR2blBGNjVfdnRheUZjODZXZjUzcXdJbU0tTTZ3MlNrRG4zX2VxTHJReTRxQkUwaTlCdA',
                'QVFESDBCODM5TzVmR3JaYUpzeDJKWDNMdG1za0VJTFdzdjc4Q2JidHJYR01Zczl6dlhEOW9CUmJsdll1eFJ1Ykp0NkYzOG1qUXE4ZmNldXFpWFE0eDF0eg',
                'QVFEREZpNGlmQWpSTzB2aXpsalFrYzhoaHNEWWJZV0J4NVVfeVpnWGpuNm8zal9nT3l3cHo1VXh1LTBWZjJnRmhZRUJRZFpuaXRzeFRBbGY3R0cxcmE4Mw'
                ]
            
            if num == 0:
                url = f'https://i.instagram.com/api/v1/friendships/{str(target_id)}/followers/?count=900&search_surface=follow_list_page'
            else:
                url = f'https://i.instagram.com/api/v1/friendships/{str(target_id)}/followers/?count={randint(800,900)}&max_id={choice(things)}%3D%3D&search_surface=follow_list_page'
            r = requests.get(url,headers=head,cookies=the_cookie)
            leny = len(current_users)
            num += 1
            try:
                get_users(r.json()['users'])
            except Exception as ex:
                print(exl+' Error While getting the usernames! >> '+str(ex))
            print(mult+' Scraped '+c(str(len(current_users)-leny))+'. Total '+c(str(len(current_users))))
            


    
        print(ha+' from ' +c("@"+target)+' Scraped >> '+b(str(len(current_users)))+' Usernames!!')


    
    #        Request to get the target's info     ////////   THREADS ARE 20 HERE
    #        pr checks if it is private or not // if_followed = if followed by the user account or not
    print(mult+' Scraping '+target+'..')
    followers = ''
    insta_req = requests.get(f'https://www.instagram.com/{target}',headers={'user-agent':generate_user_agent()},cookies=cookie).text
    pr = re.findall(r'"is_private":[a-z]{4,5},"',insta_req)[0]
    if_followed = re.findall(r'"followed_by_viewer":[a-z]{4,5},"',insta_req)[0]
    followers = re.findall(r'<meta property="og:description" content="\S{,}\s{1}Followers, \S{,}\s{1}Following, \S{,}\s{1}Posts',insta_req)[0].split('"')[3].split(' ')[0]
    try:
        target_id = re.findall(r':"profilePage_\d{,}\"',insta_req)[0]
        target_id = target_id[target_id.index('_')+1:-1]
    except:
        target_id = re.findall(r'"id":"\d+","is_b',insta_req)[1]
        target_id = target_id.split('"')[3]


        
    if 'true' in pr and 'false' in if_followed:
        print(exl+' This account '+c("@"+target)+' is private! try to follow the target and get accepted or enter another target!')    
        sleep(5)


    #          DEALING WITH THE FOLLOWERS AND CHANGING THEM TO REAL WORLD NUMBERS

    if 'k' in followers:
        followers = followers[:-1]+'000'
    elif 'm' in followers:
        followers = followers[:-1]+'000000'
    elif ',' in followers:
        v = followers.split(',')
        followers = v[0]+v[1]
    if '.' in followers:
        v = followers.split('.')
        followers = v[0]+v[1][:-1]
    

    scrape(cookie,target_id,target)
    print()
    
    print(str(len(current_users))+' Usernames scraped')
    with open('scraped_usernames.txt','w',encoding='utf-8') as file:
        for u in current_users:
            file.write(u+'\n')
    print(ha+' All the usernames are saved in scraped_usernames.txt file!')
    sleep(5)


def main():
    while True:
        try:
            cred = input(ques+' Enter an Instagram account username:password >> ')
            if ':' in cred:
                break
        except:
            print(exl+' Please enter the account in this format username:password!')
            sleep(2)
            pass
    creds = cred.split(':')
    coo = login(creds[0],creds[1])
    
    if coo == []:
        sleep(10)
        return
    scrape_from = input(ques+' Enter the account you want to scrape from >> ')
    if scrape_from.startswith('@'):
        scrape_from = scrape_from[1:]
    scrape_followers(scrape_from,coo)
main()
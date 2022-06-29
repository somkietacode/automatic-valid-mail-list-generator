import argparse ,  subprocess
from lib import nqtm

try:
    from googlesearch import search
except ImportError:
    #print("No module named 'google' found")
    pass
from bs4 import BeautifulSoup
import re , requests



def find_mail_by_name(name,k,g,domaine,conutrycode):
    print("looking for :"+name+" on the world wild web ")
    print("---------------------------------------------------------------------------------------")
    query = name+'''"'''+domaine+'''"'''
    head = {'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-G960F '\
                            'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '\
                            'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'}
    for j in search(query, tld=conutrycode , stop=200000, pause=100 , user_agent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F '\
                            'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '\
                            'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'):
        if 'pdf' in j :
            pass
        else :
            try:
                url = j
                r = requests.get(url , headers = head, timeout = 5 )
                code = r.status_code
                if code == 200:
                    soup = BeautifulSoup(r.text, 'lxml')
                    for x in  re.findall(r'[\w\.-]+'+domaine+'+', soup.text ) :
                        if x not in k :
                            print(x)
                            g.write(x+'\n')
                            k.append(x)
            except Exception as e:
                pass

    return k

parser = argparse.ArgumentParser(description='Mail Extractor Pro : A tool permit mail extraction automation base on name liste domaine name and geo array.')
parser.add_argument("-name_list" , "-n", help=" Enter full path of name list .")
parser.add_argument("-country_code", "-cc",help=" Enter geographical area code . Exemple : fr , nl , us ....")
parser.add_argument("-domaine_name", "-d",help=" define domaine name to extract . Exemple : @gmail.fr , @sfr.com ...")
parser.add_argument("-out", help=" path and name for the output file")

args = parser.parse_args()
try :
    k = []
    file = open(args.out,'w')
    nl_file = open(args.name_list,'r').readlines()
    nqnt = nqtm.xyz()
    nqnt.secure(nl_file)
    for name in nl_file :
        find_mail_by_name(name.replace('\n',''), k, file, args.domaine_name, args.country_code)
except Exception as e:
    print(e)
    pass

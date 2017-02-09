import urllib2
import urllib
import cookielib
import time
import datetime
import re
import os
 
def lSort(lOne, lTwo):
    tbDLP = []
    for i in lOne:
        nAppend = False
        for j in lTwo:
            if i == j:
                nAppend = True
        if nAppend == False:
            tbDLP.append(i)
    return tbDLP
 
def downList(dList,ext, urlA, urlB=''):
    for i in dList:
        urlpdf = urlA + i + urlB
        resPDF = opener.open(urlpdf)
        pdfB = resPDF.read()
        pdfN = i + '.' + ext
        pdfF = open(pdfN, 'wb')
        pdfF.write(pdfB)
        pdfF.close()
 
 
url = 'https://www.packtpub.com/packt/offers/free-learning'
email = '*******'
os.chdir('J:')
password = '******'
run = 1
Day = datetime.datetime.now().day
nextDay = True
while run == 1:
    while nextDay == False:
        time.sleep(3600)
        if Day != datetime.datetime.now().day:
            Day = datetime.datetime.now().day
            nextDay = True
    html = urllib2.urlopen(url).read()
    findFormID = str(html).find('input type="hidden" name="form_build_id" id="')
    html = html[findFormID + 45:]
    findEndValue = str(html).find('" value')
    html = html[:findEndValue]
    form_id = html
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'email' : email, 'password' : password, 'op' : 'Login', 'form_build_id':form_id, 'form_id' : 'packt_user_login_form'})
    resp1 = opener.open(url, login_data)
    hold = resp1.read()
    iLeft = hold.find('float-left free-ebook')
    hold = hold[iLeft:iLeft+500]
    iLeft = hold.find('href="')
    iRight = hold.find('" class=')
    hold = hold[iLeft+6:iRight]
    url2 = 'https://www.packtpub.com' + str(hold)
    print url2
    claimData = ''
    resp = opener.open(url2)
    print "Response 1"
    print resp1.headers
    print ''
    print ''
    print "Response 2"
    print resp.headers
    dLoads = resp.read()
    pdf = re.findall('/ebook_download/.*?/pdf', dLoads)
    code = re.findall('"/code_download.*?"', dLoads)
    pdfNums = []
    for i in pdf:
        iNum = i[16:len(i)-4]
        nAppend = False
        for j in pdfNums:
            if iNum == j:
                nAppend = True
        if nAppend == False:
            pdfNums.append(iNum)
    codeNums = []
    for i in code:
        iNum = i[15:len(i)-1]
        nAppend = False
        for j in codeNums:
            if iNum == j:
                nAppend = True
        if nAppend == False:
            codeNums.append(iNum)
    sFiles = os.listdir(os.getcwd())
    eFiles = []
    for i in sFiles:
        if os.path.isfile(i) == True:
            eFiles.append(i[:len(i)-4])
    tbDLP = lSort(pdfNums, eFiles)
    tbDLC = lSort(codeNums, eFiles)
    downList(tbDLP, 'pdf', 'https://www.packtpub.com/ebook_download/', '/pdf')
    downList(tbDLC, 'zip', 'https://www.packtpub.com/code_download/')
    nextDay = False

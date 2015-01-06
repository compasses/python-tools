#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      I311352
#
# Created:     22/12/2014
# Copyright:   (c) I311352 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re;
import time;
from collections import defaultdict;

Res  = defaultdict(dict);
FMap = defaultdict(dict);

commit = re.compile(r'commit ([0-9a-fA-F]+.)');
author = re.compile(r'Author: (.*) <*');
Modifyphp  = re.compile(r'M\t(.*$)');
PHPFile = re.compile(r'.*\/(.*\.php)');
MPHP = re.compile(r'M\t.*\/(.*\.php)')
APHP = re.compile(r'A\t.*\/(.*\.php)');


fow = open('./owner.txt',"w");
#occ-eshop*//(*.php)

def useString():
    regex = re.compile('(\d+)+')
    s = 'There are 9,000,000 bicycles in Beijing.'
    print re.findall(regex, s)
    index = 0;
    with open("C:\\Python27\\gitlog.txt", 'r') as f:
        for line in f:
            con = line.split(' ');
            au  = line.split(':');
            php = line.split('.');

            #print con
            if con[0] == 'commit':
                index += 1;
                print con[1];
            if au[0] == 'Author':
                print au[1];
            if len(php) == 2 and php[1] == 'php\n':
                print php[0]
    print index;

def startLog(line):
    print line;
    print re.findall(author, line);
    print re.findall(MPHP,  line);
    print re.findall(APHP,  line);

def useReg():
    index = 0;
    with open("C:\\Python27\\M3END.txt", 'r') as f:
        roundCheck = False;
        nowCot = False;
        nowAH = False;
        needAH = False;
        for line in f:
            #time.sleep(1);
            #print line;
            ct = re.findall(commit, line);
            if len(ct) > 0:
                nowCot = ct[0];
                needAH = True;

            if needAH == True:
                ah = re.findall(author, line);

                if len(ah) > 0:
                    nowAH  = ah[0];
                    needAH = False;
                    if Res.has_key(nowAH):
                        print nowAH;
                    else:
                        #print nowAH;
                        Res[nowAH] = {};
                        #Res[nowAH].append(0);
            else:
                Aphp = re.findall(APHP,  line);

                if len(Aphp) > 0:
                    Aphp = Aphp[0];
                    if Res[nowAH].has_key(Aphp):
                        Res[nowAH][Aphp][0] += 1;
                    else:
                        Res[nowAH][Aphp] = [1, 0];

                    if FMap.has_key(Aphp):
                        if FMap[Aphp].has_key(nowAH):
                            FMap[Aphp][nowAH][0] += 1;
                        else:
                            FMap[Aphp][nowAH] = [1, 0];
                    else:
                        FMap[Aphp] = {};
                        FMap[Aphp][nowAH] = [1, 0];
                else:
                    Mphp = re.findall(MPHP,  line);
                    if  len(Mphp) > 0:
                        Mphp = Mphp[0];
                        if Res[nowAH].has_key(Mphp):
                            Res[nowAH][Mphp][1] += 1;
                        else:
                            Res[nowAH][Mphp] = [0, 1];

                        if FMap.has_key(Mphp):
                            if FMap[Mphp].has_key(nowAH):
                                FMap[Mphp][nowAH][1] += 1;
                            else:
                                FMap[Mphp][nowAH] = [0, 1];
                        else:
                            FMap[Mphp] = {};
                            FMap[Mphp][nowAH] = [0, 1];

def getOwner(key):
    if FMap.has_key(key):
        dct = FMap[key];
        Max = 0;
        owner = 'finding';
        for k in dct:
            mark = dct[k][0] + dct[k][1];
            if mark > Max:
                Max = mark;
                owner = k;
        return owner;
    else:
        return 'not found';

def dumpToFileOwner():
    for key in FMap:
        fow.write(key);
        dct = FMap[key];
        fow.write('|');
        owner = getOwner(key);
        s = 'Owner: ' + owner + '|';
        fow.write(s);
        for key in dct:
            str2 = key + ' Add: ' + str(dct[key][0])+' Modify: '+str(dct[key][1]);
            fow.write(str2);
            fow.write('|');
        fow.write('\n');
    fow.close();

def main():
    pass;
    #str = "Author: Joe Qiao <j.qiao@sap.com>";
    #useReg();
    #print FMap;
    #print re.findall(author, str);



if __name__ == '__main__':
    main()


import re;
import gitlog;

gitlog.useReg();
gitlog.dumpToFileOwner();


pair = re.compile(r".*Error:(.+) File:(.+) \[\]*");

fl = open('./result.txt',"w");

dd = dict();

f = file('./occ_eshop.log')

NameFile = re.compile(r'.*\/(.*\.php)Line:\d+');

def getErrorInfo():
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        res = pair.match(line);
        if res == None:
            continue;
        if res.lastindex != 2:
            continue;
        mathres = res.group(1) + '|' + res.group(2);
        filename = re.findall(NameFile, res.group(2));
        if len(filename) > 0:
            filename = filename[0];
            owner = gitlog.getOwner(filename);
            mathres += "|Owner: " + owner;

        if dd.has_key(mathres):
            dd[mathres] += 1;
        else:
            dd[mathres] = 1;

        #print mathres;
        # Notice comma to avoid automatic newline added by Python
    f.close() # close the file

    for key in dd:
        fl.write(key);
        fl.write("|");
        fl.write(str(dd[key]));
        fl.write('\n');

    fl.close();
    #print dd;

def main():
    s = "/var/www/eshop/wp-content/themes/anweshop/core/dispatcher.phpLine:125";

    print re.findall(NameFile, s);
    getErrorInfo();


if __name__ == '__main__':
    main()


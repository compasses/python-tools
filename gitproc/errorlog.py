
import re;
import gitlog;

gitlog.useReg();
gitlog.dumpToFileOwner();


pair = re.compile(r".*Error:(.+) File:(.+) \[\]*");

pair2 = re.compile(r".*Error:(.+)\\nFile:(.+)\",(\"context\":*)");

fl = open('./result.txt',"w");

dd = dict();

f = file('./eshop.log')

NameFile = re.compile(r'.*\/(.*\.php)Line:\d+');

def getErrorInfo():
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        res = pair2.match(line);
        if res == None:
            continue;
        if res.lastindex != 3:
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
    #getErrorInfo();
    # s = "/var/www/eshop/wp-content/themes/anweshop/core/dispatcher.phpLine:125";
    # #print re.findall(NameFile, s);
    # s = '{"message":"Error No.:2\\nError:Invalid argument supplied for foreach()\\nFile:/var/www/eshop/wp-content/plugins/anywherecommerce/model/class-anw-setting.phpLine:32","context":[],"level":300,"level_name":"WARNING","channel":"occ_eshop_log","datetime":{"date":"2015-03-25 03:36:36","timezone_type":3,"timezone":"UTC"},"extra":{"memory_usage":"4.5 MB","process_id":30,"url":"/","ip":"172.17.42.1","http_method":"GET","server":"127.0.0.1","referrer":null,"file":"/var/www/eshop/wp-content/plugins/anywherecommerce/services/exception/class-errorhandler.php","line":47,"class":"ErrorHandler","function":"handleWarning"}}\n'
    # res = pair2.match(s);
    # print res.group(1);
    # print "Line2:"
    # print res.group(2);
    # print re.findall(NameFile, res.group(2));
    # print "End"
    getErrorInfo();


if __name__ == '__main__':
    main()
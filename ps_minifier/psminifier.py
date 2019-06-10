import sys
import re
from itertools import product
import argparse

VAR_REGEX = "\$(?:[_a-zA-Z0-9]{2,}|[a-zA-Z0-9]+)"

MARKER_PREFIX = "/\\./\\"

AUTO_VARS = ["$true","$false","$$","$?","$^","$_","$args","$consolefilename","$error","$event","$eventargs","$eventsubscriber","$executioncontext","$foreach","$home","$host","$input","$iscoreclr","$islinux","$ismacos","$iswindows","$lastexitcode","$matches","$myinvocation","$nestedpromptlevel","$null","$pid","$profile","$psboundparametervalues","$pscmdlet","$pscommandpath","$psculture","$psdebugcontext","$pshome","$psitem","$psscriptroot","$pssenderinfo","$psuiculture","$psversiontable","$pwd","$sender","$shellid","$stacktrace","$switch","$this"]

def main(args=sys.argv, file=None):
    global variables, variable, var_count, chars

    if file != None: return_result = True
    else: return_result = False

    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="path to file to minify")
    parser.add_argument("-o", "--out-file", type=str, help="path to save the result")
    args = parser.parse_args(args[1:])
    if file == None:
        if args.file != None:
            with open(args.file, "r") as f:
                file = f.read()
        else:
            file = input()

    variable = "a"
    var_count = 0
    variables = [""]
    genVars()        

    str_locs, file = removeStrings(file)


    file = file.replace("\t", "    ")
    file = re.sub("( *|)=( *|)", "=", file)
    file = re.sub("( *|),( *|)", ",", file)
    file = re.sub(" *\( *", "(", file)
    file = re.sub(" *\) *", ")", file)
    file = re.sub(" *{ *", "{", file)
    file = re.sub(" *} *", "}", file)
    file = re.sub("({VR}|[0-9])( *|)\+( *|)({VR}|[0-9])".format(VR=VAR_REGEX), "\\1+\\4", file)
    file = re.sub("({VR}|[0-9])( *|)\-( *|)({VR}|[0-9])".format(VR=VAR_REGEX), "\\1-\\4", file)
    file = re.sub("({VR}|[0-9])( *|)/( *|)({VR}|[0-9])".format(VR=VAR_REGEX), "\\1/\\4", file)
    file = re.sub("({VR}|[0-9])( *|)\*( *|)({VR}|[0-9])".format(VR=VAR_REGEX), "\\1*\\4", file)
    file = re.sub("#.*$", "", file)
    file = re.sub("#.*\n", "\n", file)
    file = re.sub("\n *", "", file)


    done_vars = []
    found_vars = re.findall(VAR_REGEX, file)
    for i in str_locs:
        found_vars += [ii[1:] for ii in re.findall("[^`]"+VAR_REGEX, str_locs[i])]
    for i in found_vars:
        if i not in done_vars and i.lower() not in AUTO_VARS:
            new = "${}".format(getVar())
            file = re.sub(re.escape(i)+"(?![_a-zA-Z0-9])", new, file)
            for ii in str_locs:
                str_locs[ii] = re.sub("([^`])"+re.escape(i)+"(?![_a-zA-Z0-9])", "\\1"+new, str_locs[ii])
            done_vars.append(new)

    for i in str_locs:
        file = file.replace(i, str_locs[i])


    if not return_result:
        if args.out_file != None:
            with open(args.out_file, "w") as f:
                f.write(file)
        else:
            print("==RESULT==\n"+file)
    else:
        return file

def genVars():
    global variables
    length = len(variables[0])
    variables = []
    for i in product(*(["".join(chars)]*(length+1))):
        if "$"+"".join(i) not in AUTO_VARS: variables.append("".join(i))
def getVar():
    global variable, var_count
    var = variable
    if variables.index(variable) == len(variables)-1:
        genVars()
        var_count = 0
        variable = variables[var_count]
    else:
        var_count += 1
        variable = variables[var_count]
    return var

def removeStrings(file):
    # Returns a dictionary of markers and their strings
    # Returns file, but with the markers instead of the strings
    marker_count = 0
    strings = re.findall('".*"', file)
    str_locs = {}
    for i in strings:
        file = file.replace(i, MARKER_PREFIX.replace(".", str(marker_count)))
        str_locs[MARKER_PREFIX.replace(".", str(marker_count))] = i
        marker_count += 1
    return str_locs, file

if __name__ == "__main__":
    main()

#!/usr/bin/python2

import sys
import os

# def authorInformation():
#     fileName = "author.info"
#     if !os.path.exists(fileName):
#         return ""
#     file = open(fileName)
#     content = file.read()
#     file.close()
#     return content
# 
# def writeAuthorInformation(file):
#     content = authorInfomation()
#     if len(content) == 0:
#         return;
#     file.write("/*")
#     file.write(content)
#     file.write("*/")

def qtClasses():
    classes = [
            "QWindow",
           "QMainWindow",
           "QObject"
           ]
    return classes



def constructHeadFile(className):
    fileName = className + ".h"
    file = open(fileName, "w")
    #writeAuthorInformation(file)
    file.write("#ifndef __" + className.upper() + "__H\n")
    file.write("#define __" + className.upper() + "__H\n")
    file.write("\n")
    file.write("class " + className + "\n")
    file.write("{\n")
    file.write("    public:\n")
    file.write("        " + className + "();\n");
    file.write("        ~" + className + "();\n");
    file.write("};\n")
    file.write("#endif//__" + className.upper() + "__H\n")

def constructCppFile(className):
    fileName = className + ".cpp"
    file = open(fileName, "w")
    file.write("#include \"" + className + ".h\"")
    file.write("\n\n")
    file.write(className + "::" + className + "()\n");
    file.write("{\n}\n\n");
    file.write( className + "::~" + className + "()\n");
    file.write("{\n}\n");


def constructClass(className):
    constructHeadFile(className)
    constructCppFile(className)

def constructInheritedHeadFile(subclass, parent):
    fileName = subclass + ".h"
    file = open(fileName, "w")
    file.write("#ifndef __" + subclass.upper() + "__H\n")
    file.write("#define __" + subclass.upper() + "__H\n")
    file.write("\n")
    file.write("#include \"" + parent + ".h\"\n")
    file.write("\n")
    file.write("class " + subclass + "\n")
    file.write("{\n")
    file.write("\tpublic:\n")
    file.write("\t\t" + subclass + "();\n")
    file.write("\t\t~" + subclass + "();\n")
    file.write("};\n")
    file.write("\n")
    file.write("#endif//__" + subclass.upper() + "__H\n")

def constructInheritedCppFile(subclass, parent):
    fileName = subclass + ".cpp"
    file = open(fileName, "w")
    file.write("#include \"" + subclass + ".h\"\n")
    file.write("\n")
    file.write(subclass + "::" + subclass + "()\n")
    file.write("\t:" + parent + "()\n")
    file.write("{\n}\n\n")
    file.write(subclass + "::~" + subclass + "()\n")
    file.write("{\n}\n")

def constructInheritedClass(subclass, parent):
    constructInheritedHeadFile(subclass, parent)
    constructInheritedCppFile(subclass, parent)
    
def error():
    print "invalid arguemnts.\n"
    
def main():
    if len(sys.argv) == 2 :
        constructClass(sys.argv[1])
    elif len(sys.argv) == 3:
        constructInheritedClass(sys.argv[1], sys.argv[2])
    else:
        print error()

if __name__==("__main__"):
    main()

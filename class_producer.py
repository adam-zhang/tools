#!/bin/python2

import sys

def constructHeadFile(className):
    fileName = className + ".h"
    file = open(fileName, "w")
    file.write("#ifndef __" + className.upper() + "__H\n")
    file.write("#define __" + className.upper() + "__H\n")
    file.write("\n")
    file.write("class " + className + "\n")
    file.write("{\n")
    file.write("    public:\n")
    file.write("        " + className + "();\n");
    file.write("        ~" + className + "();\n");
    file.write("}\n")
    file.write("#endif//__" + className.upper() + "__H\n")

def constructCppFile(className):
    fileName = className + ".cpp"
    file = open(fileName, "w")
    file.write("#include \"" + className + "\".h")
    file.write("\n\n")
    file.write(className + "::" + className + "()\n");
    file.write("{\n}\n\n");
    file.write("~" + className + "::" + className + "()\n");
    file.write("{\n}\n");


def constructClass(className):
    constructHeadFile(className)
    constructCppFile(className)

def constructHeadFile(subclass, parent):
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
    file.write("}\n")
    file.write("\n")
    file.write("#endif//__" + subclass.upper() + "__H\n")

def constructCppFile(subclass, parent):
    fileName = subclass + ".cpp"
    file = open(fileName, "w")
    file.write("#include \"" + subclass + "\"\n")
    file.write("\n")
    file.write(subclass + "::" + subclass + "()\n")
    file.write("\t:" + parent + "()\n")
    file.write("{\n}\n\n")
    file.write(subclass + "::~" + subclass + "()\n")
    file.write("{\n}\n")

def constructInheritedClass(subclass, parent):
    constructHeadFile(subclass, parent)
    constructCppFile(subclass, parent)
    
def error():
    print "invalid arguemnts.\n"
    
def main():
    if len(sys.argv) == 2 :
        constructClass(sys.argv[1])
    if len(sys.argv) == 3:
        constructInheritedClass(sys.argv[1], sys.argv[2])
    else:
        print error()

if __name__==("__main__"):
    main()

import os
import sys

########################################################################
#   Original Implementation by Larry Kheriarty in 1978                 #
#   JavaScript and DHTML in 2006 by Hans Franke                        #
#   Written by Petar Jovanovic 2024                                    #
#   Special thanks to Tyler Zahnke                                     #
########################################################################

def Cls():
    os.system('cls');

def PrChar(c):
    print(c,end='')

def PrNL():
    print()

def GetChar():
    str = input('?');
    ch=str[0];
    return ch;

def Waduzitdo(source):
    Loc=0;
    End = len(source)-1;
    CBUF= " ";

    Acc=" ";
    Flg=" ";
    Last=0;

    while(Loc<End):
        CBUF=source[Loc]
        if(CBUF>"*"):
            if CBUF=="Y" or CBUF=="N" :
                if(CBUF!=Flg):
                    while Loc<End and CBUF!="\r" and CBUF!="\n":
                         Loc+=1
                         CBUF = source[Loc]
            elif CBUF=="A" :
                Acc = GetChar()
                Last=Loc
                Loc+=1

            elif CBUF=="M":
                Loc+=2
                Flg= "Y" if source[Loc]==Acc else "N"

            elif CBUF=="J":
                Loc+=2
                i=int(source[Loc])
                if i==0:
                    Loc = Last-1
                else:
                    while Loc<End and i>0:
                        if source[++Loc]=="*":
                            i-=1
            
            elif CBUF=="S":
                Loc=End

            elif CBUF=="T":
                Loc+=2
                CBUF=source[Loc]
                while Loc<End and CBUF!="\r" and CBUF!="\n":
                    PrChar(source[Loc])
                    Loc+=1
                    CBUF=source[Loc]
                PrNL()
            
            else:
                CBUF=source[Loc]
                while Loc<End and CBUF!="\r" and CBUF!="\n":
                    PrChar(source[Loc])
                    Loc+=1
                    CBUF=source[Loc]
                Loc-=1
                PrNL()
        Loc+=1

def editor():
    ret = ""
    print("Waduzitdoo-PY V 1.0.")
    print("<c> 2024-2030 JP Programi")
    print("Input commands. Type 'EOF' to run.")
    uns = ""
    while uns!="EOF":
        uns=input('>')
        if uns!="EOF":
            ret+=uns+"\n"
    return ret

def main():
    source = """T:,-------------,
T:| Hallo Welt! |
T:'-------------'
T:
T:Bitte 'A' eingeben
A:
M:A
YT:Danke
NT:Nö, so nicht
NJ:0
T:Ende
S:"""
    if len(sys.argv)>1:
        try:
            f=open(sys.argv[1])
            source = f.read()
            Waduzitdo(source)
        except:
            print("Error reading file. File is not presend and/or corrupt.")
    else:
        source = editor()
        Waduzitdo(source)

if __name__ == "__main__":
    main()
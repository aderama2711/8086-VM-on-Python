from i8086 import i8086
import sys, getopt

def main(argv):
    #initialize default
    files = './hello.emu'
    trace = True

    #initialize argument
    try:
        opts, args = getopt.getopt(argv,"hf:t:",["help","file=","trace="])
    except getopt.GetoptError:
        print ('use -h or --help for help')
        sys.exit(2)

    #checking argument
    for opt, arg in opts :
        if opt in ("-h", "--help") :
            print ("ez run for i8086 emulator by Ade\n-f [ --file ] arg\t\t: Run file (path-to-file, default : hello.emu)\n-t [ --trace ] arg\t\t: Turn trace on or off (1 or 0, default : 1)\n-h [ --help ]\t\t: Helppp!")
            sys.exit()
        elif opt in ("-f", "--file") :
            files = arg
        elif opt in ("-t", "--trace") :
            if(int(arg) == 1) :
                mode = True
            elif(int(arg) == 0) :
                mode = False
            else :
                print("Wrong option!")
                sys.exit(2)

    
    vm = i8086(trace)

    lines = []
    f = open(files, "r")
    for line in f.readlines():
        lines.append(line.split(' '))
    f.close()

    commands = [item.strip() for sublist in lines for item in sublist]
    print(commands)

    vm.run(commands,0)
    
#start main
if __name__ == "__main__":
   main(sys.argv[1:])
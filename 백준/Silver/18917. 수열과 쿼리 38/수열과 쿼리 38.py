import sys

def main():
    M = int(input())
    
    SUM = 0
    XOR = 0
    
    for _ in range(M):
        cmd = sys.stdin.readline()

        if (cmd[0] == '1'):
            arg = int(cmd[2:])
            XOR = XOR ^ arg
            SUM += arg

        elif (cmd[0] == '2'):
            arg = int(cmd[2:])
            SUM -= arg
            XOR = XOR ^ arg

        elif (cmd[0] == '3'):
            sys.stdout.write("%d\n" % SUM)

        else:
            sys.stdout.write("%d\n" % XOR)
                
main()
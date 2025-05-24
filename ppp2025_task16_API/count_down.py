import time

def countdown(n):
    for i in range(n, -1, -1):
        time.sleep(1)
        print(i, end = '\r')
    print("Bomb!")



def main():
   countdown(5)

if __name__ == "__main__":
    main()
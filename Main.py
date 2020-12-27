from Bacon import Bacon

def main():

    s = input("Here: ")
    cipherd = Bacon.encrypt(s)
    print(cipherd)
    print(Bacon.decrypt(cipherd))

if __name__ == '__main__':
    main()

import cs50
import sys


def main():

    if len(sys.argv) != 2 or int(sys.argv[1]) < 1:
        print("Usage: ./caesar k")
        return 1
    else:
        k = int(sys.argv[1])
        print("{}".format(k))

    k = k % 26

    print("plaintext: ", end="")
    inputString = cs50.get_string()


    for i in inputString:
        asciiCode = ord(i)
        j = 0

        #print(asciiCode)

        #if uppercase char
        if asciiCode >= 65 and asciiCode <= 90:
            #if go outside the bounds of uppercase chars in ASCII
            if (asciiCode + k) > 90:
                j = (asciiCode + k) - 26
            else:
                j = asciiCode + k
            print("{}".format(chr(j)), end="")

        #if lowercase char
        elif asciiCode >=97 and asciiCode <= 122:
            #if goes outside bounds of uppercase chars in ASCII
            if (asciiCode+k) > 122:
                j = (asciiCode + k) - 26
            else:
                j = k + asciiCode
            print("{}".format(chr(j)), end="")

        else:
            print("{}".format(i), end="")
    print("\n", end="")



if __name__ == "__main__":
    main()

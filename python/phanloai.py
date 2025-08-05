def main():
    tuoi = int(input("Nhap tuoi: "))
    gt = str(input("Nhap gioi tinh: "))
    match gt:
        case 'm' | 'M':
            if tuoi >=21: print("Loai 1")
            else: print("Loai 3")
        case 'f' | 'F':
            if tuoi >=21: print("Loai 2")
            else: print("Loai 4")
        case _: 
            print("I don't know why")

if __name__ == "__main__":
    main()
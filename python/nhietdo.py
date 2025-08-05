def main():
    doF=float(input("Nhap do K: "))
    doC=(doF-32)/1.8
    doK=doC+273.15
    print(f"Do C = {doC},  do K = {doK}")

if __name__ == "__main__":
    main()
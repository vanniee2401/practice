def main():
    PSI=float(input("Nhap so PSI: "))
    res=PSI*0.453592/(2.54**2)
    print(f"Doi sang kg/cm2 = {round(res,4)}")

if __name__ == "__main__":
    main()
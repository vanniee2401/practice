def main():
    c1=str(input("Nhap ki tu c1: "))
    c2=str(input("Nhap ki tu c2: "))
    x=int(input("Nhap x: "))
    print("Ma ASCII cua c1:", ord(c1))
    print("Ma ASCII cua c2:", ord(c2))
    print("Khoang cach giua c1 va c2:", abs(ord(c1)-ord(c2)))
    print("Dang viet hoa cua c1:", c1.upper())
    print("Ky tu co ma ASCII la", x, ":", chr(x))

if __name__ == "__main__":
    main()
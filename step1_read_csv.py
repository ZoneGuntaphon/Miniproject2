def main():
    # ใช้ with เพื่อให้ปิดไฟล์อัตโนมัติ
    with open("records.csv", "r", encoding="utf-8") as f:
        header = f.readline().strip()
        print("HEADER:", header)

        print("\nSAMPLE ROWS:")
        for i in range(5):                  # ลองอ่าน 5 แถวถัดจาก header
            line = f.readline()
            if not line:
                break                       # เจอ EOF ก็หยุด
            print(f"{i+1:>2}.", line.strip())

if __name__ == "__main__":
    main()
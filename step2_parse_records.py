def parse_row(line: str):
    """แปลง 1 บรรทัด (CSV) เป็น dict — ใช้ split แบบง่าย เพราะไฟล์นี้ไม่มี comma ในชื่อ"""
    parts = line.strip().split(",")
    # คาดหวังคอลัมน์: TG, Student ID, School, Name, Gender, CGPA
    tg, sid, school, name, gender, cgpa = parts[:6]
    return {
        "tutorial_group": parts[0],
        "student_id": parts[1],
        "school": parts[2],
        "name": parts[3],
        "gender": parts[4],
        "cgpa": float(parts[5])
    }

def read_records(path="records.csv"):
    students = []
    with open(path, "r", encoding="utf-8") as f:
        header = f.readline()           # ข้าม header
        for line in f:
            line = line.strip()
            if not line:
                continue
            students.append(parse_row(line))
    return students

def main():
    students = read_records("records.csv")
    print("Total records:", len(students))
    print("\nSample dicts (first 3):")
    for s in students[:3]:
        print(s)

if __name__ == "__main__":
    main()
# step3_group_by_tutorial.py
from step2_parse_records import read_records
import json

def group_by_tutorial(students):
    """รวมคนใน tutorial group เดียวกันไว้ด้วยกัน"""
    groups = {}  # dict ว่างไว้เก็บผลลัพธ์ เช่น {"G-1": [...], "G-2": [...]}

    for s in students:
        tg = s["tutorial_group"]       # กลุ่มของนักเรียนคนนี้ เช่น "G-1"
        if tg not in groups:           # ถ้ายังไม่เคยมี key นี้มาก่อน
            groups[tg] = []            # สร้าง list ว่างไว้
        groups[tg].append(s)           # เพิ่มนักเรียนคนนี้เข้า list ของกลุ่มนั้น

    return groups

def save_groups(groups):
    """เซฟผลลัพธ์แต่ละ tutorial group ลงไฟล์ JSON เพื่อให้เพื่อนเอาไปต่อได้"""
    with open("zone_groups.json", "w", encoding="utf-8") as f:
        sorted_groups = dict(sorted(groups.items(), key=lambda x: int(x[0].split('-')[1])))
        json.dump(sorted_groups, f, indent=4)

    print("✅ Saved all groups to zone_groups.json")

def main():
    students = read_records("records.csv")
    groups = group_by_tutorial(students)
    save_groups(groups)

    print("Number of tutorial groups:", len(groups))
    print("Example group: G-1")
    for s in groups["G-1"][:5]:        # แสดงนักเรียน 5 คนแรกของกลุ่ม G-1
        print(s["student_id"], s["name"], s["school"], s["cgpa"])

if __name__ == "__main__":
    main()
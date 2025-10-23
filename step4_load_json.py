import json

def load_groups(path="zone_groups.json"):
    """อ่านข้อมูลที่เซฟไว้ในไฟล์ JSON แล้วแปลงกลับมาเป็น dict"""
    with open(path, "r", encoding="utf-8") as f:
        groups = json.load(f)
    return groups


def show_group_summary(groups):
    """แสดงสรุปว่ามีกี่กลุ่ม และแต่ละกลุ่มมีนักเรียนกี่คน"""
    print("Number of tutorial groups:", len(groups))
    print("\nGroup summary:")
    for tg, members in groups.items():
        print(f"{tg}: {len(members)} students")


def main():
    groups = load_groups("zone_groups.json")
    show_group_summary(groups)

    # ถ้าอยากดูตัวอย่างข้อมูลของกลุ่ม G-1
    print("\nExample data from G-1:")
    for s in groups["G-1"][:3]:  # แสดง 3 คนแรกของ G-1
        print(s["student_id"], s["name"], s["cgpa"])


if __name__ == "__main__":
    main()
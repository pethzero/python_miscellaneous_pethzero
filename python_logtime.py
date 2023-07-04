from datetime import datetime, timedelta

def generate_schedule(start_date, end_date):
    start_time_1 = datetime.strptime("07:00:00", "%H:%M:%S").time()
    end_time_1 = datetime.strptime("18:00:00", "%H:%M:%S").time()
    start_time_2 = datetime.strptime("18:00:00", "%H:%M:%S").time()
    end_time_2 = datetime.strptime("23:59:59", "%H:%M:%S").time()

    current_date = start_date
    schedule = []

    while current_date <= end_date:
        current_time = start_time_1
        next_date = current_date

        while current_time <= end_time_1:
            schedule.append((len(schedule) + 1, current_date.day, current_time.strftime("%d/%m/%Y %H:%M:%S"), "1 T"))
            current_time = (datetime.combine(datetime.min, current_time) + timedelta(hours=11)).time()

        current_time = start_time_2
        next_date = current_date + timedelta(days=1)

        while current_time <= end_time_2:
            schedule.append((len(schedule) + 1, current_date.day, current_time.strftime("%d/%m/%Y %H:%M:%S"), "1 T"))
            current_time = (datetime.combine(datetime.min, current_time) + timedelta(hours=11)).time()

        current_date = next_date

    return schedule

# เรียกใช้ฟังก์ชัน generate_schedule() เพื่อสร้างตารางเวลา
start_date = datetime.strptime("01/01/2566", "%d/%m/%Y").date()
end_date = datetime.strptime("02/01/2566", "%d/%m/%Y").date()
schedule = generate_schedule(start_date, end_date)

# พิมพ์รายการตารางเวลา
for entry in schedule:
    print(entry)

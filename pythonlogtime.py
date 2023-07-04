from datetime import datetime, timedelta

def generate_data(start_date, end_date):
    data = []
    current_date = start_date
    # count = 1
    count = 63
    while current_date <= end_date:
        # data.append((count, 1, current_date.strftime('%d/%m/%Y %H:%M:%S'), '1 T'))
        data.append((count,2, current_date.strftime('%d/%m/%Y %H:%M:%S'), '1 T'))
        current_date += timedelta(hours=11) if current_date.hour < 18 else timedelta(hours=13)
        count += 1

    return data

start_date = datetime(2566, 1, 1, 7, 0, 0)
end_date = datetime(2566, 1, 31, 18, 0, 0)

result = generate_data(start_date, end_date)
    
for row in result:
    text = f"{row[0]}	     {row[1]}	             {row[2]}  {row[3]}"
    print("   "+text)


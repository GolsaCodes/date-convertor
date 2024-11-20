import random
import csv

# List of Persian months
persian_months = [
    "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
]

# Convert numbers to Persian text for days (1 to 31)
def convert_to_persian_text(number):
    words = {
        1: "یک", 2: "دو", 3: "سه", 4: "چهار", 5: "پنج",
        6: "شش", 7: "هفت", 8: "هشت", 9: "نه", 10: "ده",
        11: "یازده", 12: "دوازده", 13: "سیزده", 14: "چهارده",
        15: "پانزده", 16: "شانزده", 17: "هفده", 18: "هجده",
        19: "نوزده", 20: "بیست", 21: "بیست‌ و یک", 22: "بیست ‌و دو",
        23: "بیست‌ و سه", 24: "بیست‌ و چهار", 25: "بیست‌ و پنج",
        26: "بیست ‌و شش", 27: "بیست‌ و هفت", 28: "بیست‌ و هشت",
        29: "بیست‌ و نه", 30: "سی", 31: "سی‌ و یک"
    }
    return words.get(number, str(number))

def generate_informal_date(day, month, year):
    formats = [
        f"{day} {month} {year}",  # Numeric day, month, year
        f"{convert_to_persian_text(day)} {month} {year}",  # Persian text day
        f"{convert_to_persian_text(day)} {month} سال {year}",  # With "سال"
        f"{day} {month} سال {year}",  # Numeric day + "سال"
        f"{day} {month} ماه {year}",  # Month + " ماه" (with space)
        f"{convert_to_persian_text(day)} {month} ماه {year}",  # Persian text day + " ماه" (with space)
        f"روز {convert_to_persian_text(day)} {month} {year}",  # With "روز"
        f"روز {convert_to_persian_text(day)} {month} ماه {year}",  # With "روز" + " ماه" (with space)
        f"{year}.{persian_months.index(month) + 1}.{day:02d}",  # YYYY.MM.DD
    ]
    return random.choice(formats)


# Generate the dataset
def generate_dataset(num_samples=1000):
    dataset = []
    for _ in range(num_samples):
        year = random.randint(1300, 1450)
        month = random.choice(persian_months)
        day = random.randint(1, 31)
        # Ensure valid days for each month
        if month in ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "آبان", "آذر", "دی", "بهمن"] and day > 30:
            day = 30
        elif month == "اسفند" and day > 29:
            day = 29
        informal_date = generate_informal_date(day, month, year)
        formal_date = f"{year:04d}/{persian_months.index(month) + 1:02d}/{day:02d}"
        dataset.append((informal_date, formal_date))
    return dataset

# Save dataset to a CSV file
def save_dataset_to_csv(filename="persian_dates_dataset.csv", num_samples=1000):
    dataset = generate_dataset(num_samples)
    with open(filename, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Informal", "Formal"]) 
        writer.writerows(dataset)
    print(f"Dataset saved to {filename}")

# Generate and save the dataset
save_dataset_to_csv(num_samples=30000)

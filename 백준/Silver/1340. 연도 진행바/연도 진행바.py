from datetime import datetime


def convert_month_str_to_num(month_str):
    month_dict = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }

    return month_dict[month_str]


def year_progress_bar(year_time):
    month, dd, year, hh_mm = year_time.split()
    year, day = int(year), int(dd[:-1])
    hour, minute = list(map(int, hh_mm.split(":")))

    month = convert_month_str_to_num(month_str=month)

    total_year_datetime = datetime(year=year, month=12, day=31) - datetime(year=year - 1, month=12, day=31)
    input_year_datetime = datetime(year=year, month=month, day=day, hour=hour, minute=minute) - datetime(year=year,
                                                                                                         month=1, day=1)

    total_year_minute = total_year_datetime.days * 24 * 60
    input_year_minute = input_year_datetime.days * 24 * 60 + input_year_datetime.seconds // 60

    return input_year_minute / total_year_minute * 100


if __name__ == "__main__":
    year_time = input()
    print(year_progress_bar(year_time=year_time))
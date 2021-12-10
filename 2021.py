from time import time


loaded_successfully = []
failed_days = []
for day in range(1, 26):
    try:
        exec(f'from day_{day} import day_{day}')
        loaded_successfully.append(day)
    except ImportError:
        failed_days.append(day)

if failed_days:
    print(f'Warning: failed to load the following day{"s" if len(failed_days) > 1 else ""} {failed_days}')

start_time = time()
print(f'Advent Of Code 2021')
for day in loaded_successfully:
    day_start = time()
    print(f'  Day {day}: {eval(f"day_{day}()")} in {time() - day_start:.5f} seconds')
print(f'Total duration: {(time() - start_time) // 60:.0f} minutes, {(time() - start_time) % 60:.5f} seconds')

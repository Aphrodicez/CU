import time
import csv

def main():
    NUM_ITER = 50000
    timestamps = []
    start = time.perf_counter_ns()

    for i in range(NUM_ITER):
        now = time.perf_counter_ns()
        timestamps.append((i, (now - start) / 1e9))  # convert ns → seconds

    # Save after all iterations (avoid I/O in the loop)
    with open("cpu_timestamps.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["iteration", "elapsed_seconds"])
        writer.writerows(timestamps)

if __name__ == "__main__":
    main()

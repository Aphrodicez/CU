import pandas as pd
import matplotlib.pyplot as plt

def load_and_plot():
    files = {
        "EC2_t2micro_depleted": "cpu_timestamps_EC2_t2micro_depleted.csv",
        "EC2_t2micro_fresh": "cpu_timestamps_EC2_t2micro_fresh.csv",
        "Local_machine": "cpu_timestamps_Local_machine.csv"
    }

    plt.figure(figsize=(10,6))
    for label, file in files.items():
        df = pd.read_csv(file)
        plt.plot(df["iteration"], df["elapsed_seconds"], label=label)

    plt.title("CPU Performance Comparison")
    plt.xlabel("Iteration")
    plt.ylabel("Elapsed Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("cpu_comparison_plot.png")
    plt.show()

if __name__ == "__main__":
    load_and_plot()

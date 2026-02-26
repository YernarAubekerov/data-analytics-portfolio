import csv
import os

def generate_kpi_report(file_path):
    print(f"--- Train Loading KPI Report: {file_path} ---")
    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return

    print(f"{'Date':<12} | {'Train':<7} | {'Plan':<5} | {'Actual':<6} | {'%':<5} | Status")
    print("-" * 60)

    total_plan = 0
    total_actual = 0
    count = 0

    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            plan = int(row['plan_teu'])
            actual = int(row['actual_teu'])
            completion = (actual / plan) * 100

            total_plan += plan
            total_actual += actual
            count += 1

            status = "🟢 OK" if completion >= 90 else "🔴 ALERT"
            print(f"{row['date']:<12} | {row['train_id']:<7} | {plan:<5} | {actual:<6} | {completion:>4.1f}% | {status}")

    avg_completion = (total_actual / total_plan) * 100
    print("-" * 60)
    print(f"OVERALL PERFORMANCE: {avg_completion:.1f}%")
    print("-" * 40)

if __name__ == "__main__":
    generate_kpi_report("kpi-dashboard/data/mock_loading_data.csv")

import csv
import os

def analyze_containers(file_path):
    print(f"--- Analyzing CTMS Data: {file_path} ---")
    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return

    status_counts = {}
    damage_count = 0
    total_count = 0

    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_count += 1
            status = row['status']
            status_counts[status] = status_counts.get(status, 0) + 1
            if row['damage_type'].lower() != 'none':
                damage_count += 1

    print(f"Total Containers: {total_count}")
    print("\nStatus Distribution:")
    for status, count in status_counts.items():
        print(f"  - {status}: {count} ({count/total_count*100:.1f}%)")

    damage_rate = (damage_count / total_count) * 100
    print(f"\nDamage Rate: {damage_rate:.1f}%")
    print("-" * 40)

if __name__ == "__main__":
    analyze_containers("ctms-analysis/data/mock_containers.csv")

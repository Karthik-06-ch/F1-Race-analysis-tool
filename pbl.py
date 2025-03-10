import pandas as pd
import matplotlib.pyplot as plt
def get_input_data():
    data = []
    num_drivers = int(input("Enter the number of drivers: "))
    
    for _ in range(num_drivers):
        driver_name = input("Enter the driver's name: ")
        num_laps = int(input(f"Enter the number of laps for {driver_name}: "))
        
        for lap in range(1, num_laps + 1):
            lap_time = float(input(f"Enter lap time for {driver_name} (Lap {lap}): "))
            data.append({'driver': driver_name, 'lap': lap, 'lap_time': lap_time})
    
    return pd.DataFrame(data)
def clean_data(data):
    data_clean = data.dropna()
    data_clean['lap_time'] = pd.to_numeric(data_clean['lap_time'], errors='coerce')
    print("Data cleaned successfully.")
    return data_clean
def calculate_average_lap_times(data_clean):
    average_lap_times = data_clean.groupby('driver')['lap_time'].mean()
    print("\nAverage Lap Times:")
    print(average_lap_times)
    return average_lap_times
def plot_lap_times(data_clean):
    drivers = data_clean['driver'].unique()
    for driver in drivers:
        driver_data = data_clean[data_clean['driver'] == driver]
        plt.plot(driver_data['lap'], driver_data['lap_time'], label=driver)
    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (seconds)')
    plt.title('Lap Times for Each Driver')
    plt.legend()
    plt.show()
def generate_summary_report(driver, data_clean):
    driver_data = data_clean[data_clean['driver'] == driver]
    total_laps = driver_data['lap'].count()
    avg_lap_time = driver_data['lap_time'].mean()
    best_lap_time = driver_data['lap_time'].min()
    worst_lap_time = driver_data['lap_time'].max()
    report = f"""
    Summary Report for {driver}:
    Total Laps: {total_laps}
    Average Lap Time: {avg_lap_time:.2f} seconds
    Best Lap Time: {best_lap_time:.2f} seconds
    Worst Lap Time: {worst_lap_time:.2f} seconds
    """
    print(report)
def main():
    data = get_input_data()
    data_clean = clean_data(data)
    average_lap_times = calculate_average_lap_times(data_clean)
    plot_lap_times(data_clean)
    drivers = data_clean['driver'].unique()
    for driver in drivers:
        generate_summary_report(driver, data_clean)
if __name__ == "__main__":
    main()

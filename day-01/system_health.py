import psutil  # Importing the psutil module

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU threshold: "))  # Taking threshold input from user
    
    current_cpu = psutil.cpu_percent(interval=1)  # Getting current CPU usage
    
    if current_cpu > cpu_threshold:  # Checking if CPU usage exceeds threshold
        print(f"CPU usage is high: {current_cpu}% > {cpu_threshold}% + Alerting the team via email...")
    else:
        print(f"CPU usage is normal: {current_cpu}% <= {cpu_threshold}%")


if __name__ == "__main__":
    check_cpu_threshold()


import speedtest
import os
import psutil

def test_speed():
    st = speedtest.Speedtest()
    print("Testing download speed...")
    dl_speed = st.download()
    print(f"Download speed: {dl_speed / 1024 / 1024:.2f} Mbps")
    print("Testing upload speed...")
    ul_speed = st.upload()
    print(f"Upload speed: {ul_speed / 1024 / 1024:.2f} Mbps")
    servernames = []
    st.get_servers(servernames)
    print("Testing ping...")
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")


def check_usage(limit, bytes_sent_start, bytes_recv_start):
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    mb_sent = (bytes_sent - bytes_sent_start) / 1024 / 1024
    mb_recv = (bytes_recv - bytes_recv_start) / 1024 / 1024
    total_usage = mb_sent + mb_recv
    print(f"Data sent: {mb_sent:.2f} MB")
    print(f"Data received: {mb_recv:.2f} MB")
    print(f"Total usage: {total_usage:.2f} MB")
    if total_usage > limit:
        print("Warning: Network usage limit exceeded")

def menu():
    # Get network usage at the start
    net_io_counters = psutil.net_io_counters()
    bytes_sent_start = net_io_counters.bytes_sent
    bytes_recv_start = net_io_counters.bytes_recv
    
    limit = float(input("Enter network usage limit (in MB): "))
    while True:
        print("\nNetwork Usage Tracker")
        print("---------------------")
        print("Limit: " + str(limit) + " MB")
        print("\n1. Test upload speed, download speed and ping")
        print("2. Change the limit entered earlier")
        print("3. Check network usage in this session")
        print("4. Exit\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            test_speed()
        elif choice == '2':
            limit = float(input("Enter network usage limit (in MB): "))
        elif choice == '3':
            check_usage(limit, bytes_sent_start, bytes_recv_start)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    menu()
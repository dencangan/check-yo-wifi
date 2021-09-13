import os
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Wifi windows commands
WIFI_NAME_CMD = """powershell -Command "& {(netsh wlan show interfaces) -Match '^\s+Profile' -Replace '^\s+Profile\s+:\s+',''"}"""
WIFI_SIGNAL_CMD = """powershell -Command "& {(netsh wlan show interfaces) -Match '^\s+Signal' -Replace '^\s+Signal\s+:\s+',''"}"""
WIFI_RECEIVE_CMD = """powershell -Command "& {(netsh wlan show interfaces) -Match '^\s+Receive' -Replace '^\s+Receive\s+:\s+',''"}"""
WIFI_TRANSMIT_CMD = """powershell -Command "& {(netsh wlan show interfaces) -Match '^\s+Transmit' -Replace '^\s+Transmit\s+:\s+',''"}"""


def record_data(
        cmd: str,
        record_time: int,
        intervals: int = 1) -> tuple:
    """
    Records data specified by input windows cmd commands.
    :param cmd: Windows command to retrieve data.
    :param record_time: How long to record for.
    :param intervals: Configure sleep before next iteration is called, defaults at 1 second.
    :return: Tuple of required data for plotting.
    """
    wifi_name = os.popen(WIFI_NAME_CMD).read().replace(' \n', '')
    t1 = time.time()
    results, time_of_record = [], []
    print(f"Recording WiFi signal for '{wifi_name}' for {record_time}s...")
    time_start = datetime.now()
    for i in range(record_time):
        data = os.popen(cmd).read()
        data = int(data.replace(' \n', '').replace('%', ''))
        results.append(data), time_of_record.append(datetime.now())
        time.sleep(intervals)
    time_end = datetime.now()
    print(f"WiFi recording complete. Took: {time.time() - t1}")
    return results, time_of_record, time_start, time_end, wifi_name


if __name__ == '__main__':
    RECORD_TIME = 240
    x, t, ts, te, wf_name = record_data(record_time=RECORD_TIME, cmd=WIFI_SIGNAL_CMD)
    plt.title(wf_name)
    plt.ylabel('Wifi Strength %')
    plt.ylim(0, 100)
    plt.xlabel('Time')
    plt.xlim(ts, te)
    plt.plot(t, x)
    plt.legend(["Received Mbps"])

    #
    # plt.title(wf_name)
    # plt.ylabel('Wifi Strength %')
    # plt.ylim(0, 100)
    # plt.xlabel('Time')
    # plt.xlim(ts, te)
    # plt.plot(t, x)
    # plt.legend(["Signal"])

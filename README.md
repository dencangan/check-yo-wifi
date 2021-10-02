# Check Yo WiFi

I got frustrated at the instability of the WiFi signal at my place. 
This program helps track your WiFi signal over a period of time and plots a chart to show you how 
it performed.

An option to track receive and transmit data in Mbps is also available. Here is an example chart of my flaky annoying WiFi:

![wifi_chart](Figure_1.png)


## Windows 10
Uses powershell commands to record signal and plots a line graph. Record time argument in seconds. 
See 'wifiSignalWin10.py' file. There are also commands to track 'Transmit/Receive (mbps)' rate too. 

## MacOs
Records WiFi signal in dBm values and output grep to a txt file.

On terminal<br>
1. `$ chmod +x wifiSignalMacOS`<br>
2. `./wifiSignalMacOS`<br>
3. `Enter input integer (seconds).`

Some other features to add in the future:
- Add moving average.
- Parse MacOS txt output to support plotting too.
- To add Linux support soon.
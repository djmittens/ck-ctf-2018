# Country(50):  Czech Republic
----------
Description:  Imagine you join our Security Operations team and on your first day your assigned buddy gets paged about a particular Trojan Horse being loaded on an Employee's laptop. The alert has this information:

Type of attack: Crime
Family: USteal.D
Malware type: Trojan

“Trojan horse is a program in which malicious or harmful code is contained inside apparently harmless programming or data in such a way that it can get control and do its chosen form of damage.” 

Most of the anti-viruses detect it as TrojanSpy:Win32/Usteal.D. 

You reach out to that person for more information and you take their corptop and capture a pcap to investigate what's happening. In this case you find out that the Trojan generated continues to remain as a backdoor. The generated Trojan is mainly used to steal stored passwords from various web browsers, FTP clients and IRC’s.

Your buddy asks you to confirm the MAC address of the server. Analyze the PCAP file to get the MAC address of the server/destination. You can find the file here: https://code.corp.creditkarma.com/ck-private/sec_capture-the-flag/blob/master/Trojan%20Capture/BIN_UStealD_2b796f11f15e8c73f8f69180cf74b39d.pcap

[You can use Wireshark if you have Kali installed or already have it on your machine otherwise you can use https://packettotal.com/]
----------
Hint:  Checked DHCP logs?
----------
Attachments:  []
~!|----------|!~


I solved this one by using tshark(command line version of wireshark).
there were a total of 3 mac's in the pcap, and i just tried all 3 of them.
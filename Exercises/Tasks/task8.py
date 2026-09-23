import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 24 * 60, 5)

# 3 servers

cpu1 = np.random.normal(60, 10, 288)
cpu2 = np.random.normal(65, 10, 288)
cpu3 = np.random.normal(70, 10, 288)

memory1 = np.random.normal(55, 8, 288)
memory2 = np.random.normal(60, 8, 288)
memory3 = np.random.normal(65, 8, 288)

network1 = np.random.normal(50, 15, 288)
network2 = np.random.normal(55, 15, 288)
network3 = np.random.normal(60, 15, 288)

# keeping values between 0 and 100
cpu1 = np.clip(cpu1, 0, 100)
cpu2 = np.clip(cpu2, 0, 100)
cpu3 = np.clip(cpu3, 0, 100)

memory1 = np.clip(memory1, 0, 100)
memory2 = np.clip(memory2, 0, 100)
memory3 = np.clip(memory3, 0, 100)

network1 = np.clip(network1, 0, 100)
network2 = np.clip(network2, 0, 100)
network3 = np.clip(network3, 0, 100)

#some critical values
cpu1[50] = 98
cpu2[120] = 97
memory3[180] = 96

# 3*1 grid
fig, (c1, c2, c3) = plt.subplots(3,1,figsize=(12,12))

# for cpu
c1.plot(time, cpu1, label="Server 1")
c1.plot(time, cpu2, label="Server 2")
c1.plot(time, cpu3, label="Server 3")

c1.axhline(80, linestyle='--', label="Warning 80%",alpha = 0.6,color ='red')
c1.axhline(95, linestyle='--', label="Critical 95%", color='red')
c1.fill_between(time, 95, 100, alpha=0.4, color = 'red')

for i in range(288):
    if cpu1[i] >= 95:
        c1.annotate(f"{time[i]//60:.0f}:{time[i]%60:02.0f}", (time[i], cpu1[i]))
    if cpu2[i] >= 95:
        c1.annotate(f"{time[i]//60:.0f}:{time[i]%60:02.0f}", (time[i], cpu2[i]))
    if cpu3[i] >= 95:
        c1.annotate(f"{time[i]//60:.0f}:{time[i]%60:02.0f}", (time[i], cpu3[i]))

c1.set_title("CPU Usage")
c1.set_ylabel("CPU %")
c1.legend()


# for memory
c2.plot(time, memory1, label="Server 1")
c2.plot(time, memory2, label="Server 2")
c2.plot(time, memory3, label="Server 3")

c2.axhline(80, linestyle='--', label="Warning 80%",alpha = 0.6,color ='red')
c2.axhline(95, linestyle='--', label="Critical 95%",color='red')
c2.fill_between(time, 95, 100, alpha=0.4, color = 'red')

for i in range(288):
    if memory1[i] >= 95:
        c2.annotate(f"{time[i]//60:.0f}:{time[i]%60:02.0f}", (time[i], memory1[i]))
    if memory2[i] >= 95:
        c2.annotate(f"{time[i]//60:.0f}:{time[i]%60:02.0f}", (time[i], memory2[i]))
    if memory3[i] >= 95:
        c2.annotate(f"{time[i]//60:.0f}:{time[i]%60:02.0f}", (time[i], memory3[i]))

c2.set_title("Memory Usage")
c2.set_ylabel("Memory %")
c2.legend()


# for network
c3.plot(time, network1, label="Server 1")
c3.plot(time, network2, label="Server 2")
c3.plot(time, network3, label="Server 3")

c3.set_title("Network I/O")
c3.set_xlabel("Time (minutes)")
c3.set_ylabel("Network I/O")
c3.legend()

plt.suptitle("System Health Dashboard")
plt.savefig('system_health_dashboard.png')
plt.show()
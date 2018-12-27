# author: tangxi
# time:2018-12-27
# plot
import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


x = np.arange(1,15,1)
print(x)
train_acc = np.array([0.7127,0.8308,0.8521,0.8672,0.8842,0.9005,0.9041,0.9098,0.9210 ,0.9279 ,0.9320 ,0.9380,0.9410 ,0.9505])
train_loss = np.array([0.5816,0.3911,0.3632,0.3278,0.3016,0.2571,0.2365,0.2206,0.1995,0.1790,0.1644,0.1531,0.1433])
val_acc = np.array([0.8423,0.8288,0.8656,0.8601,0.8648,0.8906,0.8950,0.8882,0.8862,0.8914,0.8894,0.8851,0.8740,0.8843])
val_loss = np.array([0.3633,0.4033,0.3262,0.3345,0.3261,0.2712,0.2565,0.2544,0.2703,0.2807, 0.2955 ,0.2987,0.3114,0.2931])

plt.figure(figsize=(8,4))
plt.plot(x,train_acc,label = "$train_acc$",color = "red",linewidth = 2)
plt.plot(x,val_acc,  label = "$val_acc$",color = "green",linewidth = 2)
plt.xlabel("epoch")
plt.ylabel("acc")
plt.title("acc-epoch")
plt.ylim(0.8,1)
plt.legend()
plt.show()

plt.figure(figsize=(8,4))
plt.plot(x,train_loss,label = "$train_loss$",color = "red",linewidth = 2)
plt.plot(x,val_loss,  label = "$val_loss$",color = "green",linewidth = 2)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("loss-epoch")
plt.ylim(0,0.5)
plt.legend()
plt.show()
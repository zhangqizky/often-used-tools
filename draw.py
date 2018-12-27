# author: tangxi
# time:2018-12-27
# plot
import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


x = np.arange(1,11,1)
print(x)
train_acc = np.array([0.8095,0.8754,0.8941,0.9061,0.9077,0.9095,0.9149,0.9172,0.9187,0.9197])
train_loss = np.array([0.4468,0.3181,0.2673,0.2423,0.2335,0.2196,0.2145,0.2043,0.2071,0.1968])
val_acc = np.array([0.8553,0.8288,0.8890,0.8744,0.8966,0.8977,0.8989,0.8954,0.8989,0.8922])
val_loss = np.array([0.3498,0.4170,0.2595,0.3263,0.2566,0.2624,0.2465,0.3222,0.3087,0.3610,])

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
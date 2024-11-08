import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Duration of the animation
t0=0 # [s]
t_end=10 # [s]
dt=0.02 # [s]

# Create array for time
t=np.arange(t0,t_end+dt,dt)
y=1000*t


frame_amount=len(t)

def update_plot(t):
    print(t)
    wire_1.set_data([-160,0],[-100,1000*t])
    wire_2.set_data([160,0],[-100,1000*t])
    y_text.set_text('y = '+str(int(1000*t))+' mm')

    return wire_1,wire_2,y_text

# Define figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(4,4)
plt.subplots_adjust(left=0.03,bottom=0.035,right=0.99,top=0.97,wspace=0.15,hspace=0.2)
ax=fig.add_subplot(gs[:,0:4],facecolor=(0.9,0.9,0.9))

wire_1,=ax.plot([],[],'k',linewidth=2)
wire_2,=ax.plot([],[],'k',linewidth=2)
plate_A=ax.plot([-50,50],[-200,-200],'g',linewidth=200)

box_object=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='r',lw=1)
y_text=ax.text(400,250,'',size=20,color='r',bbox=box_object)

plt.xlim(-600,600)
plt.ylim(-300,300)
plt.xlabel('x-length [mm]',fontsize=12)
plt.ylabel('y-length [mm]',fontsize=12)
plt.grid()


engine_ani=animation.FuncAnimation(fig,update_plot,
    frames=t,interval=20,repeat=False,blit=True)
plt.show()
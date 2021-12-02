import os
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import time
listt = os.listdir(os.getcwd()[:47] + 'Imagens/')
start = time.time()
fig = plt.figure()
im = []
plt.axis(False)
aux = True
for i in range(len(listt)):
    im.append([plt.imshow(plt.imread(os.getcwd()[:47] + 'Imagens/' + str(i) + '.png'))])
    if aux:
        stop = time.time()
        print((stop-start) * len(listt) / 60)
        aux = False

    

anim = ArtistAnimation(fig, im, interval=20)
anim.save(os.getcwd()[:47] + 'Simulação.gif', fps = 10)
plt.show()
plt.close()

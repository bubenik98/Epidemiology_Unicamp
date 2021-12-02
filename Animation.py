import os
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
listt = os.listdir(os.getcwd()[:47] + 'Imagens/')

fig = plt.figure()
im = []
plt.axis(False)
for i in range(len(listt)):
    im.append([plt.imshow(plt.imread(os.getcwd()[:47] + 'Imagens/' + str(i) + '.png'))])
    

anim = ArtistAnimation(fig, im)#, interval=75)
plt.show()
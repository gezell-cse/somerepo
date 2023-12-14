#!/usr/bin/env python
# coding: utf-8

# In[146]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

#DAISY FUNCTION
def xmas_surprise():
    def draw_daisy(ax, x_offset, y_offset, scale):
        # Draw the flower head
        ax.add_patch(plt.Circle((x_offset, y_offset), 0.4 * scale, color='yellow', ec='black'))
        # Draw petals
        num_petals = 12
        for i in range(num_petals):
            angle = i * (360 / num_petals)
            x = x_offset + 0.6 * np.cos(np.radians(angle)) * scale
            y = y_offset + 0.6 * np.sin(np.radians(angle)) * scale
            ax.add_patch(patches.Ellipse((x, y), 0.8 * scale, 0.4 * scale, angle=angle, color='white', ec='black'))

    #SETUP
    fig, ax = plt.subplots(figsize=(10, 8))
    theta = np.linspace(0, 2 * np.pi, 100)

    #HEART
    x_heart = 16 * (np.sin(theta) ** 3)
    y_heart = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)
    for i, scale in enumerate(range(1, 201, 1)):
        plt.plot(2 * scale * x_heart, 2 * scale * y_heart, color="#FF5252", zorder=2.0)

    for x in range(0,360, 45):
        draw_daisy(ax, x_offset=7500*math.cos(x*math.pi/180), y_offset=7500*math.sin(x*math.pi/180), scale=2000)

    for x in range(0,360, 45):
        draw_daisy(ax, x_offset=7000*math.cos((x+15)*math.pi/180), y_offset=7000*math.sin((x+15)*math.pi/180), scale=2000)

    ax.set_xlim([-11000, 11000])
    ax.set_ylim([-11000, 11000])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    print("🎄 MERRY CHRISTMAS 🎄")

    plt.show()
    
xmas_surprise()


# In[ ]:





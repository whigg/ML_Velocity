''' Helper functions for various scripts
    Created Sept 21, 2018
    Bidhya N Yadav

    Functions:
'''
def tic():
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    toc_str = "Toc: start time not set, call tic() first" #default message
    if 'startTime_for_tictoc' in globals():
        elasped_time = time.time() - startTime_for_tictoc
        if elasped_time <= 60.0:
            toc_str = "Elapsed time is {:.3f} seconds.".format(elasped_time)
        elif elasped_time <= 3600.0:
            elasped_time /= 60.0
            toc_str = "Elapsed time is {:.2f} minutes.".format(elasped_time)
        else:
            elasped_time /= 3600.0
            toc_str = "Elapsed time is {:.2f} hours.".format(elasped_time)
    print(toc_str)
    return toc_str #so we can pass it to logging etc


def add_osgb_scalebar(ax, at_x=(0.1, 0.4), at_y=(0.05, 0.075), max_stripes=5):
    """
    Add a scalebar to a GeoAxes of type cartopy.crs.OSGB (only).

    Args:
    * at_x : (float, float)
        target axes X coordinates (0..1) of box (= left, right)
    * at_y : (float, float)
        axes Y coordinates (0..1) of box (= lower, upper)
    * max_stripes
        typical/maximum number of black+white regions
    """
    # ensure axis is an OSGB map (meaning coords are just metres)
    # assert isinstance(ax.projection, ccrs.OSGB)
    # fetch axes coordinate mins+maxes
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as mfonts
    
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    # set target rectangle in-visible-area (aka 'Axes') coordinates
    ax0, ax1 = at_x
    ay0, ay1 = at_y
    # choose exact X points as sensible grid ticks with Axis 'ticker' helper
    x_targets = [x0 + ax * (x1 - x0) for ax in (ax0, ax1)]
    ll = mpl.ticker.MaxNLocator(nbins=max_stripes, steps=[1,2,4,5,10])
    x_vals = ll.tick_values(*x_targets)
    # grab min+max for limits
    xl0, xl1 = x_vals[0], x_vals[-1]
    # calculate Axes Y coordinates of box top+bottom
    yl0, yl1 = [y0 + ay * (y1 - y0) for ay in [ay0, ay1]]
    # calculate Axes Y distance of ticks + label margins
    y_margin = (yl1-yl0)*0.25

    # fill black/white 'stripes' and draw their boundaries
    fill_colors = ['black', 'white']
    i_color = 0
    for xi0, xi1 in zip(x_vals[:-1],x_vals[1:]):
        # fill region
        plt.fill((xi0, xi1, xi1, xi0, xi0), (yl0, yl0, yl1, yl1, yl0),
                 fill_colors[i_color])
        # draw boundary
        plt.plot((xi0, xi1, xi1, xi0, xi0), (yl0, yl0, yl1, yl1, yl0),
                 'black')
        i_color = 1 - i_color

    # add short tick lines
    for x in x_vals:
        plt.plot((x, x), (yl0, yl0-y_margin), 'black')

    # add a scale legend 'Km'
    font_props = mfonts.FontProperties(size='medium', weight='bold')
    plt.text(
        0.5 * (xl0 + xl1),
        yl1 + y_margin,
        'Km',
        verticalalignment='bottom',
        horizontalalignment='center',
        fontproperties=font_props)

    # add numeric labels
    for x in x_vals:
        plt.text(x,
                 yl0 - 2 * y_margin,
                 '{:g}'.format((x - xl0) * 0.001),
                 verticalalignment='top',
                 horizontalalignment='center',
                 fontproperties=font_props)        

if __name__ == "__main__":
    print("Some helper functions")
    tic()
    toc()
    

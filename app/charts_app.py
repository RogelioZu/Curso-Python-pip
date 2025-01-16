import matplotlib.pyplot as plot

def generate_bar_chart(name, labels, values):

    fig, ax  = plot.subplots()
    ax.bar(labels,values)
    plot.savefig(f'app/images/{name}.png')
    plot.close()    


def generate_pie_chart(name, labels, values):

    fig, ax = plot.subplots()
    ax.pie(values , labels = labels)
    ax.axis('equal')
    plot.savefig(f'app/images/{name}.png')
    plot.close()
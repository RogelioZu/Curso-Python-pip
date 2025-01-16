import matplotlib.pyplot as pylot



def generarte_pie_chart():

    labels = ['A', 'B', 'C']
    values = [100,250,600]

    fig, ax = pylot.subplots()
    ax.pie(values,labels=labels)
    pylot.savefig('pie.png')
    pylot.close()

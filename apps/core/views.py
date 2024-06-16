import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from io import BytesIO
import base64


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    data = {}
    data['user'] = request.user
    return render(request, 'core/index.html', data)

def bar_chart_view(request):
    # Example data
    data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [23, 45, 56, 78]}
    df = pd.DataFrame(data)
    
    # Plotting the bar chart
    plt.figure(figsize=(10,5))
    df.plot(kind='bar', x='Category', y='Values', legend=False)
    plt.title('Bar Chart Example')
    plt.xlabel('Category')
    plt.ylabel('Values')

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64 to pass it to the template
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {'graphic': graphic}
    return render(request, 'core/index.html', context)





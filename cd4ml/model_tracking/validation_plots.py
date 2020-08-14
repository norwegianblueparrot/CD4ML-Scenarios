from bokeh.plotting import figure


def get_validation_plot(true_value, prediction):
    x_min = min(min(true_value), min(prediction))
    x_max = max(max(true_value), max(prediction))

    x_range = [x_min, x_max]
    y_range = x_range

    plot = figure(width=800, height=800,
                  x_range=x_range, y_range=y_range)

    plot.xaxis.axis_label = "True value"
    plot.xaxis.axis_label_text_font_size = '14pt'
    plot.xaxis.major_label_text_font_size = '12pt'

    plot.yaxis.axis_label = "Prediction"
    plot.yaxis.axis_label_text_font_size = '14pt'
    plot.yaxis.major_label_text_font_size = '12pt'

    plot.circle(true_value, prediction)

    plot.line(x_range, y_range, line_dash='dashed', color='gray')

    return plot


def make_validation_plot(true_value, prediction):
    return get_validation_plot(true_value, prediction)
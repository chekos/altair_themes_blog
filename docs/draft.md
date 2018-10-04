# Consistently beautiful visualizations with `altair` themes

If you are a data visualization fan or practitioner that also uses `python` you may have heard of Jake Vanderplas and Brian Granger's `altair`: _"a declarative statistical visualization library for Python, based on Vega and Vega-lite"_.

> _With Altair, you can spend more time understanding your data and its meaning. Altair’s API is simple, friendly and consistent and built on top of the powerful Vega-Lite visualization grammar. This elegant simplicity produces beautiful and effective visualizations with a minimal amount of code._

If you haven't, you should check out Jake Vanderplas' 2018 PyCon tutorial: https://www.youtube.com/watch?v=ms29ZPUKxbU

***
In this piece we'll be digging deeper into one of `altair`'s less known features: themes. 

### What are `altair` themes?

A theme, in `altair`, is a set of chart configurations applied globally each `python` session. This means you can produce similar-looking visualizations consistently. 

### Why would that be useful?

Maybe you are working on developing a personal style for your blog or maybe you are part of a company that already has a style in place or maybe you hate gridlines and are tired of turning them off every single time you create a chart. 
Having a styleguide to follow is always a benefit when you are producing data visualizations. 

Rather than explaining the value of styleguides and consistency in your visualizations, in this article we will explore how to implement one in `altair` by coding the [Urban Institute's Data Visualization Styleguide](http://urbaninstitute.github.io/graphics-styleguide/). 

### Themes in `altair`

> _A theme is simply a function that returns a dictionary of default values to be added to the chart specification at rendering time, which is then registered and activated._

Here's a simple example from the docs:
```python
import altair as alt
from vega_datasets import data

# define the theme by returning the dictionary of configurations
def black_marks():
    return {
        'config': {
            'view': {
                'height': 300,
                'width': 400,
            },
            'mark': {
                'color': 'black',
                'fill': 'black'
            }
        }
    }

# register the custom theme under a chosen name
alt.themes.register('black_marks', black_marks)

# enable the newly registered theme
alt.themes.enable('black_marks')

# draw the chart
cars = data.cars.url
alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)
```

`height` and `width` remained the same as the default theme but we have now included `color` and `fill` values to be applied __globally__ (unless otherwise specified) to any charts generated from this point until the end of __this__ `python` session.

This would be the equivalent of 
```python
alt.Chart(cars).mark_point(color = 'black', fill = 'black').encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)
```
![FIG 2](../images/figures/figure-1.png)

in the `black_marks` `config` dictionary returned you can see that we specified the value `black` for the keys `color` and `fill` in `mark`. This is the format all these specifications follow. For example, if you wanted to configure the left axis' label's font size:
```python
def my_theme():
    return {
        'config': {
            'view': {
                'height': 300,
                'width': 400,
            },
            'mark': {
                'color': 'black',
                'fill': '#000000',
            },
            'axisLeft': {
                'labelFontSize': 30,
            },
        }
    }

# register the custom theme under a chosen name
alt.themes.register('my_theme', my_theme)

# enable the newly registered theme
alt.themes.enable('my_theme')
```
![FIG 2](../images/figures/figure-2.png)

(side note: you can get these ___specifications___ (i.e. `'axisLeft'`) from [Vega-Lite's documentation](https://vega.github.io/vega-lite/docs/config.html.)

This can be particularly useful if you or your company have a styleguide you have to follow. 
If you don't have a styleguide you can start building one by saving your configurations on your personal theme rather than in your viz code (it pays off long-term!).

Vega already has some [themes on GitHub](https://github.com/vega/vega-themes/tree/master/src).

#### fivethirtyeight
![FIG 538](../images/figures/fivethirtyeight.png)
#### excel
![FIG excel](../images/figures/excel.png)
#### ggplot2
![FIG ggplot2](../images/figures/ggplot2.png)
#### vox
![FIG vox](../images/figures/vox.png)
***

All the information for this ___simplified___ version of Urban Institute's style can be found in this graphic from their GitHub page.

![urban_chart-parts](../images/figures/urban_chart-parts-02.png)

***

So let's build a simplified Urban Institute's `altair` theme.

The basic anatomy of the theme is as follows:

```python
def theme_name():
    
    return {
        "config": { 
            "TOPLEVELOBJECT": { # i.e. "title", "axisX", "legend",
                "CONFIGURATION": "VALUE",
                "ANOTHER_ONE": "ANOTHER_VALUE",
                "MAYBE_A_SIZE": 14, # values can be a string, boolean, or number,
            },
            "ANOTHER_OBJECT": {
                "CONFIGURATION": "VALUE",
            }
        }
    }
```

We will configure the top-level objects "title", "axisX", "axisY", "range", and "legend", plus a few other one-liner specifications. ("range" would be the color-scheme)

Now, off the bat we saw that Urban uses the "Lato" font on all text so we can save that as a variable so we don't have to reuse it. 

1. "title"

Titles at Urban are 18px in size, Lato font, left-aligned, black.

```python
def urban_theme():
    font = "Lato"
    
    return {
        "config": {
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "fontColor": "#000000"
            }
        }
    }
```

At this point you could _register_ and _enable_ this theme and all your `altair` charts in this `python` session would have an Urban-Institute-looking title.

#### SIDE-NOTE
If you do not have "Lato" font installed in your computer you can run this code in a cell to import it to your browser from Google Fonts for the time being.
```python
%%html
<style>
@import url('https://fonts.googleapis.com/css?family=Lato');
</style>
```


2. "axisX" and "axisY"

At Urban the X-axis and Y-axis differ slightly. X-axes have what in `altair` is referred to as _domain_, the line that runs across the axis. Y-axes do not have this (similar to `seaborn`'s `sns.despine()`). Y-axes have gridlines, X-axes do not. X-axes have ticks, Y-axes do not. But both have same-size labels and titles. 


```python
def urban_theme():
    # Typography
    font = "Lato"
    # At Urban it's the same font for all text but it's good to keep them separate in case you want to change one later.
    labelFont = "Lato" 
    sourceFont = "Lato"
    
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    
    return {
        "config": {
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "fontColor": "#000000"
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "tickSize": 5, # default, including it just to show you can change it
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "ticks": False, # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "Y Axis Title (units)", 
                # titles are by default vertical left of axis so we need to hack this 
                "titleAngle": 0, # horizontal
                "titleY": -10, # move it up
                "titleX": 18, # move it to the right so it aligns with the labels 
            },
            
        }
    }
```

If you _register_ed and _enable_d this theme you'd have something that kinda, sorta, looks like an Urban Institute's chart. But what lets you know right away that you are looking at an Urban Institute's data visualization is the colors.

```python
# register
alt.themes.register("my_custom_theme", urban_theme)
# enable
alt.themes.enable("my_custom_theme")
```

In `altair`, you have `scales` with `domain` and `range`. These are "_functions that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels._" So if you want to add a default color scheme all you have to do is encode in your theme the values for the top-level object `"range"`.

We'll save the values as a list `main_palette` and `sequential_palette`. The Urban Institute's Data Visualization Styleguide has __a lot__ of color combinations. We will encode these two as defaults but when it comes to colors you will most likely end up modifying your data visualization on the go.

```python
def urban_theme():
    # Typography
    font = "Lato"
    # At Urban it's the same font for all text but it's good to keep them separate in case you want to change one later.
    labelFont = "Lato" 
    sourceFont = "Lato"
    
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    
    # Colors
    main_palette = ["#1696d2", 
                    "#d2d2d2",
                    "#000000", 
                    "#fdbf11", 
                    "#ec008b", 
                    "#55b748", 
                    "#5c5859", 
                    "#db2b27", 
                   ]
    sequential_palette = ["#cfe8f3", 
                          "#a2d4ec", 
                          "#73bfe2", 
                          "#46abdb", 
                          "#1696d2", 
                          "#12719e", 
                         ]
    
    return {
        "config": {
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "fontColor": "#000000"
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "tickSize": 5, # default, including it just to show you can change it
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "ticks": False, # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "Y Axis Title (units)", 
                # titles are by default vertical left of axis so we need to hack this 
                "titleAngle": 0, # horizontal
                "titleY": -10, # move it up
                "titleX": 18, # move it to the right so it aligns with the labels 
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            }
            
        }
    }
```

At this point, your theme will have the Urban Institute's title, axes, and color configurations by default. Pretty cool but that's not all you can do. 

Let's add a default legend configuration.
This time we'll stray away from the styleguide a little because the position of the legend depends on the chart at hand (and you can't have a horizontal legend in vega-lite).

This code also includes "view" and "background" configurations which are easy to follow without much explanation. It also includes the configurations for "area", "line", "trail", "bar", "point", and other marks. This is just setting up the colors right for each specific mark.

```python
def urban_theme():
    # Typography
    font = "Lato"
    # At Urban it's the same font for all text but it's good to keep them separate in case you want to change one later.
    labelFont = "Lato" 
    sourceFont = "Lato"
    
    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    
    # Colors
    main_palette = ["#1696d2", 
                    "#d2d2d2",
                    "#000000", 
                    "#fdbf11", 
                    "#ec008b", 
                    "#55b748", 
                    "#5c5859", 
                    "#db2b27", 
                   ]
    sequential_palette = ["#cfe8f3", 
                          "#a2d4ec", 
                          "#73bfe2", 
                          "#46abdb", 
                          "#1696d2", 
                          "#12719e", 
                         ]
    
    return {
        # width and height are configured outside the config dict because they are Chart configurations/properties not chart-elements' configurations/properties.
        "width": 685, # from the guide
        "height": 380, # not in the guide
        "config": {
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "fontColor": "#000000"
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "tickSize": 5, # default, including it just to show you can change it
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "ticks": False, # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "Y Axis Title (units)", 
                # titles are by default vertical left of axis so we need to hack this 
                "titleAngle": 0, # horizontal
                "titleY": -10, # move it up
                "titleX": 18, # move it to the right so it aligns with the labels 
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            },
            "legend": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "symbolType": "square", # just 'cause
                "symbolSize": 100, # default
                "titleFont": font,
                "titleFontSize": 12,
                "title": "", # set it to no-title by default
                "orient": "top-left", # so it's right next to the y-axis
                "offset": 0, # literally right next to the y-axis.
            },
            "view": {
                "stroke": "transparent", # altair uses gridlines to box the area where the data is visualized. This takes that off.
            },
            "background": {
                "color": "#FFFFFF", # white rather than transparent
            },
            ### MARKS CONFIGURATIONS ###
            "area": {
               "fill": markColor,
           },
           "line": {
               "color": markColor,
               "stroke": markColor,
               "strokewidth": 5,
           },
           "trail": {
               "color": markColor,
               "stroke": markColor,
               "strokeWidth": 0,
               "size": 1,
           },
           "path": {
               "stroke": markColor,
               "strokeWidth": 0.5,
           },
           "point": {
               "filled": True,
           },
           "text": {
               "font": sourceFont,
               "color": markColor,
               "fontSize": 11,
               "align": "right",
               "fontWeight": 400,
               "size": 11,
           }, 
           "bar": {
                "size": 40,
                "binSpacing": 1,
                "continuousBandSize": 30,
                "discreteBandSize": 30,
                "fill": markColor,
                "stroke": False,
            }, 
            
        }
    }
```


#### SIDE NOTE
I personally save these themes in a `.py` script with 
```python
import altair as alt
alt.themes.register("my_custom_theme", urban_theme)
alt.themes.enable("my_custom_theme")
```
at the end and just `%run theme.py` in my jupyter notebook. 

***
Here are some examples of charts created with that theme.

#### Bar Chart
![bar_chart](../images/figures/urban_barchart.png)

#### Area Chart (categorical)
![area_chart](../images/figures/urban_areachart.png)

#### Area Chart (sequential)
![area_chart2](../images/figures/urban_areachart-sequential.png)

#### Line Chart
![line_chart](../images/figures/urban_linechart.png)

***

There are __a lot__ of ways to configure your theme and I would encourage you to try many different things. You can take this theme we just put together and play around with the values. Use a different font, font size, color-scheme. Have gridlines, don't have gridlines. Have really, really, big labels for your axes. Do whatever you want but save it somewhere so you can build on it and grow your personal style.

While you may want to look up more on this in the `altair` documentation, I find it better to use the [Vega-lite](https://vega.github.io/vega-lite/docs/config.html) documentation. After all, `altair` is a python-wrapper for vega-lite. 

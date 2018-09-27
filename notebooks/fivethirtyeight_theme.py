def fivethirtyeight_theme():
    markColor = '#30a2da'
    axisColor = '#cbcbcb'
    backgroundColor = '#f0f0f0'
    return {
        'config': {
            'arc': { 
                'fill': markColor 
            },
            'area': { 
                'fill': markColor 
            },
            'axisBand': {
                'grid': False,
            },
            'axisBottom': {
                'domain': False,
                'domainColor': 'black',
                'domainWidth': 3,
                'grid': True,
                'gridColor': axisColor,
                'gridWidth': 1,
                'labelFontSize': 12,
                'labelPadding': 4,
                'tickColor': axisColor,
                'tickSize': 10,
                'titleFontSize': 14,
                'titlePadding': 10,
            },
            'axisLeft': {
                'domainColor': axisColor,
                'domainWidth': 1,
                'gridColor': axisColor,
                'gridWidth': 1,
                'labelFontSize': 12,
                'labelPadding': 4,
                'tickColor': axisColor,
                'tickSize': 10,
                'ticks': True,
                'titleFontSize': 14,
                'titlePadding': 10,
            },
            'axisRight': {
                'domainColor': axisColor,
                'domainWidth': 1,
                'gridColor': axisColor,
                'gridWidth': 1,
                'labelFontSize': 12,
                'labelPadding': 4,
                'tickColor': axisColor,
                'tickSize': 10,
                'ticks': True,
                'titleFontSize': 14,
                'titlePadding': 10,
            },
            'axisTop': {
                'domain': False,
                'domainColor': 'black',
                'domainWidth': 3,
                'grid': True,
                'gridColor': axisColor,
                'gridWidth': 1,
                'labelFontSize': 12,
                'labelPadding': 4,
                'tickColor': axisColor,
                'tickSize': 10,
                'titleFontSize': 14,
                'titlePadding': 10,
            },
            'background': backgroundColor,
            'group': {
                'fill': backgroundColor,
            },
            'legend': {
                'labelFontSize': 11,
                'padding': 1,
                'symbolSize': 30,
                'symbolType': 'square',
                'titleFontSize': 14,
                'titlePadding': 10,
            },
            'line': {
                'stroke': markColor,
                'strokeWidth': 2,
            },
            'path': { 
                'stroke': markColor, 
                'strokeWidth': 0.5 
            },
            'point': { 
                'filled': True 
            },
            'rect': { 
                'fill': markColor 
            },
            'range': {
                'category': [
                    '#30a2da',
                    '#fc4f30',
                    '#e5ae38',
                    '#6d904f',
                    '#8b8b8b',
                    '#b96db8',
                    '#ff9e27',
                    '#56cc60',
                    '#52d2ca',
                    '#52689e',
                    '#545454',
                    '#9fe4f8',
                ],
                'diverging': [
                    '#cc0020',
                    '#e77866',
                    '#f6e7e1',
                    '#d6e8ed',
                    '#91bfd9',
                    '#1d78b5',
                ],
                'heatmap': ['#d6e8ed', '#cee0e5', '#91bfd9', '#549cc6', '#1d78b5'],
            },
            'symbol': {
                'opacity': 1,
                'shape': 'circle',
                'size': 40,
                'strokeWidth': 1,
            },
            'shape': { 
                'stroke': markColor 
            },
            'style': {
                'bar': {
                    'binSpacing': 2,
                    'fill': markColor,
                    'stroke': None,
                },
            },
            'title': {
                'anchor': 'start',
                'fontSize': 24,
                'fontWeight': 600,
                'offset': 20,
            },
        }
    }

import altair as alt

# register the custom theme under a chosen name
alt.themes.register('fivethirtyeight_theme', fivethirtyeight_theme)

# enable the newly registered theme
alt.themes.enable('fivethirtyeight_theme')
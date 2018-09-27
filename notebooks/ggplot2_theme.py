def ggplot2_theme():
    markColor = '#000'
    return {
        'config': {
            'group': {
                'fill': '#e5e5e5',
            },
            'arc': { 
                'fill': markColor 
            },
            'area': { 
                'fill': markColor 
            },
            'line': { 
                'stroke': markColor 
            },
            'path': { 
                'stroke': markColor 
            },
            'rect': { 
                'fill': markColor 
            },
            'shape': { 
                'stroke': markColor 
            },
            'symbol': { 
                'fill': markColor, 
                'size': 40 
            },
            'axis': {
                'domain': False,
                'grid': True,
                'gridColor': '#FFFFFF',
                'gridOpacity': 1,
                'labelColor': '#7F7F7F',
                'labelPadding': 4,
                'tickColor': '#7F7F7F',
                'tickSize': 5.67,
                'titleFontSize': 16,
                'titleFontWeight': 'normal',
            },
            'legend': {
                'labelBaseline': 'middle',
                'labelFontSize': 11,
                'symbolSize': 40,
            },  
            'range': {
                'category': [
                    '#000000',
                    '#7F7F7F',
                    '#1A1A1A',
                    '#999999',
                    '#333333',
                    '#B0B0B0',
                    '#4D4D4D',
                    '#C9C9C9',
                    '#666666',
                    '#DCDCDC',
                ],
            },
        }
    }


import altair as alt

# register the custom theme under a chosen name
alt.themes.register('ggplot2_theme', ggplot2_theme)

# enable the newly registered theme
alt.themes.enable('ggplot2_theme')
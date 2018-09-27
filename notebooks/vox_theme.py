def vox_theme():
    markColor = '#3e5c69'
    
    return {
        'config': {
            'background': '#fff',
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
                'fill': markColor 
            },
            'axis': {
                'domainWidth': 0.5,
                'grid': True,
                'labelPadding': 2,
                'tickSize': 5,
                'tickWidth': 0.5,
                'titleFontWeight': 'normal',
            },
            'axisBand': {
                'grid': False,
            },
            'axisX': {
                'gridWidth': 0.2,
            },  
            'axisY': {
                'gridDash': [3],
                'gridWidth': 0.4,
            },
            'legend': {
                'labelFontSize': 11,
                'padding': 1,
                'symbolType': 'square',
            },
            'range': {
                'category': [
                    '#3e5c69',
                    '#6793a6',
                    '#182429',
                    '#0570b0',
                    '#3690c0',
                    '#74a9cf',
                    '#a6bddb',
                    '#e2ddf2',
                ],
            },
        }
        
    }

import altair as alt

# register the custom theme under a chosen name
alt.themes.register('vox_theme', vox_theme)

# enable the newly registered theme
alt.themes.enable('vox_theme')
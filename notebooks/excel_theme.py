def excel_theme():
    markColor = '#4572a7'
    return  {
        'config': {
            'background': '#fff',
            'arc': { 
                'fill': markColor 
            },
            'area': { 
                'fill': markColor 
            },
            'line': { 
                'stroke': markColor, 
                'strokeWidth': 2 
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
                'strokeWidth': 1.5, 
                'size': 50 
            },
            'axis': {
                'bandPosition': 0.5,
                'grid': True,
                'gridColor': '#000000',
                'gridOpacity': 1,
                'gridWidth': 0.5,
                'labelPadding': 10,
                'tickSize': 5,
                'tickWidth': 0.5,
            },
            'axisBand': {
                'grid': False,
                'tickExtra': True,
            },
            'legend': {
                'labelBaseline': 'middle',
                'labelFontSize': 11,
                'symbolSize': 50,
                'symbolType': 'square',
            },  
            'range': {
                'category': [
                    '#4572a7',
                    '#aa4643',
                    '#8aa453',
                    '#71598e',
                    '#4598ae',
                    '#d98445',
                    '#94aace',
                    '#d09393',
                    '#b9cc98',
                    '#a99cbc',
                ],
            },
        }
        
    }

import altair as alt

# register the custom theme under a chosen name
alt.themes.register('excel_theme', excel_theme)

# enable the newly registered theme
alt.themes.enable('excel_theme')
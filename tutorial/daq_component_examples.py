# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

from tutorial import styles
from tutorial import tools
from tutorial.utils.convert_props_to_table_daq import generate_prop_table
from tutorial.utils.component_block import ComponentBlock
from tutorial.components import Syntax, Example

examples = {
    'boolean-switch': tools.load_example('tutorial/examples/daq_components/boolean_switch.py'),
    'color-picker': tools.load_example('tutorial/examples/daq_components/color_picker.py'),
    'gauge': tools.load_example('tutorial/examples/daq_components/gauge.py'),
    'graduated-bar': tools.load_example('tutorial/examples/daq_components/graduated_bar.py'),
    'indicator': tools.load_example('tutorial/examples/daq_components/indicator.py'),
    'knob': tools.load_example('tutorial/examples/daq_components/knob.py'),
    'LED-display': tools.load_example('tutorial/examples/daq_components/LED_display.py'),
    'numeric-input': tools.load_example('tutorial/examples/daq_components/numeric_input.py'),
    'power-button': tools.load_example('tutorial/examples/daq_components/power_button.py'),
    'precision-input': tools.load_example('tutorial/examples/daq_components/precision_input.py'),
    'stop-button': tools.load_example('tutorial/examples/daq_components/stop_button.py'),
    'slider': tools.load_example('tutorial/examples/daq_components/slider.py'),
    'tank': tools.load_example('tutorial/examples/daq_components/tank.py'),
    'thermometer': tools.load_example('tutorial/examples/daq_components/thermometer.py'),
    'toggle-switch': tools.load_example('tutorial/examples/daq_components/toggle_switch.py'),
    'dark-theme-provider': tools.load_example('tutorial/examples/daq_components/dark_theme_provider.py')
    
}


# BooleanSwitch
BooleanSwitch = html.Div(children=[
    html.H1('Boolean Switch Examples and Reference'),
    html.Hr(),
    html.H3('Default Boolean Switch'),
    html.P("An example of a default boolean switch without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['boolean-switch'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['boolean-switch'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Boolean Switch Properties"),
    generate_prop_table('BooleanSwitch')
])

# ColorPicker
ColorPicker = html.Div(children=[
    html.H1('Color Picker Examples and Reference'),
    html.Hr(),
    html.H3('Default Color Picker'),
    html.P("An example of a default Color Picker without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['color-picker'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['color-picker'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Color Picker Properties"),
    generate_prop_table('ColorPicker')
])

# Gauge
Gauge = html.Div(children=[
    html.H1('Gauge Examples and Reference'),
    html.Hr(),
    html.H3('Default Gauge'),
    html.P("An example of a default Gauge without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['gauge'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['gauge'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Gauge Properties"),
    generate_prop_table('Gauge')
])

# Graduated Bar
GraduatedBar = html.Div(children=[
    html.H1('Graduated bar Examples and Reference'),
    html.Hr(),
    html.H3('Default Graduated bar'),
    html.P("An example of a default Graduated bar without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['graduated-bar'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['graduated-bar'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Graduated Bar Properties"),
    generate_prop_table('GraduatedBar')
])

# Indicator
Indicator = html.Div(children=[
    html.H1('Indicator Examples and Reference'),
    html.Hr(),
    html.H3('Default Indicator'),
    html.P("An example of a default Indicator without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['indicator'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['indicator'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Indicator Properties"),
    generate_prop_table('Indicator')
])

# Knob
Knob = html.Div(children=[
    html.H1('Knob Examples and Reference'),
    html.Hr(),
    html.H3('Default Knob'),
    html.P("An example of a default Knob without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['knob'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['knob'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Knob Properties"),
    generate_prop_table('Knob')
])

# LED Display
LEDDisplay = html.Div(children=[
    html.H1('LED display Examples and Reference'),
    html.Hr(),
    html.H3('Default LED display'),
    html.P("An example of a default LED display without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['LED-display'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['LED-display'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("LED Display Properties"),
    generate_prop_table('LEDDisplay')
])

# Numeric Input
NumericInput = html.Div(children=[
    html.H1('LED display Examples and Reference'),
    html.Hr(),
    html.H3('Default Numeric Input'),
    html.P("An example of a default numeric input without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['numeric-input'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['numeric-input'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Numeric Input Properties"),
    generate_prop_table('NumericInput')
])

# Power Button
PowerButton = html.Div(children=[
    html.H1('LED display Examples and Reference'),
    html.Hr(),
    html.H3('Default Power Button'),
    html.P("An example of a default power button without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['power-button'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['power-button'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Power Button Properties"),
    generate_prop_table('PowerButton')
])

# Precision Input
PrecisionInput = html.Div(children=[
    html.H1('Precision Input Examples and Reference'),
    html.Hr(),
    html.H3('Default Precision Input'),
    html.P("An example of a default precision input without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['precision-input'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['precision-input'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Precision Input Properties"),
    generate_prop_table('PrecisionInput')
])

# Stop Button
StopButton = html.Div(children=[
    html.H1('Stop Button Examples and Reference'),
    html.Hr(),
    html.H3('Default Stop Button'),
    html.P("An example of a default stop button without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['stop-button'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['stop-button'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Stop Button Properties"),
    generate_prop_table('StopButton')
])

# Slider
Slider = html.Div(children=[
    html.H1('Slider Examples and Reference'),
    html.Hr(),
    html.H3('Default Slider'),
    html.P("An example of a default slider without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['slider'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['slider'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Slider Properties"),
    generate_prop_table('Slider')
])

# Tank
Tank = html.Div(children=[
    html.H1('Tank Examples and Reference'),
    html.Hr(),
    html.H3('Default Tank'),
    html.P("An example of a default tank without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['tank'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['tank'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Tank Properties"),
    generate_prop_table('Tank')
])

# Thermometer
Thermometer = html.Div(children=[
    html.H1('Thermometer Examples and Reference'),
    html.Hr(),
    html.H3('Default Thermometer'),
    html.P("An example of a default Thermometer without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['thermometer'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['thermometer'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Thermometer Properties"),
    generate_prop_table('Thermometer')
])

# Toggle Switch
ToggleSwitch = html.Div(children=[
    html.H1('Toggle Switch Examples and Reference'),
    html.Hr(),
    html.H3('Default Toggle Switch'),
    html.P("An example of a default toggle switch without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['toggle-switch'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['toggle-switch'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Toggle Switch Properties"),
    generate_prop_table('ToggleSwitch')
])

# Dark Theme Provider
DarkThemeProvider = html.Div(children=[
    html.H1('Dark Theme Provider Examples and Reference'),
    html.Hr(),
    html.H3('Default Dark Theme Provider'),
    html.P("An example of a default dark theme provider without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['dark-theme-provider'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['dark-theme-provider'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
#     html.H3('Multi-Value Dropdown'),
#     dcc.Markdown("A dropdown component with the `multi` property set to `True` \
#                   will allow the user to select more than one value \
#                   at a time."),
#     ComponentBlock('''import dash_core_components as dcc

# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montreal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value=['MTL', 'NYC'],
#     multi=True
# )''', customStyle=styles.code_container, language='python'),
#     html.Hr(),

    html.Hr(),
    html.H3("Dark Theme Provider Properties"),
    generate_prop_table('DarkThemeProvider')
])
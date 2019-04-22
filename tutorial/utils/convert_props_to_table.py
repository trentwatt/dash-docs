# -*- coding: utf-8 -*-
import json
import os
import dash_html_components as html
import dash_core_components as dcc
import dash_cytoscape
import dash_table
import pandas as pd
import re
from textwrap import dedent


def generate_prop_table(component_name, lib=dcc):
    component = getattr(lib, component_name)
    component_doc = component.__doc__
    subs = [
        [r'A {} component.\n'.format(component.__name__), ''],
        [r'- setProps.*\n', ''],
        [r'Available events: .*', '']
    ]
    for sub in subs:
        component_doc = re.sub(sub[0], sub[1], component_doc)

    return html.Div([
        dcc.Markdown(dedent(
        '''
        > Access this documentation in your Python terminal with:
        > ```
        > >>> help({}.{})
        > ```
        '''.format(lib.__name__, component_name)
        )),
        dcc.Markdown(component_doc)
    ])

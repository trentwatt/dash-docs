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


def generate_prop_info(component_name, lib=dcc):
    component = getattr(lib, component_name)
    component_doc = component.__doc__

    regex = r"^\s*([a-zA-Z_]*)\s*\(([a-zA-Z\/:',\s]*);\s*([A-Za-z\s]*)\):\s*(.*?)\s*$"

    return_div = [
        dcc.Markdown(dedent(
            '''
            > Access this documentation in your Python terminal with:
            > ```
            > >>> help({}.{})
            > ```
            '''.format(lib.__name__, component_name)
        ))
    ]

    props = component_doc.split('\n-')[1:]

    for prop in props:
        if component_name == 'Molecule3dViewer' and 'dash_bio' in str(lib):
            print(component_doc)

        r = re.match(
            re.compile(regex),
            prop.replace('\n', ' ')
        )

        if r is not None:
            (prop_name, prop_type, prop_optional_default, prop_desc) = r.groups()
            prop_desc = prop_desc.replace('[', '\[').replace(']', '\]')

            defined_default_val = re.search(r'default (.*)', prop_optional_default)

            prop_optional = prop_optional_default
            if defined_default_val is not None:
                prop_optional = f'default `{defined_default_val.groups(1)[0]}`'

            return_div.append(dcc.Markdown(dedent(
                f'''
                **`{prop_name}`** (*{prop_type};* {prop_optional}): {prop_desc}
                '''
            )))

    return html.Div(return_div)

library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  simple_example=utils$LoadExampleCode('dashr/chapters/dash-core-components/dropdown/examples/simple-example.R')
)


layout <- htmlDiv(list(
htmlH1('dccDropdown - Examples & Reference'),
htmlHr(),

dccMarkdown('
# Default Dropdown

An example of a default dropdown without any extra properties.
'),
examples$simple_example$source_code,
examples$simple_example$layout,

dccMarkdown('
***

## Multi-Value Dropdown

A dropdown component with the `multi` property set to `TRUE`
will allow the user to select more than one value at a time.
'),
utils$LoadAndDisplayComponent(
'
library(dashR)
library(dashCoreComponents)

dccDropdown(
  options=list(
    list(label="New York City", value="NYC"),
    list(label="Montréal", value="MTL"),
    list(label="San Francisco", value="SF")
  ),
  value=list("MTL", "NYC"),
  multi=TRUE
)
'
),

dccMarkdown("
***

## Disable Search

The `searchable` property is set to `TRUE` by default on all Dropdown components.
To prevent searching the dropdown value, just set the `searchable` property to `FALSE`.
Try searching for 'New York' on this dropdown below and compare it to the other dropdowns on the page to see the difference.
"),
utils$LoadAndDisplayComponent(
  '
library(dashR)
library(dashCoreComponents)

dccDropdown(
    options=list(
      list(label="New York City", value="NYC"),
      list(label="Montréal", value="MTL"),
      list(label="San Francisco", value="SF")
    ),
    searchable=FALSE
)
'
),

dccMarkdown("
***

## Dropdown Clear

The `clearable` property is set to `TRUE` by default on all Dropdown components.
To prevent the clearing of the selected dropdown value, just set the `clearable` property to `FALSE`
"),
utils$LoadAndDisplayComponent(
'
library(dashR)
library(dashCoreComponents)

dccDropdown(
    options=list(
      list(label="New York City", value="NYC"),
      list(label="Montréal", value="MTL"),
      list(label="San Francisco", value="SF")
    ),
    value="MTL",
    clearable=FALSE
)
'
),

dccMarkdown("
***

## Placeholder Text

The `placeholder` property allows you to define default text shown when no value is selected.
"),
utils$LoadAndDisplayComponent(
  '
library(dashR)
library(dashCoreComponents)

dccDropdown(
    options=list(
      list(label="New York City", value="NYC"),
      list(label="Montréal", value="MTL"),
      list(label="San Francisco", value="SF")
    ),
    placeholder="Select a city"
)
'
),

dccMarkdown("
***

## Disable Dropdown

To disable the dropdown just set `disabled=True`.
"),
utils$LoadAndDisplayComponent(
  '
library(dashR)
library(dashCoreComponents)

dccDropdown(
    options=list(
      list(label="New York City", value="NYC"),
      list(label="Montréal", value="MTL"),
      list(label="San Francisco", value="SF")
    ),
    disabled=TRUE
)
'
),

dccMarkdown("
***

## Disable Options

To disable a particular option inside the dropdown menu, set the `disabled` property in the options.
"),
utils$LoadAndDisplayComponent(
  '
library(dashR)
library(dashCoreComponents)

dccDropdown(
    options=list(
      list(label="New York City", value="NYC", "disabled" = TRUE),
      list(label="Montréal", value="MTL"),
      list(label="San Francisco", value="SF", "disabled" = TRUE)
    )
)
'
),

dccMarkdown("
***

## Dropdown Properties
"),
dccMarkdown(help(dccDropdown)),
utils$LoadAndDisplayComponent(
  '
library(dashR)
library(dashCoreComponents)

dccMarkdown(help(dccDropdown))
'
),

htmlHr(),
dccMarkdown("
[Back to the Table of Contents](/)
  ")


))

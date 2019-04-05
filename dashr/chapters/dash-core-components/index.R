library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

examples <- list(
  button1 = utils$LoadExampleCode('dashr/chapters/dash-core-components/button/examples/simple-example.R')
)


titleLink <- function(componentName) {
  return(htmlH2(
    dccLink(
      componentName,
      href=paste('/dash-core-components/', componentName, sep='')
    )
  ))
}

referenceLink <- function(componentName) {
  return(dccLink(
    'More examples & reference',
    href=paste('/dash-core-components/', componentName, sep='')
  ))
}

layout <- htmlDiv(list(

htmlH1('Dash Core Components'),

htmlDiv(titleLink('dccDropdown')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccDropdown(
  options=list(
    list(label="New York City", value="NYC"),
    list(label="Montréal", value="MTL"),
    list(label="San Francisco", value="SF")
  ),
  value="MTL"
)
'
),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccDropdown(
  options=list(
    list(label="New York City", value="NYC"),
    list(label="Montréal", value="MTL"),
    list(label="San Francisco", value="SF")
  ),
  value="MTL",
  multi=TRUE
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccSlider')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccSlider(
    min=-5,
    max=10,
    step=0.5,
    value=-3,
)
'
),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccSlider(
    min=0,
    max=9,
    marks=c(paste("Label", 0:10)),
    value=5,
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccRangeSlider')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccRangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=list(-3, 7)
)
'
),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccRangeSlider(
    marks=c(paste("Label", -5:7)),
    min=-5,
    max=6,
    value=list(-3, 4)
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccInput')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccInput(
    placeholder=\'Enter a value...\',
    type=\'text\',
    value=\'\'
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccInput')),
utils$LoadAndDisplayComponent(
  'library(dashCoreComponents)

dccTextarea(
    placeholder=\'Enter a value...\',
    value=\'This is a TextArea component\',
    style=list(\'width\'= \'100%\')
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccCheckboxes')),
utils$LoadAndDisplayComponent(
  'library(dashCoreComponents)

dccChecklist(
    options=list(
        list(label="New York City", value="NYC"),
        list(label="Montréal", value="MTL"),
        list(label="San Francisco", value="SF")
    ),
    values=list("MTL", "SF")
)
'
),

utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccChecklist(
    options=list(
        list(label="New York City", value="NYC"),
        list(label="Montréal", value="MTL"),
        list(label="San Francisco", value="SF")
    ),
    values=list("MTL", "SF"),
    labelStyle=list("display" = "inline-block")
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccRadioItems')),
utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccRadioItems(
    options=list(
        list(label="New York City", value="NYC"),
        list(label="Montréal", value="MTL"),
        list(label="San Francisco", value="SF")
    ),
    value="MTL"
)
'
),

utils$LoadAndDisplayComponent(
'library(dashCoreComponents)

dccRadioItems(
    options=list(
        list(label="New York City", value="NYC"),
        list(label="Montréal", value="MTL"),
        list(label="San Francisco", value="SF")
    ),
    value="MTL",
    labelStyle=list("display" = "inline-block")
)
'
),
htmlDiv(referenceLink('dropdown')),


htmlDiv(titleLink('htmlButton')),
utils$LoadAndDisplayComponent(
'library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(htmlDiv(list(
    htmlDiv(dccInput(id="input-box", type="text")),
    htmlButton("Submit", id="button"),
    htmlDiv(id="output-container-button",
             children="Enter a value and press submit")
)))


#app$run_server()
'
),


# app$callback(output("output-container-button", "children"),
#              list(input("button", "n_clicks"),
#                   input("input-box", "value")),
#              function(n_clicks, value) {
#                sprintf(\'The input value was "%s" and the button has been clicked "%s" times\', value, n_clicks)
#              })

# examples$button1$source,
# examples$button1$layout,
htmlDiv(referenceLink('dropdown'))

))

route <- function(pathname) {
  componentName = gsub('dropdown', '', pathname)
  component_chapter_index = file.path(
    'dashr',
    'chapters',
    'dash-core-components',
    componentName,
    'index.R'
  )
  tmp_namespace = new.env()
  source(component_chapter_index, local=tmp_namespace)
  return(tmp_namespace$layout);
}

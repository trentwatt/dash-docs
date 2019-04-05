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
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('DatePickerSingle')),
utils$LoadAndDisplayComponent(
'library(dashR)
library(dashCoreComponents)
library(lubridate)


dccDatePickerSingle(
    id="date-picker-single",
    date=ymd("1997-05-10")
)
'
),

htmlDiv(titleLink('DatePickerRange')),
utils$LoadAndDisplayComponent(
  'library(dashR)
library(dashCoreComponents)
library(lubridate)

dccDatePickerRange(
    id="date-picker-range",
    start_date=ymd("1997-05-3"),
    end_date_placeholder_text="Select a date!"
)
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('dccMarkdown')),
utils$LoadAndDisplayComponent(
'library(dashR)
library(dashCoreComponents)

dccMarkdown("
#### Dash and Markdown

Dash supports [Markdown](http://commonmark.org/help).

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
")
'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('Interactive Tables')),
utils$LoadAndDisplayComponent(
'library(dashR)
library(dashCoreComponents)

dccMarkdown("
The `dashHtmlComponents` library exposes all of the HTML tags.
This includes the `Table`, `Tr`, and `Tbody` tags that can be used to create an HTML table.
See [Create Your First Dash App, Part 1](/getting-started-part-1) for an example.
Dash provides an interactive`DataTable` as part of the `data-table` project.
This table includes built-in filtering, row-selection, editing, and sorting.
![Example of a Dash Interactive Table](https://dash.plot.ly/assets/images/gallery/DataTable.gif)
")

'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('Upload Component')),
utils$LoadAndDisplayComponent(
'library(dashR)
library(dashCoreComponents)

dccMarkdown("
The `dccUpload` component allows users to upload files into your app
through drag-and-drop or the system\'s native file explorer.
![Dash Upload Component](https://user-images.githubusercontent.com/1280389/30351245-6b93ee62-97e8-11e7-8e85-0411e9d6c98c.gif)
")

'
),
htmlDiv(referenceLink('dropdown')),

htmlDiv(titleLink('Tabs')),
utils$LoadAndDisplayComponent(
'library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

dccMarkdown("
The Tabs and Tab components can be used to create tabbed sections in your app.
")

app$layout(htmlDiv(list(
    dccTabs(id="tabs", value="tab-1", children=list(
        dccTab(label="Tab one", value="tab-1"),
        dccTab(label="Tab two", value="tab-2")
    )),
    htmlDiv(id="tabs-content")
)))
'
),

# app$callback(output("tabs-content", "children"),
#              list(input("tabs", "value")),
#              function(tab) {
#                if(tab == "tab-1"){
#                  return(htmlDiv(list(
#                    htmlH3("Tab content 1")
#                  )))
#                }else if(tab == "tab-2"){
#                  return(htmlDiv(list(
#                    htmlH3("Tab content 2")
#                  )))
#                }
#              })
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

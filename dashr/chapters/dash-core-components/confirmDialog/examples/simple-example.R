library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(htmlDiv(list(
  htmlButton(
    id="input-button",
    'Click Me'
  ),
  htmlDiv(id="output-div")
)))


app$callback(output("output-div", "children"),
             list(input("input-button", "n_clicks")),
             function(n_clicks) {
               return(dccConfirmDialogProvider(
                 id='confirm',
                 message='Danger danger! Are you sure you want to continue?'
               )
             )})

# app$run_server()


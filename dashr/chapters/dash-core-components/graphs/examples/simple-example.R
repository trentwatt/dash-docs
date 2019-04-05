library(dashR)
library(dashCoreComponents)
library(dashHtmlComponents)

app <- Dash$new()

app$layout(htmlDiv(list(
  dccGraph(
    figure = list(
      data = list(
        list(
          x = c(1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012),
          y = c(219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                350, 430, 474, 526, 488, 537, 500, 439),
          name = 'Rest of world',
          type='bar',
          marker = list(color = 'rgb(55, 83, 109)')
        ),
        list(
          x = c(1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012),
          y = c(16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                299, 340, 403, 549, 499),
          name = 'China',
          type='bar',
          marker = list(color = 'rgb(26, 118, 255)')
        )
      ),
      layout = list(
        title = 'US Export of Plastic Scrap',
        showlegend = TRUE,
        legend = list(
          x = 0,
          y = 1.0
        ),
        margin = list(l = 40, r = 0, t = 40, b = 30)
      )
    ),
    style = list(height = 300),
    id = 'my-graph'
  ),

  htmlBr(),

  htmlDiv(id = 'hidden', style = list(display = 'none'))
)))

# app$run_server()


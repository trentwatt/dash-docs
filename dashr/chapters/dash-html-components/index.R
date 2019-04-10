library(dashCoreComponents)
library(dashHtmlComponents)
library(dashR)

utils <- new.env()
source('dashr/utils.R', local=utils)

layout <- htmlDiv(list(
  htmlH1('Dash HTML Components'),
dccMarkdown("
  Dash is a web application framework that provides pure R abstraction around HTML, CSS, and JavaScript.
  Instead of writing HTML or using an HTML templating engine, you compose your layout using R structures with the `dashHtmlComponents` library.
  The source for this library is on GitHub: [plotly/dash-html-components](https://github.com/plotly/dash-html-components).
  Here is an example of a simple HTML structure:
"),
utils$LoadComponent(
  'library(dashHtmlComponents)

  htmlDiv(list(
  htmlH1(\'Hello Dash\'),
  htmlDiv(list(
    htmlP(\'Dash converts R classes into HTML\'),
    htmlP(\'This conversion happens behind the scenes by Dash s JavaScript front-end\')
    ))
  ))'
),

dccMarkdown("
which gets converted (behind the scenes) into the following HTML in your web-app:
  "),
utils$LoadComponent(
  '<div>
      <h1>Hello Dash</h1>
      <div>
          <p>Dash converts Python classes into HTML</p>
          <p>This conversion happens behind the scenes by Dash\'s JavaScript front-end</p>
    </div>
  </div>'
),
dccMarkdown("
  If you're not comfortable with HTML, don't worry!
  You can get 95% of the way there with just a few elements and attributes.
  Dash's [core component library](/dash-core-components) also supports
  [Markdown](https://commonmark.org/help/).
"),

utils$LoadAndDisplayComponent(
  'library(dashHtmlComponents)

  dccMarkdown("
    #### Dash and Markdown

    Dash supports [Markdown](http://commonmark.org/help).

    Markdown is a simple way to write and format text.
    It includes a syntax for things like **bold text** and *italics*,
    [links](http://commonmark.org/help), inline `code` snippets, lists,
    quotes, and more.
  ")'
),


dccMarkdown("
  If you're using HTML components, then you also have access to properties like `style`,
  `class`, and `id`. All of these attributes are available in the Python classes.
  The HTML elements and Dash classes are mostly the same but there are a few key differences:
  - The `style` property is a dictionary
  - Properties in the `style` dictionary are camelCased
  - The `class` key is renamed as `className`
  - Style properties in pixel units can be supplied as just numbers without the `px` unit
  Let's take a look at an example.
"),


utils$LoadComponent(
  "library(dashHtmlComponents)

  htmlDiv(list(
      htmlDiv('Example Div', style=list('color' = 'blue', 'fontSize' = 14)),
      htmlP('Example P', className='my-class', id='my-p-element')
  ), style=list('marginBottom' = 50, 'marginTop' = 25))"
),

dccMarkdown("
  That dash code will render this HTML markup:
"),

utils$LoadComponent(
'<div style="margin-bottom: 50px; margin-top: 25px;">

    <div style="color: blue; font-size: 14px">
        Example Div
    </div>

    <p class="my-class", id="my-p-element">
        Example P
    </p>

</div>'
),

htmlHr(),
dccMarkdown("
  [Back to the Table of Contents](/)
")
))

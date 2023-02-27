library(shiny)

ui <- fluidPage(
  titlePanel("다이아몬드 투명도에 따른 분석"),
  # 화면 분할
  sidebarLayout(
    sidebarPanel(
      # 슬라이드 입력
      sliderInput('level', 'Diamond Level', min = 0, max = 10, value = 3)
    ),
    mainPanel(
      # 출력
      textOutput('selectValue')
     )
  )
)

# Server => UI 요소 데이터 생성 및 입력처리
server <- function(input, output, session){
  output$selectValue <- renderText(input$level)
}

shinyApp(ui, server)

# -----------------------------------------------------
ui <- fluidPage(
  
  # Application title
  titlePanel("Hello Shiny!"),
  
  sidebarLayout(
    
    # Sidebar with a slider input
    sidebarPanel(
      sliderInput("obs",
                  "Number of observations:",
                  min = 0,
                  max = 1000,
                  value = 500),
      checkboxInput("chk", "VALUE"),
      actionButton("OK", "ok")
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot")
    )
  )
)

# Server logic
# Show Output
server <- function(input, output) {
  output$distPlot <- renderPlot({
    hist(rnorm(input$obs))
  })
}

shinyApp(ui = ui, server = server)
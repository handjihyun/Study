# ============================================
library(shiny)

# UI 요소 구성 부분 --------------------------
ui <- fluidPage(
  # add title of webpage
  titlePanel("Data Analysis"),
  
  # add webpage content UI
  # divide window left&right => sidebarLayout()
  sidebarLayout(
    # Left
    sidebarPanel(
      # Input UI
      radioButtons('type', 'Blood TYPE:', c('A', 'B', 'AB', 'O')),
      br(),
      br(),
      br(),
      sliderInput('age', 'AGE', min = 0, max = 200, value = 20)
    ),
    # Right
    mainPanel(
      # Output UI
      # Print Blood Type to text
      textOutput("blood"),
      # Print graph about Age
      plotOutput("pAge")
    )
  )
)

# SERVER 구현 부분 ---------------------------
server <- function(input, output, session){
  # input 매개변수 <- UI 로부터 입력받은 데이터 저장
  # input$type, input$age
  
  # Rendering(Show) data of output UI
  # output$blood, output$pAge
  output$blood <- renderText(paste("당신의 혈액형은 ", input$type, '형 입니다.'))
  output$pAge <- renderPlot( plot({0:input$age}, col = 'blue') )
}

# --------------------------------------------
ui <- fluidPage(
  # add title of webpage
  titlePanel("다이아몬드 데이터 분석"), 
  
  # add webpage content UI
  # divide window by tab
  tabsetPanel(
    tabPanel('캐럿에 대한 분석 결과'),
    tabPanel('투명도에 대한 분석 결과'),
    tabPanel('컷팅에 대한 분석 결과')
  )
) 

server <- function(input, output, session){
  
}
# Shiny App 실행 부분 ------------------------
shinyApp(ui, server)

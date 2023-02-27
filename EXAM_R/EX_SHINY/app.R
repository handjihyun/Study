# ======================================================================================
# shiny package
install.packages("shiny")
library(shiny)

# ======================================================================================
# Web - app programming 
#   - Front - End (UI) + Back - End (Server)
#   - app 실행 코드 
# ======================================================================================
# Front-End(UI) 처리 함수 구현 --------------------------------
# 웹 페이지 구성 => 입력 & 출력 요소
# ======================================================================================
ui <- fluidPage(
  # 화면에 글자 보여주는 UI Widget
  # 함수의 첫번째 매개변수는 output 객체의 속성, id
  textOutput('msg'),
  textOutput('value'),
  verbatimTextOutput('code'), 
  imageOutput('img1')
)

# ======================================================================================
# Back-End(Server) 기능 함수 구현
# 사용자의 요청에 해당하는 페이지 생성
# 웹 페이지 출력 내용 생성
#   - input: Front-End에서 입력한 데이터 저장 객체
#   - ouput: Front-End로 보낼 데이터 저장 객체
# ======================================================================================
server <- function(input, output, session){
  # 상대경로 : app.R파일 기준으로 찾기
  output$msg <- renderText("Good Luck 2023")
  output$value <- renderText(12344566)
  output$code <- renderPrint(summary(1:5))
  filename <- normalizePath(file.path("Image", 'cat.jpg'))
  output$img1 <- renderImage(
    list(src = filename, 
         contentType = 'image/jpg',
         alt = 'This is alternate text')
  )
  deleteFile = FALSE
}

# ======================================================================================
# shiny Web App 실행 ------------------------------------------
#   - 실행 앱의 Front-End, Back-End 지정
# ======================================================================================
shinyApp(ui = ui, server = server)

# UI 처리 기능 함수
ui <- fluidPage(
  plotOutput("plot1", width = '400px')
)

# UI 출력 내용 생성 함수
server <- function(input, output, session){
  output$plot1 = renderPlot(
    {
      cars2 <- cars + rnorm(nrow(cars))
      plot(cars2, col = 'blue', pch = 20)
    }
  )
}

shinyApp(ui = ui, server = server)
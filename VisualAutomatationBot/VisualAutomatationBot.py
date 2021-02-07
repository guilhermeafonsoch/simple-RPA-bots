import pyautogui as p


#pos of browser
p.doubleClick(40, 945)

p.sleep(1)
p.write('https://www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(3)

local_search = p.locateOnScreen(r'C:\ws-py\rpa\RobotTests\RobotFour\SearchBar.png', confidence = 0.9)
search_coord = p.center(local_search)
x_search, y_search = search_coord

p.moveTo(x_search, y_search)
p.click(x_search, y_search)
p.write('Testes de automatos')
p.press('enter')

p.sleep(4)
p.screenshot('Cursos.png')

p.sleep(2)
local_close = p.locateOnScreen(r'C:\ws-py\rpa\RobotTests\RobotFour\Close.png', confidence = 0.9)
search_close = p.center(local_close)
x_close, y_close = search_close

p.moveTo(x_close, y_close)
p.click(x_close, y_close)


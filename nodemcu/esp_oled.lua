-- Nota: O GPIO 16 não pode ser usado para I2C.
-- Pino que está conectado o SDA (GPIO 12).
SDA = 6
-- Pino que está conectado o SCL (GPIO 13).
SCL = 7

-- Endereço I2C do display OLED.
-- Pode ser bbtido no datashet.
ADDRESS = 0x3c

-- Apenas o modo SLOW é suportado.
i2c.setup(0, SDA, SCL, i2c.SLOW)

-- Usamos a função ssd1306_128x64_i2c
-- pois é a compatível com o modelo de display utilizado.
disp = u8g.ssd1306_128x64_i2c(ADDRESS)

function draw()
  disp:setFont(u8g.font_6x10)
  disp:drawStr(10, 10, "BUTECO OPEN SOURCE")
  disp:drawLine(0, 16, 128, 16);
  disp:setFont(u8g.font_chikita)
  disp:drawStr(38, 30, "Exemplo com")
  disp:drawStr(26, 40, "Display OLED I2C")
  disp:drawStr(40, 50, "no BUTECO")
end

function drawLoop()
  -- Início do Picture Loop.
  disp:firstPage()
  -- Ficará desenhando até que a u8g
  -- informe que terminou de desenhar
  -- o que solicitamos.
  repeat
    draw()
  until disp:nextPage() == false
  -- Fim do Picture Loop
end

drawLoop()

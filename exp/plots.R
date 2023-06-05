# 5 Window
window5x <- c(1, 2, 3, 4)
window5y <- c(400, 706, 888, 1035)

plot(
  window5x,
  window5y,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Cantidad de palabras desconocidas V.S. predicciones equivocadas",
  sub = "Tamaño de ventana: 5 palabras. Total de predicciones: 1159",
  xlab = "Cantidad de palabras desconocidas",
  ylab = "Cantidad de predicciones equivocadas"
)

# 10 Window
window10x <- c(1, 2, 4, 5, 7, 8)
window10y <- c(187, 360, 713, 827, 1052, 1093)

plot(
  window10x,
  window10y,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Cantidad de palabras desconocidas V.S. predicciones equivocadas",
  sub = "Tamaño de ventana: 10 palabras. Total de predicciones: 1154",
  xlab = "Cantidad de palabras desconocidas",
  ylab = "Cantidad de predicciones equivocadas"
)

# 20 Window
window20x <- c(1, 2, 4, 8, 10, 14, 16)
window20y <- c(98, 170, 323, 690, 824, 984, 1014)

plot(
  window20x,
  window20y,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Cantidad de palabras desconocidas V.S. predicciones equivocadas",
  sub = "Tamaño de ventana: 20 palabras. Total de predicciones: 1144",
  xlab = "Cantidad de palabras desconocidas",
  ylab = "Cantidad de predicciones equivocadas"
)

# 40 Window
window50x <- c(2, 4, 8, 16, 20, 28, 32)
window50y <- c(276, 333, 469, 725, 824, 939, 962)

plot(
  window50x,
  window50y,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Cantidad de palabras desconocidas V.S. predicciones equivocadas",
  sub = "Tamaño de ventana: 40 palabras. Total de predicciones: 1124",
  xlab = "Cantidad de palabras desconocidas",
  ylab = "Cantidad de predicciones equivocadas"
)


#
# Porcentajes
#

# 5 Window
window5xp <- c(20, 40, 60, 80)
window5yp <- c(34.51, 60.91, 76.61, 89.30)

plot(
  window5xp,
  window5yp,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Porcentaje de palabras desconocidas V.S. porcentaje de predicciones equivocadas",
  sub = "Tamaño de ventana: 5 palabras. Total de predicciones: 1159",
  xlab = "Porcentaje de palabras desconocidas",
  ylab = "Porcentaje de predicciones equivocadas"
)

# 10 Window
window10xp <- c(10, 20, 40, 50, 70, 80)
window10yp <- c(16.20, 31.19, 61.78, 71.66, 91.16, 94.71)

plot(
  window10xp,
  window10yp,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Porcentaje de palabras desconocidas V.S. porcentaje de predicciones equivocadas",
  sub = "Tamaño de ventana: 10 palabras. Total de predicciones: 1154",
  xlab = "Porcentaje de palabras desconocidas",
  ylab = "Porcentaje de predicciones equivocadas"
)

# 20 Window
window20xp <- c(5, 10, 20, 40, 50, 70, 80)
window20yp <- c(8.56, 14.86, 28.23, 60.31, 72.02, 86.01, 88.63)

plot(
  window20xp,
  window20yp,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Porcentaje de palabras desconocidas V.S. porcentaje de predicciones equivocadas",
  sub = "Tamaño de ventana: 20 palabras. Total de predicciones: 1144",
  xlab = "Porcentaje de palabras desconocidas",
  ylab = "Porcentaje de predicciones equivocadas"
)

# 40 Window
window40xp <- c(5, 10, 20, 40, 50, 70, 80)
window40yp <- c(24.55, 29.62, 41.72, 64.50, 73.30, 83.54, 85.58)

plot(
  window40xp,
  window40yp,
  type = 'b',
  lty = 1,
  lwd = 3,
  main = "Porcentaje de palabras desconocidas V.S. porcentaje de predicciones equivocadas",
  sub = "Tamaño de ventana: 40 palabras. Total de predicciones: 1124",
  xlab = "Porcentaje de palabras desconocidas",
  ylab = "Porcentaje de predicciones equivocadas"
)



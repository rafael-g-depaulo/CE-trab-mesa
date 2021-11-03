library(readxl)
raw_data <- read.csv(file.path("UnB/CE 2/simulation-results.csv"))

library(dplyr)
# location <- raw_data %>% group_by(id)
top10 <- head(raw_data[order(raw_data$producao.cientifica, decreasing = TRUE),], 10)
top10$densidade.populacional = trunc(top10$densidade.populacional)
top10$pib.per.capita = trunc(top10$pib.per.capita)
names(top10)[names(top10) == 'NM_MUNICIPIO_PROGRAMA_IES'] <- 'city'

end_point <- 0.5 + nrow(top10) + nrow(top10) - 1
barplot(top10$producao.cientifica, main = "Produção Científica x Densidade Populacional", xlab = "Densidade populacional do Território", ylab = "Produção", col=rgb(0.2,0.4,0.6,0.6))
text(seq(0.5, end_point, by = 1.2), par("usr")[3]-0.25, srt = 60, adj = 1, xpd = TRUE, labels = top10$densidade.populacional, cex = 0.75)

plot(raw_data$pib.per.capita, raw_data$producao.cientifica, pch=19, col="darkgreen", cex=1.5, xlab = 'Pib per capita', ylab =  'Produção cienífica')

library(dplyr)
library(purrr)
library(tibble)
library(ggplot2)

convert_csv <- function(path) {
    arranged_datum <- read.csv(path) %>%
        arrange(position)
    # arranged_datum%>%filter(!is.na(position) & !is.na(entropy))

    window_size <- 20
    step_size <- 5
    data_length <- nrow(arranged_datum)
    max_start <- (data_length - (data_length-20) %% 5) - 19
    positions <- vector("numeric")
    avg_entropy <- vector("numeric")


    for (start in seq(1, max_start, by = step_size)) {
        end <- start + window_size - 1
        avg_entropy <- c(avg_entropy, mean(arranged_datum$entropy[start:end]))
        positions <- c(positions, mean(arranged_datum$position[start:end]))
    }
    neo_datum <- tibble(
        positions = positions,
        avg_entropy = avg_entropy
    )
    return(neo_datum)
}

generate_graph <- function(tibble_) {
    p1 <- tibble_%>%
        ggplot(aes(x=positions,y=avg_entropy))+geom_line()+theme(aspect.ratio = 4/7)+labs(x="position",y="shannon entropy")
    ggsave("p1.png",p1)
    
}
# -*- coding: utf-8 -*-
"""database_analytics_energy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16fBNtqLYXmP7eAQtBAoGY5pE5v1mxXU6
"""

install.packages("sqldf")
library(sqldf)

data <- read.csv("/content/Energy_dataset.csv")

head(data)

selected_columns <- c("Surface.Area","Overall.Height","Heating.Load")

selected_data <- data[selected_columns]

print(selected_data)

filtered_data <- data[data$Surface.Area > 650,]

print(filtered_data)

aggregate_data <- data %>%
  group_by(cooling.load) %>%
  summarise(avg_surface_area = mean(surface.area))





install.packages("tidyverse")



library(tidyverse)



data <- read.csv("/content/Energy_dataset.csv")

head(data)

install.packages("dplyr")

library(dplyr)

aggregate_data <- data %>%
  group_by(Cooling.Load) %>%
  summarise(avg_surface_area = mean(Surface.Area))

print(aggregate_data)

filtered_data_cool <- data %>%
  filter(Cooling.Load>25)

print(filtered_data_cool)

selected_columns <- data %>%
  select(Cooling.Load,Surface.Area,Roof.Area)

print(selected_columns)

new_variable <- data %>%
  mutate(Area.per.Cooling.Load = Wall.Area/ Cooling.Load)

print(new_variable)

library(ggplot2)

ggplot(data aes(x = Wall.Area y= Cooling.Load)) +
  goem_point() +
    labs(title = "Scatter Plot", x = "Wall Area", y = "Cooling.Load")

install.packages("ggplot2")

library(ggplot2)

data <- read.csv("/content/Energy_dataset.csv")

ggplot(data, aes(x = Wall.Area, y= Cooling.Load)) +
  geom_point() +
    labs(title = "Scatter Plot", x = "Wall Area", y = "Cooling.Load")

install.packages('ggforce')

library(ggforce)

library(dplyr)
library(ggplot2)

data_transformed <- data %>%
      group_by(Relative.Compactness) %>%
      summarise(mean_cooling_load = mean(Cooling.Load))
ggplot(data_transformed, aes(x = Relative.Compactness, y = mean_cooling_load)) +
   geom_bar(stat = "identity") +
   labs(title = "Bar Plot", x = "Relative Compactness", y = "Mean Cooling Load")

library(tidyr)
library(ggplot2)

high_data <- data %>%
     gather(key = "area_type", value = "area_value", Wall.Area)

ggplot(high_data, aes(x = area_value, y = Cooling.Load, color = area_type)) +
     geom_line() +
     labs(title = "Line Plot", x = "Area", y = "Cooling Load")

"""# Section 2"""


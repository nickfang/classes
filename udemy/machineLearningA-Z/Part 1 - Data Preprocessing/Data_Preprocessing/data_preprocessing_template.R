# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')
dataset$Age = ifelse(is.na(dataset$Age),ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)),dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),ave(dataset$Salary, FUN = function(x) mean(x,na.rm = TRUE)),dataset$Salary)

View(dataset)

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)




# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Titanic Analytics Interpretations

## Missing Value Handling

The `age` column had approximately 19.87% missing values, so the missing values were replaced using the median. The `embarked` and `embark_town` columns had less than 5% missing values, so rows with missing values were removed. The `deck` column had approximately 77.22% missing values, so the column was dropped.

## Fare Distribution and Outliers

The mean fare was 32.10, while the median fare was 14.45 and the mode was 8.05. The fare skewness was 4.80, indicating a strongly right-skewed distribution caused by relatively high fare values. The IQR method identified 114 fare outliers and 65 age outliers.

## Survival Rate by Sex

Female passengers had a survival rate of approximately 74.04%, while male passengers had a survival rate of approximately 18.89%. This shows a substantial difference in survival rates between the two sex groups in the cleaned Titanic dataset.

## Survival Rate by Passenger Class

First-class passengers had a survival rate of approximately 62.62%, second-class passengers had a survival rate of approximately 47.28%, and third-class passengers had a survival rate of approximately 24.24%. The survival rate therefore varied across passenger classes.

## Survival Rate by Sex and Passenger Class

Female passengers had higher survival rates than male passengers across all three passenger classes. Female survival rates were approximately 96.74% in first class, 92.11% in second class, and 50.00% in third class. Male survival rates were approximately 36.89% in first class, 15.74% in second class, and 13.54% in third class.

## Correlation Analysis

The strongest absolute correlation was between `pclass` and `fare` (r = -0.548), indicating a moderate negative relationship between passenger class number and fare.

The second strongest absolute correlation was between `sibsp` and `parch` (r = 0.415), indicating a moderate positive relationship between the number of siblings/spouses and parents/children travelling with a passenger.

## Multivariate Chart 1 — Survival Rate by Sex and Passenger Class

The chart shows that female passengers had higher survival rates than male passengers across all three passenger classes. Female survival was highest in first class and second class, while it was lower in third class. Male passengers had much lower survival rates, especially in second and third class.

## Multivariate Chart 2 — Age Distribution by Sex and Survival

The chart compares the age distribution of passengers across sex and survival groups. It helps show how passenger age varied between survivors and non-survivors for females and males. The distribution also allows comparison of age patterns across the two survival outcomes.

## Multivariate Chart 3 — Fare Distribution by Passenger Class and Survival

The chart compares fare distributions across passenger classes for survivors and non-survivors. It shows that fare values vary substantially between passenger classes, with higher fares generally associated with first-class passengers. The chart also shows differences in fare distributions between the survival groups.

## Multivariate Chart 4 — Age vs Fare by Survival and Sex

The scatter plot shows the relationship between passenger age and fare while distinguishing passengers by survival status and sex. It provides a multivariate view of how age, fare, sex, and survival outcome are distributed together. The plot also shows that fare values are concentrated at lower levels for many passengers, while a smaller number of passengers paid substantially higher fares.

## Z-Score Standardization

Z-score standardization was performed on the `age` and `fare` variables as an exploratory analysis. After standardization, the variables were centered around a mean of approximately 0 and scaled to a standard deviation of approximately 1. This standardized data was not used as input to the final modeling pipeline.
## Random Forest GridSearchCV

GridSearchCV identified a Random Forest configuration with `max_depth=5`, `max_features='sqrt'`, and `n_estimators=100`. The best cross-validation F1 score for this configuration was approximately 0.749. The corresponding Random Forest model achieved an OOB score of approximately 0.827 on the training data.
## Residual Analysis

The residual plot shows that the residual spread increases as the predicted fare increases. The residuals are closely clustered around zero for lower predicted fare values, while higher predicted fares show much larger positive and negative residuals. This changing spread indicates the presence of heteroscedasticity in the regression errors. Therefore, the regression model does not maintain constant error variance across all predicted fare values.
## Regression Results

The Random Forest regression model produced an MAE of 15.36 and an RMSE of 41.61. The R² value was -0.119 and the Adjusted R² value was -0.178. These negative R² values indicate that the selected features did not explain the fare variation well on the test data.
## Classifier Model Comparison

Three classification models were evaluated using the same stratified train-test split.

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.804 | 0.793 | 0.667 | 0.724 | 0.844 |
| Decision Tree | 0.765 | 0.755 | 0.580 | 0.656 | 0.797 |
| Random Forest | 0.816 | 0.800 | 0.696 | 0.744 | 0.829 |

Random Forest achieved the highest accuracy, precision, recall, and F1 score among the three models. Logistic Regression achieved the highest ROC-AUC value. Decision Tree produced lower values across the main classification metrics compared with the other two models.

## Class Imbalance Comparison

Three approaches were compared: the baseline Logistic Regression model, class-weighted Logistic Regression, and SMOTE-based Logistic Regression.

| Method | Precision | Recall | F1 |
|---|---:|---:|---:|
| Baseline | 0.793 | 0.667 | 0.724 |
| Class Weight Balanced | 0.730 | 0.783 | 0.755 |
| SMOTE | 0.740 | 0.783 | 0.761 |

The baseline model had the highest precision, but its recall was lower. Both class weighting and SMOTE increased recall from 0.667 to 0.783, meaning more positive cases were identified. SMOTE produced the highest F1 score of 0.761 among the three approaches, while class weighting produced an F1 score of 0.755.

## Final Classifier Recommendation

Based on the evaluated test-set metrics, Random Forest provides the highest accuracy and F1 score among the three tested classifiers. Its precision and recall are also slightly higher than those of Logistic Regression. Logistic Regression has the highest ROC-AUC value, showing strong ranking performance. The final saved pipeline therefore uses the selected Random Forest configuration identified during the model development process.
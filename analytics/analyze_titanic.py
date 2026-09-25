import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.to_csv("analytics/titanic.csv", index=False)

print("Titanic dataset loaded successfully")
print("\nDataset info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nDescriptive statistics:")
print(df.describe())

print("\nMissing values percentage:")
print(df.isnull().mean() * 100)
missing_percent = df.isnull().mean() * 100

print("\nMissing value handling:")

for column in df.columns:
    percentage = missing_percent[column]

    if percentage < 5:
        print(column, "-> Drop rows")
    elif percentage <= 30:
        print(column, "-> Impute")
    else:
        print(column, "-> Drop column")
        df = df.dropna(subset=["embarked", "embark_town"])

df["age"] = df["age"].fillna(df["age"].median())

df = df.drop(columns=["deck"])

print("\nAfter missing value handling:")
print(df.isnull().sum())
print("\nNew shape:", df.shape)
import matplotlib.pyplot as plt

plt.figure()
plt.hist(df["age"], bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.savefig("analytics/age_histogram.png")
plt.close()

plt.figure()
plt.hist(df["fare"], bins=20)
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.title("Fare Distribution")
plt.savefig("analytics/fare_histogram.png")
plt.close()

plt.figure()
plt.boxplot(df["age"])
plt.ylabel("Age")
plt.title("Age Boxplot")
plt.savefig("analytics/age_boxplot.png")
plt.close()

plt.figure()
plt.boxplot(df["fare"])
plt.ylabel("Fare")
plt.title("Fare Boxplot")
plt.savefig("analytics/fare_boxplot.png")
plt.close()

age_q1 = df["age"].quantile(0.25)
age_q3 = df["age"].quantile(0.75)
age_iqr = age_q3 - age_q1
age_lower = age_q1 - 1.5 * age_iqr
age_upper = age_q3 + 1.5 * age_iqr

fare_q1 = df["fare"].quantile(0.25)
fare_q3 = df["fare"].quantile(0.75)
fare_iqr = fare_q3 - fare_q1
fare_lower = fare_q1 - 1.5 * fare_iqr
fare_upper = fare_q3 + 1.5 * fare_iqr

age_outliers = df[
    (df["age"] < age_lower) | (df["age"] > age_upper)
]

fare_outliers = df[
    (df["fare"] < fare_lower) | (df["fare"] > fare_upper)
]

print("\nIQR Outlier Analysis:")
print("Age outliers:", len(age_outliers))
print("Fare outliers:", len(fare_outliers))

print("\nFare Statistics:")
print("Mean:", df["fare"].mean())
print("Median:", df["fare"].median())
print("Mode:", df["fare"].mode()[0])
print("Skewness:", df["fare"].skew())
print("\nSurvival Rate by Sex:")
print(df.groupby("sex", observed=True)["survived"].mean())

print("\nSurvival Rate by Passenger Class:")
print(df.groupby("pclass", observed=True)["survived"].mean())

print("\nSurvival Rate by Sex and Passenger Class:")
print(
    df.groupby(
        ["sex", "pclass"],
        observed=True
    )["survived"].mean()
)
corr_columns = ["survived", "pclass", "age", "sibsp", "parch", "fare"]

corr_matrix = df[corr_columns].corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Titanic Correlation Matrix")
plt.savefig("analytics/correlation_heatmap.png")
plt.close()

print("\nCorrelation heatmap saved successfully.")
plt.figure(figsize=(8, 6))

sns.barplot(
    data=df,
    x="pclass",
    y="survived",
    hue="sex"
)

plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Sex and Passenger Class")
plt.ylim(0, 1)

plt.savefig("analytics/survival_by_sex_class.png")
plt.close()

print("\nMultivariate Chart 1 saved successfully.")
plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="sex",
    y="age",
    hue="survived"
)

plt.xlabel("Sex")
plt.ylabel("Age")
plt.title("Age Distribution by Sex and Survival")

plt.savefig("analytics/age_sex_survival.png")
plt.close()

print("\nMultivariate Chart 2 saved successfully.")
plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="pclass",
    y="fare",
    hue="survived"
)

plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.title("Fare Distribution by Passenger Class and Survival")

plt.savefig("analytics/fare_class_survival.png")
plt.close()

print("\nMultivariate Chart 3 saved successfully.")
plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="age",
    y="fare",
    hue="survived",
    style="sex"
)

plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare by Survival and Sex")

plt.savefig("analytics/age_fare_survival.png")
plt.close()

print("\nMultivariate Chart 4 saved successfully.")
from scipy.stats import zscore

age_before = df["age"].copy()
fare_before = df["fare"].copy()

df["age_zscore"] = zscore(df["age"])
df["fare_zscore"] = zscore(df["fare"])

print("\nZ-Score Standardization:")
print("Age before - Mean:", age_before.mean())
print("Age before - Std:", age_before.std())

print("Age after - Mean:", df["age_zscore"].mean())
print("Age after - Std:", df["age_zscore"].std())

print("Fare before - Mean:", fare_before.mean())
print("Fare before - Std:", fare_before.std())

print("Fare after - Mean:", df["fare_zscore"].mean())
print("Fare after - Std:", df["fare_zscore"].std())
from sklearn.model_selection import train_test_split

model_df = pd.read_csv("analytics/titanic.csv")

X = model_df[
    ["pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]
]

y = model_df["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain/Test Split:")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print("Training survival rate:", y_train.mean())
print("Testing survival rate:", y_test.mean())
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric_features = ["pclass", "age", "sibsp", "parch", "fare"]
categorical_features = ["sex", "embarked"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print("\nPreprocessing completed.")
print("Processed training shape:", X_train_processed.shape)
print("Processed testing shape:", X_test_processed.shape)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

logistic_model = LogisticRegression(max_iter=1000, random_state=42)

decision_tree_model = DecisionTreeClassifier(
    random_state=42,
    max_depth=5
)

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    oob_score=True
)

logistic_model.fit(X_train_processed, y_train)
decision_tree_model.fit(X_train_processed, y_train)
random_forest_model.fit(X_train_processed, y_train)

logistic_pred = logistic_model.predict(X_test_processed)
decision_tree_pred = decision_tree_model.predict(X_test_processed)
random_forest_pred = random_forest_model.predict(X_test_processed)

logistic_prob = logistic_model.predict_proba(X_test_processed)[:, 1]
decision_tree_prob = decision_tree_model.predict_proba(X_test_processed)[:, 1]
random_forest_prob = random_forest_model.predict_proba(X_test_processed)[:, 1]

print("\nModels trained successfully.")
print("Logistic Regression predictions:", len(logistic_pred))
print("Decision Tree predictions:", len(decision_tree_pred))
print("Random Forest predictions:", len(random_forest_pred))
print("Random Forest OOB Score:", random_forest_model.oob_score_)
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

models = {
    "Logistic Regression": (logistic_pred, logistic_prob),
    "Decision Tree": (decision_tree_pred, decision_tree_prob),
    "Random Forest": (random_forest_pred, random_forest_prob)
}

results = []

for name, (pred, prob) in models.items():
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    auc = roc_auc_score(y_test, prob)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1,
        "ROC_AUC": auc
    })

    print("\n", name)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)
    print("ROC-AUC:", auc)

results_df = pd.DataFrame(results)

print("\nModel Comparison:")
print(results_df)

results_df.to_csv(
    "analytics/classifier_comparison.csv",
    index=False
)

plt.figure(figsize=(8, 6))

for name, (pred, prob) in models.items():
    fpr, tpr, _ = roc_curve(y_test, prob)
    auc = roc_auc_score(y_test, prob)
    plt.plot(fpr, tpr, label=f"{name} AUC={auc:.3f}")

plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves")
plt.legend()

plt.savefig("analytics/roc_curves.png")
plt.close()

print("\nROC curves saved successfully.")
print("Classifier comparison saved successfully.")
from sklearn.tree import plot_tree

feature_names = preprocessor.get_feature_names_out()

plt.figure(figsize=(20, 10))

plot_tree(
    decision_tree_model,
    feature_names=feature_names,
    class_names=["Not Survived", "Survived"],
    filled=True,
    max_depth=3,
    fontsize=8
)

plt.title("Decision Tree")
plt.savefig("analytics/decision_tree.png")
plt.close()

print("\nDecision tree plot saved successfully.")
from imblearn.over_sampling import SMOTE

baseline_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

balanced_model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    random_state=42
)

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train_processed,
    y_train
)

smote_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

baseline_model.fit(X_train_processed, y_train)
balanced_model.fit(X_train_processed, y_train)
smote_model.fit(X_train_smote, y_train_smote)

baseline_pred = baseline_model.predict(X_test_processed)
balanced_pred = balanced_model.predict(X_test_processed)
smote_pred = smote_model.predict(X_test_processed)

imbalance_results = []

for name, pred in [
    ("Baseline", baseline_pred),
    ("Class Weight Balanced", balanced_pred),
    ("SMOTE", smote_pred)
]:
    imbalance_results.append({
        "Method": name,
        "Precision": precision_score(y_test, pred),
        "Recall": recall_score(y_test, pred),
        "F1": f1_score(y_test, pred)
    })

imbalance_df = pd.DataFrame(imbalance_results)

print("\nClass Imbalance Comparison:")
print(imbalance_df)

imbalance_df.to_csv(
    "analytics/imbalance_comparison.csv",
    index=False
)

print("\nImbalance comparison saved successfully.")
from sklearn.model_selection import GridSearchCV

rf_grid = RandomForestClassifier(
    random_state=42,
    oob_score=True
)

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 5, 10],
    "max_features": ["sqrt", "log2"]
}

grid_search = GridSearchCV(
    estimator=rf_grid,
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1
)

grid_search.fit(X_train_processed, y_train)

best_rf = grid_search.best_estimator_

print("\nRandom Forest GridSearchCV:")
print("Best Parameters:")
print(grid_search.best_params_)

print("Best Cross-Validation F1:", grid_search.best_score_)

print("Best Random Forest OOB Score:", best_rf.oob_score_)
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

reg_df = pd.read_csv("analytics/titanic.csv")

reg_features = [
    "pclass",
    "age",
    "sibsp",
    "parch",
    "sex",
    "embarked"
]

X_reg = reg_df[reg_features]
y_reg = reg_df["fare"]

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)

reg_numeric_features = ["pclass", "age", "sibsp", "parch"]
reg_categorical_features = ["sex", "embarked"]

reg_numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

reg_categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

reg_preprocessor = ColumnTransformer([
    ("numeric", reg_numeric_pipeline, reg_numeric_features),
    ("categorical", reg_categorical_pipeline, reg_categorical_features)
])

X_reg_train_processed = reg_preprocessor.fit_transform(X_reg_train)
X_reg_test_processed = reg_preprocessor.transform(X_reg_test)

print("\nRegression data prepared.")
print("Regression training samples:", X_reg_train.shape[0])
print("Regression testing samples:", X_reg_test.shape[0])
regression_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

regression_model.fit(
    X_reg_train_processed,
    y_reg_train
)

fare_pred = regression_model.predict(
    X_reg_test_processed
)

mae = mean_absolute_error(y_reg_test, fare_pred)
rmse = mean_squared_error(y_reg_test, fare_pred) ** 0.5
r2 = r2_score(y_reg_test, fare_pred)

n = len(y_reg_test)
p = X_reg_test_processed.shape[1]

adjusted_r2 = 1 - (
    (1 - r2) * (n - 1) / (n - p - 1)
)

print("\nRegression Results:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)
print("Adjusted R2:", adjusted_r2)
residuals = y_reg_test - fare_pred

plt.figure(figsize=(8, 6))

plt.scatter(
    fare_pred,
    residuals,
    alpha=0.6
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Predicted Fare")
plt.ylabel("Residuals")
plt.title("Residual Plot — Fare Regression")

plt.savefig("analytics/fare_residual_plot.png")
plt.close()

print("\nResidual plot saved successfully.")
import joblib

final_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        max_features="sqrt",
        random_state=42,
        oob_score=True
    ))
])

final_pipeline.fit(X_train, y_train)

joblib.dump(
    final_pipeline,
    "analytics/titanic_classifier_pipeline.joblib"
)

print("\nFinal pipeline saved successfully.")

loaded_pipeline = joblib.load(
    "analytics/titanic_classifier_pipeline.joblib"
)

raw_input = pd.DataFrame([{
    "pclass": 2,
    "sex": "female",
    "age": 25,
    "sibsp": 0,
    "parch": 0,
    "fare": 30.0,
    "embarked": "S"
}])

prediction = loaded_pipeline.predict(raw_input)

print("Raw input prediction:", prediction)
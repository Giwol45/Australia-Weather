# Weather Australia

This repository contains the data preprocessing, exploratory data analysis (EDA), and dataset preparation workflow for predicting whether it will rain tomorrow in Australia based on historical weather records.

---

## Project Overview

The objective of this project is to clean, transform, and analyze daily weather metrics to prepare a high-quality dataset for machine learning classification models. 

* **Dataset Size:** 41,564 rows × 23 columns (post-cleaning)
* **Target Variable:** `RainTomorrow` (Binary Classification: `Yes` / `No`)

---

##  Data Preprocessing & Workflow Steps

1. **Outlier Removal**
   * Handled extreme values across numerical features using the Interquartile Range (IQR) method.

2. **Feature Scaling**
   * Applied `StandardScaler` to numerical variables to center their distribution around a mean of 0 with unit variance.

3. **Duplicate & Missing Value Handling**
   * Verified zero remaining duplicate rows and zero missing values across all 23 columns.

4. **Categorical Feature Encoding**
   * Applied `LabelEncoder` to convert text-based variables (e.g., `Location`, `WindGustDir`, `RainToday`, `RainTomorrow`) into integer representations without expanding feature dimensions.

5. **Exploratory Data Analysis (EDA)**
   * **Distributions:** Temperature features (`MinTemp`, `MaxTemp`, `Temp9am`) displayed balanced near-normal distributions, while features like `Rainfall` showed heavy right-skewness.
   * **Feature Correlation:** Correlation matrix analysis revealed that **`Humidity3pm`** (humidity at 3 PM) is the strongest linear predictor for the target variable `RainTomorrow`.

6. **Dataset Splitting**
   * Split features ($X$) and target ($y$) using `train_test_split` with an 80:20 train-test ratio:
     * **Training Set:** 33,251 samples
     * **Testing Set:** 8,313 samples

---

##  Tech Stack & Libraries

* **Language:** Python
* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Machine Learning & Preprocessing:** `scikit-learn` (`StandardScaler`, `LabelEncoder`, `train_test_split`)

---

##  How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/weather-prediction-preprocessing.git
   cd weather-prediction-preprocessing
   ```

2. **Install required dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

3. **Run the Notebook/Script:**
   Open and execute `notebook.ipynb` or run the Python script to reproduce the preprocessing steps.

---

##  Summary of Results

| Metric / Stage | Details |
| :--- | :--- |
| **Cleaned Dataset Size** | 41,564 rows × 23 columns |
| **Top Target Predictor** | `Humidity3pm` |
| **Train / Test Ratio** | 80% / 20% |
| **Train Set Size** | 33,251 rows |
| **Test Set Size** | 8,313 rows |

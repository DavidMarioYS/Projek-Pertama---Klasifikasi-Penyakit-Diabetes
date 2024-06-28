# -*- coding: utf-8 -*-
"""Projek Pertama - Klasifikasi Penyakit Diabetes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rfbwYDA_yb9zaRU22ibQM7uSeUwrot-e

---
# **Projek Pertama - Klasifikasi Penyakit Diabetes**


---
Author : `David Mario Yohanes Samosir`

<h1> <b> Domain Proyek </b> </h1>
<hr>
<h3> Latar Belakang </h3>

Diabetes merupakan salah satu penyakit kronis yang paling umum di dunia, yang terjadi ketika tubuh tidak dapat secara efektif mengatur kadar gula darah. Deteksi dini dan pengelolaan yang tepat sangat penting untuk mencegah komplikasi serius. Dalam konteks ini, proyek klasifikasi diabetes dengan menggunakan data kesehatan pasien dapat memberikan wawasan berharga dan membantu dalam pengambilan keputusan medis yang lebih baik.

**Mengapa dan Bagaimana Masalah Harus Diselesaikan?** :
- **Meningkatkan Kesehatan Masyarakat**: Dengan deteksi dini, pasien dapat menerima perawatan lebih awal, mengurangi risiko komplikasi.
- **Mengurangi Biaya Perawatan Kesehatan**: Mengelola diabetes lebih awal dapat mengurangi biaya jangka panjang yang terkait dengan komplikasi.
- **Mendukung Penelitian Medis**: Data yang dihasilkan dapat digunakan untuk penelitian lebih lanjut dalam memahami faktor risiko dan pengelolaan diabetes.

<h3> Referensi </h3>

- "Diabetes: A Global Epidemic and Its Impact" - World Health Organization

- Apriyani, H., & Kurniati, K. (2020). Perbandingan Metode Naïve Bayes Dan Support Vector Machine Dalam Klasifikasi Penyakit Diabetes Melitus. Journal of Information Technology Ampera, 1(3), 133–143. https://doi.org/10.51519/journalita.volume1.isssue3.year2020.page133-143

<h1> <b> Business Understanding </b> </h1>
<hr>
<h3> <b> Problem Statements </b> </h3>

1. Bagaimana kita dapat membangun model yang akurat untuk memprediksi apakah seorang pasien menderita diabetes berdasarkan fitur-fitur medis yang tersedia?
2. Fitur mana yang paling berpengaruh dalam menentukan diagnosis diabetes?
3. Bagaimana cara mengoptimalkan model untuk meningkatkan akurasi dan efektivitas prediksi?

<h3> <b> Goals </b> </h3>

1. Mengembangkan model machine learning yang mampu memprediksi dengan akurasi tinggi apakah seorang pasien memiliki diabetes.
2. Mengidentifikasi dan mengurutkan fitur-fitur yang memiliki dampak terbesar terhadap prediksi diabetes.
3. Melakukan tuning hyperparameter dan menggunakan teknik validasi untuk meningkatkan performa model.

<h3> <b> Solution Statements </b> </h3>

1. Membangun beberapa model klasifikasi seperti Logistic Regression, Decision Tree, dan Random Forest, lalu membandingkan performanya.
2. Menggunakan teknik feature importance untuk mengidentifikasi fitur-fitur yang paling berpengaruh.
3. Melakukan hyperparameter tuning menggunakan grid search atau random search untuk mengoptimalkan model terbaik.

<h1> <b> Data Understanding </b> </h1>
<hr>
<h3> <b> Informasi Mengenai Data </b> <h3>

Dataset yang digunakan dalam proyek ini adalah dataset diabetes yang terdiri dari 2000 entri pasien dengan 9 atribut. Atribut-atribut ini mencakup informasi seperti jumlah kehamilan, tingkat glukosa darah, tekanan darah, ketebalan kulit, kadar insulin, BMI (Body Mass Index), fungsi keturunan diabetes, usia, dan hasil akhir yang menunjukkan keberadaan diabetes (Outcome).

<h3> <b> Sumber Data </b> <h3>

Dataset ini diperoleh dari Kaggle [Diabetes](https://www.kaggle.com/datasets/sitirahmahbasri/data-penyakit-diabetes/code)

<h3> <b> Variabel-Variabel dalam Dataset </b> <h3>

Berikut adalah daftar variabel-variabel yang terdapat dalam dataset diabetes:

1. Pregnancies: Jumlah kehamilan yang pernah dialami oleh pasien.
2. Glucose: Kadar glukosa darah 2 jam saat tes toleransi glukosa.
3. BloodPressure: Tekanan darah diastolik (mm Hg).
4. SkinThickness: Ketebalan lipatan kulit trisep (mm).
5. Insulin: 2-Hour serum insulin (mu U/ml).
6. BMI: Indeks massa tubuh (weight in kg/(height in m)^2).
7. DiabetesPedigreeFunction: Fungsi keturunan diabetes.
8. Age: Usia pasien (tahun).
9. Outcome: Hasil akhir (0 untuk tidak menderita diabetes, 1 untuk menderita diabetes).

Instalasi Libraries
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from google.colab import files

"""Data Wrangling

Gathering Data
"""

# Mengunggah file dari komputer lokal
uploaded = files.upload()

# Contoh: Menyimpan file yang diunggah ke dalam file lokal di Colab
with open('diabetes.csv', 'wb') as f:
    f.write(uploaded['diabetes.csv'])

# Load Dataset
df = pd.read_csv('./diabetes.csv')

print(df.shape)

df

"""Assessing Data"""

df.isnull().sum()

df.duplicated().sum()

df.describe()

df.info()

# Jumlah Data Pregnancies
df.Pregnancies.value_counts()

# Jumlah Data Glucose
df.Glucose.value_counts()

# Jumlah Data BloodPressure
df.BloodPressure.value_counts()

# Jumlah Data SkinThickness
df.SkinThickness.value_counts()

# Jumlah Data Insulin
df.Insulin.value_counts()

# Jumlah Data BMI
df.BMI.value_counts()

# Jumlah Data DiabetesPedigreeFunction
df.DiabetesPedigreeFunction.value_counts()

# Jumlah Data Age
df.Age.value_counts()

# Jumlah Data Outcome
df.Outcome.value_counts()

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 6))
    sns.distplot(df[column].dropna(), kde=True)
    plt.title(f'Distribusi dari {column}')
    plt.show()

"""Cleaning Data"""

# Menghapus baris yang duplikat
df.drop_duplicates(inplace=True)
print("Jumlah nilai duplikat:", df.duplicated().sum())

df.shape

"""Exploratory Data Analysis (EDA)"""

df

# Histogram untuk melihat distribusi variabel
df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()

# Korelasi antar variabel
correlation = df.corr()
correlation

# Heatmap korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Heatmap Korelasi Antar Variabel')
plt.show()

# Scatter plot untuk melihat hubungan dua variabel
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Glucose', y='Insulin', data=df, hue='Outcome')
plt.title('Hubungan antara Glukosa dan Insulin')
plt.xlabel('Glukosa')
plt.ylabel('Insulin')
plt.legend(title='Outcome', loc='upper right', labels=['Non-Diabetes', 'Diabetes'])
plt.show()

# Menghitung jumlah sampel untuk setiap kelas target
class_counts = df['Outcome'].value_counts()

# Plot pie chart atau bar plot untuk distribusi kelas target
plt.figure(figsize=(6, 6))
class_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'salmon'])
plt.title('Distribusi Kelas Target (Outcome)')
plt.ylabel('')
plt.show()

# Menampilkan jumlah sampel untuk setiap kelas target
print(class_counts)

# Pairplot untuk melihat hubungan antar variabel secara keseluruhan
sns.pairplot(df, hue='Outcome', diag_kind='kde', markers=['o', 's'])
plt.suptitle('Pairplot untuk Melihat Hubungan Antar Variabel', y=1.02)
plt.show()

# Boxplot untuk melihat distribusi variabel terhadap Outcome
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title('Glukosa vs Outcome')

plt.subplot(2, 2, 2)
sns.boxplot(x='Outcome', y='BMI', data=df)
plt.title('BMI vs Outcome')

plt.subplot(2, 2, 3)
sns.boxplot(x='Outcome', y='Age', data=df)
plt.title('Usia vs Outcome')

plt.subplot(2, 2, 4)
sns.boxplot(x='Outcome', y='Insulin', data=df)
plt.title('Insulin vs Outcome')

plt.tight_layout()
plt.show()

# Scatter plot untuk melihat distribusi variabel utama (misalnya Glukosa, BMI) berdasarkan usia
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Age', y='Glucose', hue='Outcome', data=df)
plt.title('Hubungan Glukosa vs Usia dengan Outcome')
plt.xlabel('Usia')
plt.ylabel('Glukosa')
plt.legend(title='Outcome', loc='upper right', labels=['Non-Diabetes', 'Diabetes'])
plt.show()

# Misalkan jika dataset memiliki informasi Age
plt.figure(figsize=(12, 6))
sns.boxplot(x='Age', y='BMI', hue='Outcome', data=df)
plt.title('Perbandingan BMI Berdasarkan Age dengan Outcome')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.legend(title='Outcome', loc='upper right', labels=['Non-Diabetes', 'Diabetes'])
plt.show()

"""<h1> <b> Data Preparation </b> </h1>
<hr>
- Handling Missing Values: Mengatasi nilai yang hilang dengan mengisi dengan rata-rata atau median dari masing-masing kolom yang relevan. Hal ini penting agar tidak ada nilai yang hilang yang mempengaruhi kinerja model.

- Scaling Features: Melakukan penskalaan fitur menggunakan StandardScaler untuk memastikan semua fitur memiliki skala yang serupa. Ini membantu model Machine Learning untuk bekerja dengan lebih baik.

- Pembagian Dataset: Memisahkan dataset menjadi data latih (X_train, y_train) dan data uji (X_test, y_test) dengan rasio 80:20. Data latih digunakan untuk melatih model, sementara data uji digunakan untuk menguji performa model yang sudah dilatih.
"""

# 1. Handling Missing Values
# Mengganti nilai-nilai yang hilang dengan rata-rata atau median
df['Glucose'].fillna(df['Glucose'].mean(), inplace=True)
df['BloodPressure'].fillna(df['BloodPressure'].median(), inplace=True)
df['SkinThickness'].fillna(df['SkinThickness'].median(), inplace=True)
df['Insulin'].fillna(df['Insulin'].median(), inplace=True)
df['BMI'].fillna(df['BMI'].median(), inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
df.head()

# 2. Scaling Featurs
# Penskalaan fitur menggunakan StandardScaler
scaler = StandardScaler()
cols_to_scale = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

# 3. Pembagian Dataset
# Memisahkan dataset menjadi fitur (X) dan target (y)
X = df.drop('Outcome', axis=1)  # X berisi semua kolom kecuali 'Outcome'
y = df['Outcome']  # y berisi kolom 'Outcome' yang merupakan target atau label yang ingin diprediksi

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Menampilkan dimensi data latih dan data uji
print("Dimensi data latih:", X_train.shape)
print("Dimensi data uji:", X_test.shape)

"""<h1> <b> Modeling </b> </h1>
<hr>

<h3> 1. Memilih Model Machine Learning </h3>
Dalam tahap Modeling, kita memilih dan mengimplementasikan model-machine learning untuk menyelesaikan permasalahan klasifikasi diabetes. Model yang dipilih dalam proyek ini meliputi:

- Logistic Regression: Model ini cocok untuk masalah klasifikasi biner dan menggunakan fungsi logistik untuk memprediksi probabilitas keberadaan diabetes berdasarkan fitur-fitur medis yang tersedia.

- Decision Tree: Menggunakan struktur pohon keputusan untuk memisahkan data berdasarkan fitur-fitur, membuat keputusan berdasarkan aturan yang ditemukan dari data.

- Random Forest: Ensemble dari banyak Decision Tree yang bekerja bersama untuk meningkatkan akurasi dan mengurangi overfitting.

<h3> 2. Parameter yang Digunakan </h3>
Setiap model memiliki parameter yang dapat diatur untuk meningkatkan performa dan generalisasi:

- Logistic Regression: Parameter yang dapat diatur misalnya adalah regularisasi (C) untuk mengontrol kompleksitas model.

- Decision Tree: Parameter seperti kedalaman maksimum pohon (max_depth), jumlah minimum sampel di leaf node (min_samples_leaf), dan kriteria pemisahan (criterion) dapat diatur untuk mengoptimalkan pembangunan pohon.

- Random Forest: Selain parameter dari Decision Tree, Random Forest juga mempertimbangkan jumlah pohon (n_estimators) dan jumlah fitur yang dipertimbangkan dalam setiap split (max_features).

<h3> 3. Kelebihan dan Kekurangan Setiap Algoritma </h3>

1. Logistic Regression:

  - Kelebihan: Sederhana, mudah diinterpretasikan, cocok untuk dataset linier.
  - Kekurangan: Tidak dapat menangani hubungan non-linier secara langsung.

2. Decision Tree:

  - Kelebihan: Mudah diinterpretasikan, mampu menangani hubungan non-linier dan interaksi antar variabel.
  - Kekurangan: Rentan terhadap overfitting jika tidak diatur dengan baik, tidak stabil terhadap perubahan kecil dalam data.

3. Random Forest:

  - Kelebihan: Mengurangi overfitting dibandingkan dengan Decision Tree tunggal, bisa digunakan untuk dataset besar dengan banyak fitur.
  - Kekurangan: Lebih sulit untuk diinterpretasikan dibandingkan Decision Tree tunggal, membutuhkan waktu lebih lama untuk melatih karena ensemble dari banyak pohon.
"""

# 1. Logistic Regression

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Define parameter grid
param_grid_logreg = {'C': [0.01, 0.1, 1, 10, 100]}

# Inisialisasi GridSearchCV untuk Logistic Regression
logreg_grid = GridSearchCV(LogisticRegression(random_state=42), param_grid_logreg, cv=5, scoring='accuracy', n_jobs=-1)

# Melatih model dengan hyperparameter tuning
logreg_grid.fit(X_train, y_train)

# Model terbaik setelah tuning
best_logreg_model = logreg_grid.best_estimator_

# Menampilkan parameter terbaik
print("Parameter terbaik untuk Logistic Regression:", logreg_grid.best_params_)

# 2. Decision Tree

from sklearn.tree import DecisionTreeClassifier

# Define parameter grid
param_grid_dt = {
    'max_depth': [None, 10, 20, 30, 40, 50],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Inisialisasi GridSearchCV untuk Decision Tree
dt_grid = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid_dt, cv=5, scoring='accuracy', n_jobs=-1)

# Melatih model dengan hyperparameter tuning
dt_grid.fit(X_train, y_train)

# Model terbaik setelah tuning
best_dt_model = dt_grid.best_estimator_

# Menampilkan parameter terbaik
print("Parameter terbaik untuk Decision Tree:", dt_grid.best_params_)

# 3. Random Forest

from sklearn.ensemble import RandomForestClassifier

# Define parameter grid
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt']
}

# Inisialisasi GridSearchCV untuk Random Forest
rf_grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring='accuracy', n_jobs=-1)

# Melatih model dengan hyperparameter tuning
rf_grid.fit(X_train, y_train)

# Model terbaik setelah tuning
best_rf_model = rf_grid.best_estimator_

# Menampilkan parameter terbaik
print("Parameter terbaik untuk Random Forest:", rf_grid.best_params_)

"""Dari hasil hyperparameter tuning yang didapatkan:

1. Logistic Regression: Parameter terbaik adalah C=1.
2. Decision Tree: Parameter terbaik adalah `max_depth=None`, `min_samples_leaf=4`, dan `min_samples_split=10`.
3. Random Forest: Parameter terbaik adalah `'max_depth': None`, `'max_features': 'sqrt'`, `'min_samples_leaf': 2`, `'min_samples_split': 10`, `'n_estimators': 50`

Berdasarkan hasil parameter terbaik, memilih Random Forest sebagai model terbaik bisa menjadi pilihan yang baik. Alasannya adalah:
- Performa yang baik: Random Forest umumnya memberikan performa yang solid dan stabil karena menggabungkan beberapa pohon keputusan untuk mengurangi variansinya.

- Mengatasi overfitting: Dengan menggunakan teknik averaging dari beberapa pohon, Random Forest cenderung lebih tahan terhadap overfitting dibandingkan dengan Decision Tree tunggal.

- Fleksibilitas dalam parameter: Random Forest memberikan fleksibilitas dalam menentukan jumlah pohon (n_estimators) dan bagaimana fitur dipilih (max_features), meskipun ada peringatan untuk mengubah max_features menjadi 'sqrt' dari 'auto' untuk menghindari peringatan masa depan.

<h1> <b> Evaluation </b> </h1>
<hr>
Dalam konteks klasifikasi untuk proyek ini, kita akan menggunakan beberapa metrik evaluasi yang umum digunakan:

1. Accuracy (Akurasi): Persentase dari prediksi yang benar secara keseluruhan.

  $Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$.

  - TP: True Positives (prediksi benar positif)
  - TN: True Negatives (prediksi benar negatif)
  - FP: False Positives (prediksi salah positif)
  - FN: False Negatives (prediksi salah negatif)

2. Precision: Persentase dari prediksi positif yang benar.
  
  $Precision = \frac{TP}{TP + FP} $

3. Recall (Sensitivity atau True Positive Rate): Persentase dari kasus positif yang berhasil diprediksi.
  
  $Recall = \frac{TP}{TP + FN} $

4. F1 Score: Harmonic mean dari Precision dan Recall, memberikan keseimbangan antara kedua metrik ini.

  $ \text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} $
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
# Fungsi untuk menampilkan hasil evaluasi
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    print(f"{model_name}:")
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(matrix)
    print()

# Evaluasi model Logistic Regression
evaluate_model(best_logreg_model, X_test, y_test, "Logistic Regression")

y_pred_logreg = best_logreg_model.predict(X_test)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
precision_logreg = precision_score(y_test, y_pred_logreg)
recall_logreg = recall_score(y_test, y_pred_logreg)
f1_logreg = f1_score(y_test, y_pred_logreg)

print("Evaluation Metrics for Logistic Regression:")
print(f"Accuracy: {accuracy_logreg:.2f}")
print(f"Precision: {precision_logreg:.2f}")
print(f"Recall: {recall_logreg:.2f}")
print(f"F1 Score: {f1_logreg:.2f}")
print()

# Evaluasi model Decision Tree
evaluate_model(best_dt_model, X_test, y_test, "Decision Tree")

y_pred_dt = best_dt_model.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
precision_dt = precision_score(y_test, y_pred_dt)
recall_dt = recall_score(y_test, y_pred_dt)
f1_dt = f1_score(y_test, y_pred_dt)

print("Evaluation Metrics for Decision Tree:")
print(f"Accuracy: {accuracy_dt:.2f}")
print(f"Precision: {precision_dt:.2f}")
print(f"Recall: {recall_dt:.2f}")
print(f"F1 Score: {f1_dt:.2f}")
print()

# Evaluasi model Random Forest
evaluate_model(best_rf_model, X_test, y_test, "Random Forest")

# Evaluasi model Random Forest
y_pred_rf = best_rf_model.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf)
recall_rf = recall_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)

print("Evaluation Metrics for Random Forest:")
print(f"Accuracy: {accuracy_rf:.2f}")
print(f"Precision: {precision_rf:.2f}")
print(f"Recall: {recall_rf:.2f}")
print(f"F1 Score: {f1_rf:.2f}")

"""Penjelasan Hasil Proyek Berdasarkan Metrik Evaluasi
*Logistic Regression*: Memberikan akurasi yang baik, tetapi memiliki recall yang lebih rendah dibandingkan *Random Forest*, yang berarti lebih banyak kasus positif yang terlewatkan.

- Decision Tree: Menunjukkan performa yang cukup baik tetapi sedikit lebih rendah dibandingkan Logistic Regression dan Random Forest dalam hal akurasi dan F1 score.

- Random Forest: Memiliki akurasi yang paling tinggi dan F1 score yang lebih baik dibandingkan dua model lainnya. Hal ini menunjukkan bahwa Random Forest mampu memberikan keseimbangan yang baik antara precision dan recall dalam memprediksi keberadaan diabetes.

- Dengan demikian, berdasarkan evaluasi metrik yang digunakan, Random Forest dipilih sebagai model terbaik untuk proyek ini karena memberikan performa yang lebih baik dalam memprediksi keberadaan diabetes berdasarkan fitur-fitur medis yang tersedia.
"""
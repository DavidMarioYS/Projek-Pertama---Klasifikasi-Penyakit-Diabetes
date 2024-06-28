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

<h1> <b> Data Preparation </b> </h1>
<hr>

- Handling Missing Values: Mengatasi nilai yang hilang dengan mengisi dengan rata-rata atau median dari masing-masing kolom yang relevan. Hal ini penting agar tidak ada nilai yang hilang yang mempengaruhi kinerja model.

- Scaling Features: Melakukan penskalaan fitur menggunakan StandardScaler untuk memastikan semua fitur memiliki skala yang serupa. Ini membantu model Machine Learning untuk bekerja dengan lebih baik.

- Pembagian Dataset: Memisahkan dataset menjadi data latih (X_train, y_train) dan data uji (X_test, y_test) dengan rasio 80:20. Data latih digunakan untuk melatih model, sementara data uji digunakan untuk menguji performa model yang sudah dilatih.

<h1> <b> Modeling </b> </h1>
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

  Dari hasil hyperparameter tuning yang didapatkan:

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

  $$F1 Score = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} $$

Penjelasan Hasil Proyek Berdasarkan Metrik Evaluasi
*Logistic Regression*: Memberikan akurasi yang baik, tetapi memiliki recall yang lebih rendah dibandingkan *Random Forest*, yang berarti lebih banyak kasus positif yang terlewatkan.

- Decision Tree: Menunjukkan performa yang cukup baik tetapi sedikit lebih rendah dibandingkan Logistic Regression dan Random Forest dalam hal akurasi dan F1 score.

- Random Forest: Memiliki akurasi yang paling tinggi dan F1 score yang lebih baik dibandingkan dua model lainnya. Hal ini menunjukkan bahwa Random Forest mampu memberikan keseimbangan yang baik antara precision dan recall dalam memprediksi keberadaan diabetes.

- Dengan demikian, berdasarkan evaluasi metrik yang digunakan, Random Forest dipilih sebagai model terbaik untuk proyek ini karena memberikan performa yang lebih baik dalam memprediksi keberadaan diabetes berdasarkan fitur-fitur medis yang tersedia.

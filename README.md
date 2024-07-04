# Laporan Proyek Machine Learning - David Mario Yohanes Samosir

## Domain Proyek: Kesehatan
---
Proyek ini berfokus pada pengembangan model klasifikasi untuk deteksi dini dan pengelolaan penyakit diabetes. Diabetes merupakan salah satu penyakit kronis yang paling umum di dunia, terjadi ketika tubuh tidak dapat secara efektif mengatur kadar gula darah. Menurut Apriyani, H., & Kurniati, K. (2020), deteksi dini dan pengelolaan yang tepat sangat penting untuk mencegah komplikasi serius.

Tujuan utama proyek ini adalah mengembangkan model klasifikasi yang dapat memprediksi keberadaan diabetes berdasarkan atribut medis. Hal ini penting karena dapat meningkatkan kesehatan masyarakat melalui intervensi medis yang lebih awal, mengurangi risiko komplikasi, dan meningkatkan kualitas hidup pasien. Selain itu, data yang dihasilkan dari model ini dapat mendukung penelitian medis lebih lanjut, membantu memahami faktor risiko, dan mengembangkan strategi pengelolaan yang lebih efektif.

Model klasifikasi seperti Logistic Regression, Decision Tree, dan Random Forest akan digunakan untuk menganalisis data medis pasien dan memprediksi kemungkinan keberadaan diabetes. Dengan memanfaatkan atribut-atribut medis seperti kadar glukosa, tekanan darah, dan BMI, model ini diharapkan dapat memberikan prediksi yang akurat. Hal ini memungkinkan deteksi dini dan pengelolaan yang lebih baik, sehingga pasien dapat menerima perawatan yang diperlukan lebih cepat.
Proyek ini mengacu pada penelitian terkini di bidang kesehatan, termasuk laporan dari World Health Organization tentang "Diabetes: A Global Epidemic and Its Impact" serta studi komparatif metode klasifikasi oleh Apriyani, H., & Kurniati, K. (2020) dalam "Perbandingan Metode Naïve Bayes Dan Support Vector Machine Dalam Klasifikasi Penyakit Diabetes Melitus".

#### Referensi
1. World Health Organization. "Diabetes: A Global Epidemic and Its Impact."
2. Apriyani, H., & Kurniati, K. (2020). Perbandingan Metode Naïve Bayes Dan Support Vector Machine Dalam Klasifikasi Penyakit Diabetes Melitus.

## Business Understanding

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- **Pernyataan Masalah 1**: Deteksi dini penyakit diabetes seringkali terlewatkan, menyebabkan komplikasi serius yang dapat dicegah dengan intervensi tepat waktu.

- **Pernyataan Masalah 2**: Kualitas hidup pasien diabetes dapat menurun drastis jika penyakit tidak dideteksi dan ditangani sejak dini.

### Goals

- **Jawaban Pernyataan Masalah 1**: Mengembangkan model klasifikasi yang dapat memprediksi keberadaan diabetes berdasarkan atribut medis untuk memungkinkan deteksi dini dan intervensi medis tepat waktu.

- **Jawaban Pernyataan Masalah 2**: Meningkatkan kualitas hidup pasien melalui pemantauan dan penanganan lebih awal dengan bantuan model klasifikasi yang akurat.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution Statements

#### Solution Statement 1:
**Solusi untuk Pernyataan Masalah 1: Deteksi Dini Diabetes**
- **Deskripsi Solusi**: Mengembangkan model klasifikasi menggunakan Logistic Regression, Decision Tree, dan Random Forest untuk memprediksi keberadaan diabetes berdasarkan atribut medis seperti glukosa darah, BMI, usia, dan lainnya.
- **Manfaat**: Model ini akan memungkinkan deteksi dini diabetes, mengidentifikasi individu dengan risiko tinggi, dan memberikan kesempatan untuk intervensi medis tepat waktu.
- **Tujuan**: Mengurangi kemungkinan terlewatnya deteksi dini diabetes yang dapat mengarah pada komplikasi serius.

#### Solution Statement 2:
**Solusi untuk Pernyataan Masalah 2: Meningkatkan Kualitas Hidup Pasien**
- **Deskripsi Solusi**: Mengimplementasikan model klasifikasi yang akurat untuk memantau pasien secara teratur berdasarkan prediksi diabetes.
- **Manfaat**: Dengan pemantauan yang lebih baik dan penanganan lebih awal, model ini akan membantu meningkatkan kualitas hidup pasien diabetes dengan mengelola kondisi mereka secara efektif.
- **Tujuan**: Mencegah penurunan drastis kualitas hidup yang sering terjadi akibat diabetes yang tidak terdeteksi atau terlambat ditangani.

### Evaluasi Solusi

- **Metode Evaluasi**: Menggunakan metrik evaluasi seperti akurasi, presisi, recall, dan F1-score untuk mengevaluasi performa ketiga model (Logistic Regression, Decision Tree, Random Forest) dalam memprediksi keberadaan diabetes.
- **Perbandingan Algoritma**: Membandingkan hasil dari ketiga algoritma untuk menentukan yang paling cocok dalam konteks deteksi dini dan manajemen diabetes.
- **Kesimpulan**: Memilih model yang paling baik dalam memenuhi tujuan deteksi dini dan meningkatkan kualitas hidup pasien, serta memberikan rekomendasi untuk implementasi lebih lanjut.

Dengan pendekatan ini (Logistic Regression, Decision Tree, dan Random Forest) didasarkan pada literatur yang ada dan praktik umum dalam machine learning untuk klasifikasi masalah kesehatan, diharapkan dapat memberikan solusi yang efektif dalam menangani masalah deteksi dini dan manajemen diabetes, serta memberikan landasan yang kuat untuk pengambilan keputusan dalam pengembangan solusi kesehatan yang lebih baik. Referensi penelitian seperti Apriyani & Kurniati (2020) membandingkan metode Naïve Bayes dan Support Vector Machine dalam klasifikasi diabetes, menunjukkan pentingnya menggunakan beberapa algoritma untuk menentukan model terbaik.

## Data Understanding

### Sumber Data
- **Dataset**: [Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/sitirahmahbasri/data-penyakit-diabetes/data).

### Informasi Data
- **Jumlah Data**: 2000 entri dengan 9 atribut.
- **Kondisi Data**: Semua kolom memiliki 2000 nilai non-null.
- **Tipe Data**: 
  - Terdapat 7 kolom bertipe data (`int64`) untuk atribut seperti kehamilan, glukosa, tekanan darah, ketebalan kulit, insulin, usia, dan outcome.
  - Terdapat 2 kolom bertipe data (`float64`) untuk atribut BMI dan fungsi keturunan diabetes.

### Atribut
1. **Kehamilan (Pregnancies)**
   - Definisi: Jumlah kali kehamilan yang dialami oleh pasien.
   - Satuan: Tidak berlaku (unitless).
   - Distribusi: Terbanyak adalah wanita dengan 1 kehamilan (356 entri), diikuti dengan wanita yang tidak pernah hamil (301 entri).
   - Insight: Banyak wanita dalam dataset ini memiliki sedikit kehamilan, dengan puncak di sekitar 1-3 kehamilan. Frekuensi kehamilan yang lebih tinggi (>10) jarang terjadi.


2. **Kadar Glukosa Darah (Glucose)**
   - Definisi: Konsentrasi glukosa dalam plasma darah pada tes saat puasa.
   - Satuan: mg/dL (miligram per desiliter).
   - Distribusi: Nilai glukosa darah paling umum adalah sekitar 99-102
   - Insight: Terdapat rentang yang luas untuk kadar glukosa, menunjukkan variasi yang signifikan di antara pasien. Kadar glukosa tinggi berkorelasi kuat dengan diabetes, jadi nilai tinggi pada atribut ini penting untuk diperhatikan.

3. **Tekanan Darah (BloodPressure)**
   - Definisi: Tekanan darah diastolik (saat jantung sedang istirahat).
   - Satuan: mmHg (milimeter raksa).
   - Distribusi: Nilai paling umum sekitar 70-80 mm Hg.
   - Insight: Distribusi tekanan darah menunjukkan banyak pasien berada dalam kisaran normal, tetapi ada nilai yang tidak mungkin (seperti 0) yang perlu diperiksa lebih lanjut untuk kesalahan atau nilai yang hilang yang mungkin tidak ditandai dengan benar.

4. **Ketebalan Kulit (SkinThickness)**
   - Definisi: Ketebalan lipatan kulit trisep.
   - Satuan: mm (milimeter).
   - Distribusi: Banyak nilai 0 yang tidak masuk akal untuk ketebalan kulit.
   - Insight: Nilai 0 mungkin menunjukkan data yang hilang atau tidak tercatat. Penting untuk menangani nilai-nilai ini, mungkin dengan imputasi atau pembersihan data.

5. **Insulin**
   - Definisi: Konsentrasi insulin serum pada tes saat puasa.
   - Satuan: mu U/mL (mikro unit per mililiter).
   - Distribusi: Sebagian besar nilai insulin adalah 0, yang mungkin menunjukkan data yang hilang.
   - Insight: Data yang hilang pada insulin cukup signifikan. Sama seperti ketebalan kulit, penting untuk menangani nilai-nilai ini untuk analisis yang akurat.

6. **BMI (Body Mass Index)**
   - Definisi: Indeks massa tubuh, menghitung proporsi berat badan terhadap tinggi badan.
   - Satuan: kg/m² (kilogram per meter persegi).
   - Distribusi: Nilai paling umum sekitar 32.
   - Insight: BMI adalah indikator penting untuk obesitas, yang merupakan faktor risiko utama untuk diabetes. Beberapa nilai 0 mungkin perlu diperiksa dan ditangani.

7. **Fungsi Keturunan Diabetes (DiabetesPedigreeFunction)**
   - Definisi: Skor fungsi keturunan diabetes, menggambarkan seberapa besar risiko diabetes yang diwariskan dari keluarga.
   - Satuan: Tidak berlaku (unitless), skala relatif dari 0 sampai 1.
   - Distribusi: Nilai paling umum sekitar 0.2-0.3.
   - Insight: Menunjukkan kecenderungan genetik terhadap diabetes, dengan distribusi yang cukup tersebar, menunjukkan berbagai tingkat risiko genetik dalam populasi ini.

8. **Usia (Age)**
   - Definisi: Usia pasien.
   - Satuan: Tahun.
   - Distribusi: Paling umum pada usia 22 tahun.
   - Insight: Banyak pasien muda dalam dataset, dengan jumlah yang menurun seiring bertambahnya usia. Distribusi ini penting untuk memahami bagaimana usia mempengaruhi risiko diabetes.

9. **Hasil Akhir (Outcome)**
   - Definisi: Hasil akhir dari tes diabetes.
   - Nilai: 0 untuk tidak diabetes, 1 untuk diabetes.
   - Satuan: Tidak berlaku (unitless).
   - Distribusi: 1316 tidak diabetes, 684 diabetes.
   - Insight: Kelas tidak seimbang dengan lebih banyak pasien tanpa diabetes daripada dengan diabetes. Ini penting untuk dipertimbangkan dalam pembangunan model, karena model bisa condong pada prediksi kelas mayoritas.

### Deskripsi Statistik Singkat

| Atribut                   | Rata-rata | Median | Max  | Persentase Diabetes |
|---------------------------|-----------|--------|------|---------------------|
| **Pregnancies**           | 3.8       | 3.0    | 17.0 | -                   |
| **Glucose**               | 121.7     | 117.0  | 199.0| -                   |
| **BloodPressure**         | 69.1      | 70.0   | 122.0| -                   |
| **SkinThickness**         | 20.5      | 23.0   | 99.0 | -                   |
| **Insulin**               | 80.8      | 30.5   | 846.0| -                   |
| **BMI**                   | 32.0      | 32.1   | 67.1 | -                   |
| **DiabetesPedigreeFunction** | 0.474     | 0.372  | 2.42 | -                   |
| **Age**                   | 33.2      | 29.0   | 81.0 | -                   |
| **Outcome**               | -         | -      | -    | 35.8% (diabetes: 1, tidak diabetes: 0) |

### Analisa Berdasarkaan Matriks Korelasi
1. Pregnancies dengan:
  - Outcome: Korelasi positif sedang (0.220942), menunjukkan bahwa jumlah kehamilan yang lebih tinggi cenderung berkorelasi dengan peningkatan risiko diabetes.
  - Age: Korelasi positif kuat (0.536657), menunjukkan bahwa usia yang lebih tua cenderung berkorelasi dengan jumlah kehamilan yang lebih tinggi.
2. Glucose dengan:
  - Outcome: Korelasi positif kuat (0.453939), menunjukkan bahwa tingkat glukosa darah yang lebih tinggi berkorelasi dengan peningkatan risiko diabetes.
3. BMI (Body Mass Index) dengan:
  - Glucose: Korelasi positif sedang (0.239693), menunjukkan bahwa indeks massa tubuh yang lebih tinggi berkorelasi dengan kadar glukosa darah yang lebih tinggi.
  - BloodPressure: Korelasi positif sedang (0.272704), menunjukkan bahwa indeks massa tubuh yang lebih tinggi berkorelasi dengan tekanan darah yang lebih tinggi.
  - Outcome: Korelasi positif sedang (0.278123), menunjukkan bahwa indeks massa tubuh yang lebih tinggi berkorelasi dengan peningkatan risiko diabetes.
4. Age dengan:
  - Pregnancies: Korelasi positif kuat (0.536657), menunjukkan bahwa usia yang lebih tua cenderung berkorelasi dengan jumlah kehamilan yang lebih tinggi.
  - Glucose: Korelasi positif sedang (0.248673), menunjukkan bahwa usia yang lebih tua cenderung berkorelasi dengan kadar glukosa darah yang lebih tinggi.
  - BloodPressure: Korelasi positif sedang (0.242559), menunjukkan bahwa usia yang lebih tua cenderung berkorelasi dengan tekanan darah yang lebih tinggi.
5. SkinThickness dengan:
  - Insulin: Korelasi positif sedang (0.436080), menunjukkan bahwa ketebalan kulit yang lebih tinggi berkorelasi dengan konsentrasi insulin serum yang lebih tinggi.
  - BMI: Korelasi positif sedang (0.367853), menunjukkan bahwa ketebalan kulit yang lebih besar berkorelasi dengan indeks massa tubuh yang lebih tinggi.
6. Insulin dengan:
  - Glucose: Korelasi positif sedang (0.325135), menunjukkan bahwa konsentrasi insulin serum yang lebih tinggi berkorelasi dengan konsentrasi glukosa darah yang lebih tinggi.
  - BMI: Korelasi positif sedang (0.205365), menunjukkan bahwa konsentrasi insulin serum yang lebih tinggi berkorelasi dengan indeks massa tubuh yang lebih tinggi.
7. DiabetesPedigreeFunction dengan:
  - Outcome: Korelasi positif sedang (0.174688), menunjukkan bahwa skor fungsi keturunan diabetes yang lebih tinggi berkorelasi dengan peningkatan risiko diabetes.

### Korelasi Antara Fitur

Analisis Matriks Korelasi:

1. Korelasi dengan Variabel Target (Outcome):
   - Glucose memiliki korelasi tertinggi dengan Outcome (0.454), menunjukkan bahwa kadar glukosa darah adalah prediktor terkuat untuk diabetes dalam dataset ini.
   - BMI memiliki korelasi positif moderat (0.278) dengan Outcome, mengindikasikan bahwa indeks massa tubuh yang lebih tinggi cenderung terkait dengan risiko diabetes yang lebih besar.
   - Age (0.242) dan Pregnancies (0.221) juga menunjukkan korelasi positif yang cukup signifikan dengan Outcome, menandakan bahwa usia dan jumlah kehamilan juga berperan dalam risiko diabetes.

2. Korelasi Antar Fitur:
   - Pregnancies dan Age memiliki korelasi positif yang kuat (0.537), menunjukkan bahwa wanita yang lebih tua cenderung memiliki lebih banyak kehamilan.
   - Insulin dan Glucose menunjukkan korelasi positif moderat (0.325), yang masuk akal secara fisiologis karena insulin berperan dalam mengatur kadar glukosa darah.
   - SkinThickness dan Insulin memiliki korelasi positif moderat (0.436), yang mungkin menunjukkan hubungan antara ketebalan kulit dan tingkat insulin dalam tubuh.

3. Fitur dengan Korelasi Rendah terhadap Outcome:
   - BloodPressure (0.079) dan SkinThickness (0.076) memiliki korelasi yang sangat rendah dengan Outcome, menunjukkan bahwa mereka mungkin bukan prediktor yang kuat untuk diabetes dalam dataset ini.

4. Multikolinearitas:
   - Tidak ada fitur yang menunjukkan korelasi sangat tinggi satu sama lain (> 0.8), yang berarti multikolinearitas mungkin bukan masalah serius dalam dataset ini.

5. Insight untuk Feature Engineering:
   - Interaksi antara Glucose dan BMI mungkin bisa menjadi fitur yang berguna, mengingat keduanya memiliki korelasi yang cukup tinggi dengan Outcome.
   - Kombinasi Age dan Pregnancies juga bisa menjadi fitur yang menarik untuk dieksplorasi.

6. Implikasi untuk Pemodelan:
   - Model prediktif mungkin akan mendapat manfaat terbesar dari fitur Glucose, BMI, Age, dan Pregnancies.
   - Fitur seperti BloodPressure dan SkinThickness mungkin kurang penting dalam prediksi dan bisa dipertimbangkan untuk dihapus jika diperlukan penyederhanaan model.

7. Arah untuk Analisis Lebih Lanjut:
   - Meskipun DiabetesPedigreeFunction memiliki korelasi yang relatif rendah dengan Outcome (0.175), fitur ini mungkin masih penting secara klinis dan layak untuk dipertahankan dalam model.
   - Hubungan non-linear antara fitur-fitur ini dan Outcome mungkin perlu dieksplorasi lebih lanjut, mengingat beberapa korelasi yang lebih rendah dari yang diharapkan (misalnya, BloodPressure).

Kesimpulan:
Analisis korelasi ini memberikan wawasan berharga tentang hubungan antar variabel dalam dataset diabetes. Hal ini akan membantu dalam proses seleksi fitur, feature engineering, dan pemilihan model untuk tahap pemodelan selanjutnya.

## Data Preparation
- Data Wrangling - Assessing Data

  Pada tahap ini, kami memeriksa kualitas data awal. Hasilnya menunjukkan:
  - Tidak ada nilai yang hilang dalam dataset.
  - Terdapat 1256 data duplikat yang perlu ditangani.

- Data Wrangling - Cleaning Data

  Untuk meningkatkan kualitas data, kami melakukan pembersihan dengan menghapus data duplikat. Setelah proses ini:
  - Tidak ada lagi data duplikat dalam dataset.
  - Jumlah baris data berkurang, namun kualitas dan keunikan data terjaga.

- Exploratory Data Analysis (EDA)
  
  **1. Struktur Dataset**
  - Setelah pembersihan, dataset memiliki 744 baris dan 9 kolom.
  - Semua fitur memiliki tipe data yang sesuai dan tidak ada nilai yang hilang.
  
  **2. Analisis Statistik Deskriptif**
  - Memberikan gambaran umum tentang distribusi data di setiap fitur.
  - Contoh: rata-rata level glukosa adalah 120.89 dengan standar deviasi 31.94.
  
  **3. Analisis Fitur**
  - Pregnancies: Bervariasi dari 0 hingga 17, dengan frekuensi tertinggi pada nilai 1.
  - Glucose: Rentang dari 0 hingga 199, dengan modus pada nilai 100.
  - BloodPressure: Rentang dari 0 hingga 122, dengan modus pada nilai 70.
  - SkinThickness dan Insulin: Banyak nilai 0, mengindikasikan kemungkinan data hilang yang belum diimputasi.
  - BMI: Beberapa nilai 0 yang secara medis tidak mungkin, menunjukkan potensi data hilang.
  - DiabetesPedigreeFunction: Bervariasi dari 0.078 hingga 2.42.
  - Age: Rentang dari 21 hingga 81 tahun, dengan modus pada usia 22 tahun.
  - Outcome: 491 data non-diabetes dan 253 data diabetes, menunjukkan ketidakseimbangan kelas.
  
  **4. Analisis Korelasi**
  - Matriks korelasi digunakan untuk melihat hubungan antar fitur.
  - Glucose memiliki korelasi positif tertinggi dengan variabel target Outcome.
  - Fitur-fitur dengan korelasi tertinggi terhadap Outcome: Glucose, BMI, Age, dan Pregnancies.
  - Ini mengindikasikan fitur-fitur potensial sebagai prediktor kuat untuk klasifikasi diabetes.


Data Preparation untuk proyek ini akan berfokus pada beberapa aspek kunci:

1. **Penanganan nilai yang hilang**
   - Pada tahap ini, dilakukan pemeriksaan terhadap nilai yang hilang pada dataset. Setelah diteliti, tidak ditemukan nilai yang hilang pada dataset ini, sehingga tidak perlu dilakukan pengisian nilai kosong.
   - Proses: Dilakukan pemeriksaan terhadap nilai yang hilang di dataset menggunakan df.isnull().sum() dan kemudian menangani nilai yang hilang jika ditemukan.
   - Hasil: Tidak ditemukan nilai yang hilang di dataset.

2. **Normalisasi atau standardisasi fitur**
   - Fitur numerik seperti Glucose, BloodPressure, BMI, dan DiabetesPedigreeFunction dinormalisasi atau distandardisasi untuk memastikan skala yang seragam di antara fitur-fitur tersebut. Ini membantu model machine learning untuk konvergensi lebih cepat dan mengoptimalkan performa.
   - Proses: Fitur numerik seperti Glucose, BloodPressure, BMI, dan DiabetesPedigreeFunction dinormalisasi menggunakan metode Min-Max Scaling.
   - Hasil: Fitur-fitur numerik telah dinormalisasi ke dalam rentang 0-1.

3. **Feature engineering**
   - Akan dipertimbangkan pembuatan fitur baru berdasarkan pengetahuan domain, seperti kategorisasi BMI atau fitur interaksi Glucose-Insulin.
   - Proses: Melakukan feature engineering dengan mempertimbangkan pembuatan fitur baru seperti kategorisasi BMI atau fitur interaksi antara Glucose dan Insulin.
   - Hasil: Fitur-fitur baru yang relevan dengan domain telah ditambahkan untuk meningkatkan informasi yang dapat diekstrak dari data.

4. **Seleksi fitur**
   - Pemilihan fitur berdasarkan kekuatan hubungan linear antara setiap fitur dan variabel target ('Outcome'). 
   - Proses: Pemilihan fitur dilakukan berdasarkan korelasi dengan variabel target ('Outcome').
   - Hasil: Fitur yang dipilih untuk digunakan dalam model adalah ['Pregnancies', 'Glucose', 'BMI', 'Age'].

5. **Penanganan outlier**
   - Outlier pada fitur seperti Glucose, BMI, dan Insulin akan diidentifikasi dan ditangani.
   - Proses: Identifikasi dan penanganan outlier dilakukan pada fitur-fitur tertentu seperti Glucose, BMI, dan Insulin.
   - Hasil: Outlier telah diidentifikasi dan diperlakukan sesuai prosedur yang ditetapkan untuk meminimalkan dampaknya pada model.

6. **Encoding fitur kategorikal**
   - Akan dipastikan semua fitur dalam format yang sesuai untuk pemodelan.
   - Proses: Memastikan semua fitur kategorikal diencode ke dalam format yang dapat diproses oleh model.
   - Hasil: Fitur kategorikal telah diencode sesuai dengan kebutuhan.

7. **Splitting data**
   - Dataset akan dibagi menjadi set pelatihan dan pengujian untuk evaluasi model.
   - Proses: Dataset dibagi menjadi set pelatihan dan pengujian untuk evaluasi model.
   - Hasil: Data telah dibagi dengan proporsi yang sesuai untuk pelatihan dan pengujian.

8. **Penanganan ketidakseimbangan kelas**
   - Ketidakseimbangan pada kolom Outcome akan diatasi menggunakan teknik seperti oversampling, undersampling, atau SMOTE.
   - Proses: Mengatasi ketidakseimbangan pada kolom Outcome menggunakan teknik oversampling.
   - Hasil: Distribusi kelas telah diubah untuk mengatasi ketidakseimbangan awal.

9. **Skalasi fitur**
   - Akan diterapkan skalasi fitur seperti Min-Max scaling atau Standard scaling.
   - Proses: Menerapkan skalasi fitur menggunakan metode Min-Max Scaling atau Standard Scaling.
   - Hasil: Fitur-fitur numerik telah discaling untuk memastikan rentang nilai yang seragam.

10. **Validasi integritas data**
   -  Akan dilakukan pemeriksaan untuk memastikan tidak ada duplikasi data dan konsistensi entri.
   - Proses: Melakukan pemeriksaan untuk memastikan tidak ada duplikasi data dan memvalidasi integritas dataset.
   - Hasil: Tidak ditemukan duplikasi data setelah pembersihan dan pra-pemrosesan.

Tahapan-tahapan ini bertujuan untuk mempersiapkan data yang bersih, konsisten, dan siap untuk pemodelan, selaras dengan tujuan bisnis yang telah diidentifikasi dalam Business Understanding.

## Modeling

### 1. Logistic Regression
Tahapan dan Parameter:

- Inisialisasi Model: Menggunakan LogisticRegression() dari scikit-learn tanpa parameter tambahan.
- Latih Model: Menggunakan metode .fit(X_train, y_train) untuk melatih model.
- Prediksi: Menggunakan metode .predict(X_test) untuk memprediksi hasil pada data uji.


Kelebihan:

- Sederhana dan mudah diinterpretasi.
- Cepat untuk dilatih dan dieksekusi.
- Bekerja dengan baik pada dataset linier.


Kekurangan:

- Tidak efektif pada dataset dengan hubungan non-linier.
Rentan terhadap outlier.

### 2. Decision Tree
Tahapan dan Parameter:

- Inisialisasi Model: Menggunakan DecisionTreeClassifier() dari scikit-learn tanpa parameter tambahan.
- Latih Model: Menggunakan metode .fit(X_train, y_train) untuk melatih model.
- Prediksi: Menggunakan metode .predict(X_test) untuk memprediksi hasil pada data uji.

Kelebihan:

- Mudah diinterpretasi dan divisualisasikan.
- Menangani fitur kategorikal dan numerik.
- Tidak memerlukan penskalaan fitur.

Kekurangan:

- Rentan terhadap overfitting.
- Sensitif terhadap perubahan kecil dalam data.

### 3. Random Forest
Tahapan dan Parameter:

- Inisialisasi Model: Menggunakan RandomForestClassifier() dari scikit-learn tanpa parameter tambahan.
- Latih Model: Menggunakan metode .fit(X_train, y_train) untuk melatih model.
- Prediksi: Menggunakan metode .predict(X_test) untuk memprediksi hasil pada data uji.

Kelebihan:

- Mengurangi overfitting dibandingkan dengan Decision Tree.
- Lebih akurat karena menggabungkan prediksi dari beberapa pohon keputusan.
- Dapat menangani dataset besar dengan fitur yang banyak.

Kekurangan:

- Lebih lambat dalam pelatihan dan prediksi dibandingkan dengan Decision Tree.
- Sulit untuk diinterpretasi dibandingkan dengan Decision Tree.

## Evaluation
   -  **Metrik Evaluasi yang Digunakan**:
      1. **Akurasi**:
         - Akurasi mengukur seberapa tepat model dalam memprediksi dengan benar (TP + TN) dari total data yang diprediksi.
         - **Formula**: 
         \( \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} \)
         - **Interpretasi**: Semakin tinggi nilai akurasi, semakin baik model dalam memprediksi.

      2. **Precision**:
         - Precision mengukur keakuratan dari positif prediksi model. Berapa proporsi dari kasus positif yang benar-benar positif.
         - **Formula**: 
         \( \text{Precision} = \frac{TP}{TP + FP} \)
         - **Interpretasi**: Semakin tinggi nilai precision, semakin sedikit hasil positif palsu yang dihasilkan model.

      3. **Recall (Sensitivitas)**:
         - Recall mengukur seberapa baik model dapat menemukan kembali semua instance yang positif.
         - **Formula**: 
         \( \text{Recall} = \frac{TP}{TP + FN} \)
         - **Interpretasi**: Semakin tinggi nilai recall, semakin sedikit kasus positif yang terlewatkan oleh model.

      4. **F1-Score**:
         - F1-Score adalah harmonic mean dari precision dan recall, memberikan keseimbangan antara keduanya.
         - **Formula**: 
         \( \text{F1-Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \)
         - **Interpretasi**: Semakin tinggi nilai F1-Score, semakin baik keseimbangan antara precision dan recall dari model.

   - Penjawaban terhadap Problem Statement:
      1. **Problem Statement**: 
      - Membangun model untuk memprediksi keberadaan diabetes berdasarkan atribut medis, dengan fokus pada akurasi prediksi yang tinggi untuk mendukung diagnosis dini dan intervensi tepat waktu.

      2. **Evaluasi Model**:
         - Model Logistic Regression memberikan akurasi sekitar 77% dengan recall dan precision sekitar 63%. Ini menunjukkan kemampuan model untuk dengan cukup baik mengidentifikasi kasus diabetes.
         - Meskipun Decision Tree dan Random Forest memberikan hasil yang sedikit lebih rendah, mereka masih memberikan indikasi yang berguna untuk diagnosis.

   - Pencapaian Goals yang Diharapkan:
      1. **Akurasi**: Model telah mencapai tingkat akurasi yang dapat dianggap cukup baik (77%). Ini berarti model dapat memberikan prediksi yang akurat dalam sebagian besar kasus.
         
      2. **Precision dan Recall**: Precision dan recall yang moderat (63%) menunjukkan bahwa model mampu mengidentifikasi sebagian besar kasus diabetes dengan benar dan mengurangi risiko diagnosis yang salah.

      3. **Impact pada Business Understanding**:
         - **Early Diagnosis**: Model dapat membantu dalam diagnosis dini diabetes, memungkinkan intervensi lebih awal untuk mengelola kondisi kesehatan pasien.
         - **Penghematan Biaya**: Dengan diagnosis yang lebih akurat, risiko komplikasi jangka panjang dapat dikurangi, yang pada gilirannya dapat mengurangi biaya perawatan kesehatan.

   - Solusi Statement yang Berdampak:
      1. **Implementasi Model**: Model yang dievaluasi dapat diimplementasikan dalam sistem informasi kesehatan untuk mendukung praktisi medis dalam pengambilan keputusan klinis sehari-hari.
         
      2. **Edukasi dan Pencegahan**: Hasil dari model ini dapat digunakan untuk pendidikan pasien tentang faktor risiko diabetes dan langkah-langkah pencegahan yang dapat diambil.

      3. **Perbaikan Proses Klinis**: Penggunaan model ini dapat memperbaiki efisiensi proses klinis dengan memberikan prediksi yang lebih cepat dan akurat.

### Logistic Regression Model

#### Proses:
- **Pelatihan Model**: Model Logistic Regression dilatih menggunakan data pelatihan yang telah dibagi sebelumnya.
- **Evaluasi Model**: Model dievaluasi menggunakan metrics seperti Precision, Recall, F1-score, dan Confusion Matrix untuk menilai performa prediksi.

#### Hasil:
- **Confusion Matrix**: Menunjukkan hasil dari prediksi model dengan matriks 2x2 yang membandingkan prediksi positif/negatif dengan nilai sebenarnya.
- **Metrics**: Precision, Recall, dan F1-score memberikan gambaran tentang ketepatan prediksi model dalam mengidentifikasi kasus diabetes.

### Decision Tree Model

#### Proses:
- **Pelatihan Model**: Model Decision Tree dilatih menggunakan data yang sama dengan Logistic Regression untuk perbandingan.
- **Evaluasi Model**: Performa model dievaluasi menggunakan metrics yang sama untuk membandingkan dengan Logistic Regression.

#### Hasil:
- **Confusion Matrix**: Menunjukkan distribusi hasil prediksi antara true positive, true negative, false positive, dan false negative.
- **Metrics**: Precision, Recall, dan F1-score digunakan untuk mengukur ketepatan dan kecocokan model dalam memprediksi diabetes.

### Random Forest Model

#### Proses:
- **Pelatihan Model**: Model Random Forest juga dilatih dan dievaluasi untuk membandingkan performa dengan dua model sebelumnya.
- **Evaluasi Model**: Metrics yang sama digunakan untuk evaluasi performa model ini.

#### Hasil:
- **Confusion Matrix**: Memberikan gambaran visual tentang seberapa baik model membedakan antara kelas positif dan negatif.
- **Metrics**: Precision, Recall, dan F1-score memberikan insight tambahan tentang performa prediksi dari model Random Forest.


### Analisis Hasil

1. **Logistic Regression**:
   - **Accuracy**: 0.777, menunjukkan bahwa sekitar 77.7% dari prediksi yang dilakukan oleh model benar.
   - **Precision**: 0.732, menunjukkan bahwa dari semua prediksi positif yang dilakukan oleh model, sekitar 73.2% benar-benar positif.
   - **Recall**: 0.600, menunjukkan bahwa dari semua kasus positif yang sebenarnya, model dapat mengidentifikasi sekitar 60% dari mereka.
   - **F1-Score**: 0.659, adalah harmonic mean dari precision dan recall, yang memberikan gambaran keseluruhan performa model dalam memprediksi.

2. **Decision Tree**:
   - **Accuracy**: 0.683, menunjukkan bahwa sekitar 68.3% dari prediksi yang dilakukan oleh model benar.
   - **Precision**: 0.554, menunjukkan bahwa dari semua prediksi positif yang dilakukan oleh model, sekitar 55.4% benar-benar positif.
   - **Recall**: 0.620, menunjukkan bahwa dari semua kasus positif yang sebenarnya, model dapat mengidentifikasi sekitar 62% dari mereka.
   - **F1-Score**: 0.585, memberikan gambaran keseluruhan performa model Decision Tree dalam memprediksi.

3. **Random Forest**:
   - **Accuracy**: 0.683, memiliki hasil yang sama dengan Decision Tree, yaitu sekitar 68.3% dari prediksi yang dilakukan oleh model benar.
   - **Precision**: 0.558, menunjukkan bahwa dari semua prediksi positif yang dilakukan oleh model, sekitar 55.8% benar-benar positif.
   - **Recall**: 0.580, menunjukkan bahwa dari semua kasus positif yang sebenarnya, model dapat mengidentifikasi sekitar 58% dari mereka.
   - **F1-Score**: 0.569, memberikan gambaran keseluruhan performa model Random Forest dalam memprediksi.

### Prediksi untuk Data Sampel
- Inputan `sample_data` terdiri dari nilai-nilai untuk fitur-fitur yang dipilih, yaitu 'Pregnancies', 'Glucose', 'BMI', dan 'Age'.
1. **Prediksi 1**:
   - Fitur: [6, 148, 33.6, 50]
   - Hasil prediksi untuk semua model: Diabetes
   - Ini menunjukkan bahwa berdasarkan fitur-fitur yang diberikan, semua model memprediksi bahwa individu tersebut memiliki diabetes.

2. **Prediksi 2**:
   - Fitur: [3, 210, 12.5, 13]
   - Hasil prediksi untuk semua model: Diabetes
   - Meskipun fitur ini agak berbeda dari yang pertama, semua model konsisten memprediksi diabetes.

3. **Prediksi 3**:
   - Fitur: [5, 180, 35.5, 45]
   - Hasil prediksi untuk semua model: Diabetes
   - Model juga memprediksi diabetes untuk data sampel ini, meskipun variasi dalam fitur.

### Kesimpulan

- **Model terbaik**: Berdasarkan metrik evaluasi yang digunakan (akurasi, precision, recall, F1-score, dan ROC-AUC Score), **Logistic Regression** merupakan pilihan terbaik untuk dataset ini karena memberikan performa paling baik secara keseluruhan.

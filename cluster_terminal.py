import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#import sklearn.cluster.hierarchical as hclust
from sklearn import preprocessing
import seaborn as sns
from app.models import *
from sklearn.metrics import davies_bouldin_score


umur = HasilDeteksi.objects.values('pengguna_id__umur')
df_umur = pd.DataFrame(umur)
df_umur.columns = ['Umur']
df=pd.DataFrame(df_umur)


jenkel = HasilDeteksi.objects.values('pengguna_id__jenis_kelamin')
df_jenkel = pd.DataFrame(jenkel)
mapping = {'Laki-laki': 1, 'Perempuan': 2}
df_jenkel['Jenis Kelamin'] = df_jenkel.replace({'pengguna_id__jenis_kelamin': mapping})
df_jenkel.drop('pengguna_id__jenis_kelamin', inplace=True, axis=1)
df['Jenis Kelamin'] = df_jenkel[['Jenis Kelamin']]


pekerjaan = HasilDeteksi.objects.values('pengguna_id__pekerjaan')
df_pekerjaan = pd.DataFrame(pekerjaan)
mapping = {'Kerja': 1, 'Pelajar/Mahasiswa': 2, 'Pelajar/Mahasiswa dan Kerja': 3, 'Tidak Kerja': 4}
df_pekerjaan['Status Pekerjaan'] = df_pekerjaan.replace({'pengguna_id__pekerjaan': mapping})
df_pekerjaan.drop('pengguna_id__pekerjaan', inplace=True, axis=1)
df['Status Pekerjaan'] = df_pekerjaan[['Status Pekerjaan']]


tingkatdepresi = HasilDeteksi.objects.values('tingkatdepresi_id')
df_tingkatdepresi = pd.DataFrame(tingkatdepresi)
df_tingkatdepresi.columns = ['Tingkat Depresi']
df['Tingkat Depresi'] = df_tingkatdepresi[['Tingkat Depresi']]


scaler = preprocessing.MinMaxScaler()
features_normal = scaler.fit_transform(df)


scoreDBI = [None] * 10
for i in range(2, 10):
    kmeans_test = KMeans(n_clusters=i, random_state=0).fit(features_normal)
    DBI = davies_bouldin_score(features_normal, kmeans_test.labels_)
    scoreDBI[i] = DBI

del scoreDBI[0:2]
get_best_cluster = scoreDBI.index(min(scoreDBI)) + 2

# # Plot the elbow
# plt.plot(range(2, 10), scoreDBI, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Inertia')
# plt.show()

kmeans = KMeans(n_clusters=get_best_cluster).fit(features_normal)

labels = pd.DataFrame(kmeans.labels_) 
labeled = pd.concat((df,labels),axis=1)
labeled = labeled.rename({0:'labels'},axis=1)

mapping = {1: 'Laki-laki (1)', 2: 'Perempuan (2)'}
labeled = labeled.replace({'Jenis Kelamin': mapping}) 

mapping = {1: 'Kerja (1)', 2: 'Pelajar/Mahasiswa (2)', 3: 'Pelajar/Mahasiswa dan Kerja (3)', 4: 'Tidak Kerja (4)'}
labeled = labeled.replace({'Status Pekerjaan': mapping})

mapping = {1: 'Tidak Depresi (1)', 2: 'Depresi Ringan (2)', 3: 'Depresi Sedang (3)', 4: 'Depresi Berat (4)'}
labeled = labeled.replace({'Tingkat Depresi': mapping})

labeled.columns = ['Umur', 'Jenis Kelamin (Kode)', 'Status Pekerjaan (Kode)', 'Tingkat Depresi (Kode)', 'Clusters/ Labels']
labeled.index = range(1, labeled.shape[0] + 1)

umur_labeled = labeled[['Umur', 'Tingkat Depresi (Kode)', 'Clusters/ Labels']]
jeniskelamin_labeled = labeled[['Jenis Kelamin (Kode)', 'Tingkat Depresi (Kode)','Clusters/ Labels']]
statuspekerjaan_labeled = labeled[['Status Pekerjaan (Kode)', 'Tingkat Depresi (Kode)','Clusters/ Labels']]

sns.lmplot(x='Umur',y='Tingkat Depresi',data=labeled,hue='labels',fit_reg=False)
plt.grid()
plt.show()

sns.lmplot(x='Jenis Kelamin',y='Tingkat Depresi',data=labeled,hue='labels',fit_reg=False)
plt.grid()
plt.show()

sns.lmplot(x='Status Pekerjaan',y='Tingkat Depresi',data=labeled,hue='labels',fit_reg=False)
plt.grid()
plt.show()


sns.pairplot(labeled,hue='labels')
plt.grid()
plt.show()


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
#import sklearn.cluster.hierarchical as hclust
from sklearn import preprocessing
import seaborn as sns
from app.models import *
from sklearn.metrics import davies_bouldin_score

umur = HasilDeteksi.objects.values('pengguna_id__umur')
df_umur = pd.DataFrame(umur)

jenkel = HasilDeteksi.objects.values('pengguna_id__jenis_kelamin')
df_jenkel = pd.DataFrame(jenkel)

pekerjaan = HasilDeteksi.objects.values('pengguna_id__pekerjaan')
df_pekerjaan = pd.DataFrame(pekerjaan)

tingkatdepresi = HasilDeteksi.objects.values('tingkatdepresi_id__nama_depresi')
df_tingkatdepresi = pd.DataFrame(tingkatdepresi)

df_umur.columns = ['Umur']
df=pd.DataFrame(df_umur)

mapping = {'Laki-laki': 1, 'Perempuan': 2}
df_jenkel['Jenis Kelamin'] = df_jenkel.replace({'pengguna_id__jenis_kelamin': mapping})
df_jenkel.drop('pengguna_id__jenis_kelamin', inplace=True, axis=1)
df['Jenis Kelamin'] = df_jenkel[['Jenis Kelamin']]

mapping = {'Kerja': 1, 'Pelajar/Mahasiswa': 2, 'Pelajar/Mahasiswa dan Kerja': 3, 'Tidak Kerja': 4}
df_pekerjaan['Status Pekerjaan'] = df_pekerjaan.replace({'pengguna_id__pekerjaan': mapping})
df_pekerjaan.drop('pengguna_id__pekerjaan', inplace=True, axis=1)
df['Status Pekerjaan'] = df_pekerjaan[['Status Pekerjaan']]

mapping = {'Tidak Depresi': 1, 'Depresi Ringan': 2, 'Depresi Sedang': 3, 'Depresi Berat': 4}
df_tingkatdepresi['Tingkat Depresi'] = df_tingkatdepresi.replace({'tingkatdepresi_id__nama_depresi': mapping})
df_tingkatdepresi.drop('tingkatdepresi_id__nama_depresi', inplace=True, axis=1)
df['Tingkat Depresi'] = df_tingkatdepresi[['Tingkat Depresi']]



df.to_csv(r'C:\Users\LENOVO\Documents\KULIAH\SEMESTER 8\Skripsi\load.csv')


data = HasilDeteksi.objects.values('pengguna_id__umur', 'pengguna_id__jenis_kelamin', 'pengguna_id__pekerjaan', 'tingkatdepresi_id__nama_depresi')
df = pd.DataFrame(data)
df.columns = ['Umur', 'Jenis Kelamin', 'Status Pekerjaan', 'Tingkat Depresi']

mapping = {'Laki-laki': 1, 'Perempuan': 2}
df['Jenis Kelamin2'] = df.replace({'Jenis Kelamin': mapping})
df.drop('Jenis Kelamin', inplace=True, axis=1)
mapping = {'Kerja': 1, 'Pelajar/Mahasiswa': 2, 'Pelajar/Mahasiswa dan Kerja': 3, 'Tidak Kerja': 4}
df['Status Pekerjaan Inisial'] = df.replace({'Status Pekerjaan': mapping})
df.drop('Status Pekerjaan', inplace=True, axis=1)
mapping = {'Tidak Depresi': 1, 'Depresi Ringan': 2, 'Depresi Sedang': 3, 'Depresi Berat': 4}
df['Tingkat Depresi Inisial'] = df.replace({'Tingkat Depresi': mapping})
df.drop('Tingkat Depresi', inplace=True, axis=1)


umur = HasilDeteksi.objects.values('pengguna_id__umur')
df_umur = pd.DataFrame(umur)
df_umur.columns = ['Umur']
df=pd.DataFrame(df_umur)

jenkel = HasilDeteksi.objects.values('pengguna_id__jenis_kelamin')
df_jenkel = pd.DataFrame(jenkel)
df['Jenis Kelamin'] = df_jenkel[['pengguna_id__jenis_kelamin']]

pekerjaan = HasilDeteksi.objects.values('pengguna_id__pekerjaan')
df_pekerjaan = pd.DataFrame(pekerjaan)
df['Status Pekerjaan'] = df_pekerjaan[['pengguna_id__pekerjaan']]

tingkatdepresi = HasilDeteksi.objects.values('tingkatdepresi_id__nama_depresi')
df_tingkatdepresi = pd.DataFrame(tingkatdepresi)
df['Tingkat Depresi'] = df_tingkatdepresi[['tingkatdepresi_id__nama_depresi']]





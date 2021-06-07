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

kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(features_normal)

labels = pd.DataFrame(kmeans.labels_) #This is where the label output of the KMeans we just ran lives. Make it a dataframe so we can concatenate back to the original data
labeled = pd.concat((df,labels),axis=1)
labeled = labeled.rename({0:'labels'},axis=1)

mapping = {1: 'Laki-laki (1)', 2: 'Perempuan (2)'}
labeled = labeled.replace({'Jenis Kelamin': mapping}) 

mapping = {1: 'Kerja (1)', 2: 'Pelajar/Mahasiswa (2)', 3: 'Pelajar/Mahasiswa dan Kerja (3)', 4: 'Tidak Kerja (4)'}
labeled = labeled.replace({'Status Pekerjaan': mapping})

mapping = {1: '(1) Tidak Depresi', 2: '(2) Depresi Ringan', 3: '(3) Depresi Sedang', 4: '(4) Depresi Berat'}
labeled = labeled.replace({'Tingkat Depresi': mapping})

labeled.columns = ['Umur', 'Jenis Kelamin (Inisial)', 'Status Pekerjaan (Inisial)', 'Tingkat Depresi (Inisial)', 'Clusters/ Labels']
labeled.index = range(1, labeled.shape[0] + 1) 

umur_labeled = labeled[['Umur', 'Tingkat Depresi (Inisial)', 'Clusters/ Labels']]
jeniskelamin_labeled = labeled[['Jenis Kelamin (Inisial)', 'Tingkat Depresi (Inisial)','Clusters/ Labels']]
statuspekerjaan_labeled = labeled[['Status Pekerjaan (Inisial)', 'Tingkat Depresi (Inisial)','Clusters/ Labels']]

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

labeled.to_csv (r'C:\Users\LENOVO\Documents\KULIAH\SEMESTER 8\Skripsi\excel\label.csv', index = True, header=True)



centroid = pd.DataFrame(kmeans.cluster_centers_)

count = labeled.pivot_table(index=['Clusters/ Labels', 'Tingkat Depresi (Inisial)', 'Umur', 'Jenis Kelamin (Inisial)', 'Status Pekerjaan (Inisial)'], aggfunc='size').reset_index(name='counts')

labeled.groupby(['Clusters/ Labels', 'Tingkat Depresi (Inisial)', 'Umur', 'Jenis Kelamin (Inisial)', 'Status Pekerjaan (Inisial)']).size().reset_index(name='counts')

count = labeled.groupby(['Umur', 'Jenis Kelamin (Inisial)', 'Status Pekerjaan (Inisial)', 'Tingkat Depresi (Inisial)', 'Clusters/ Labels']).size().reset_index(name='Jumlah Data')
group3 = pd.DataFrame(count)
group3= group3.sort_values(['Umur'],ascending=[True])  
group3= group3.sort_values(['Jenis Kelamin (Inisial)'],ascending=[True]) 
group3= group3.sort_values(['Status Pekerjaan (Inisial)'],ascending=[True]) 
# group3= group3.sort_values(['Jumlah Data'],ascending=[False])  
group3= group3.sort_values(['Tingkat Depresi (Inisial)'],ascending=[True])  


nama = HasilDeteksi.objects.values('pengguna_id__nama')
df_nama = pd.DataFrame(nama)
df_nama.columns = ['Nama']
labeled.insert(0, 'Nama', df_nama)


df['Nama'] = df_nama[['Nama']]
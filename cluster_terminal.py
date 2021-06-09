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


scoreDBI = [None] * 7
for i in range(2, 7):
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

mapping = {1: '(1) Laki-laki', 2: '(2) Perempuan'}
labeled = labeled.replace({'Jenis Kelamin': mapping}) 

mapping = {1: '(1) Kerja', 2: '(2) Pelajar/Mahasiswa', 3: '(3) Pelajar/Mahasiswa dan Kerja', 4: '(4) Tidak Kerja'}
labeled = labeled.replace({'Status Pekerjaan': mapping})

mapping = {1: '(1) Tidak Depresi', 2: '(2) Depresi Ringan', 3: '(3) Depresi Sedang', 4: '(4) Depresi Berat'}
labeled = labeled.replace({'Tingkat Depresi': mapping})

labeled.columns = ['Umur', '(Inisial) Jenis Kelamin', '(Inisial) Status Pekerjaan', '(Inisial) Tingkat Depresi', 'Clusters/ Labels']

nama = HasilDeteksi.objects.values('pengguna_id__nama')
df_nama = pd.DataFrame(nama)
df_nama.columns = ['Nama']
labeled.insert(0, 'Nama', df_nama)
# idd = HasilDeteksi.objects.values('pengguna_id')
# df_id = pd.DataFrame(idd)
# df_id.columns = ['id']
# labeled.insert(0, 'id', df_id)

labeled.index = range(1, labeled.shape[0] + 1) 

umur_labeled = labeled[['Umur', '(Inisial) Tingkat Depresi', 'Clusters/ Labels']]
jeniskelamin_labeled = labeled[['(Inisial) Jenis Kelamin', '(Inisial) Tingkat Depresi','Clusters/ Labels']]
statuspekerjaan_labeled = labeled[['(Inisial) Status Pekerjaan', '(Inisial) Tingkat Depresi','Clusters/ Labels']]

count = labeled.groupby(['Clusters/ Labels']).size().reset_index(name='Jumlah Data')
group3 = pd.DataFrame(count)
group3.index = range(1, group3.shape[0] + 1) 
# group3= group3.sort_values(['Umur'],ascending=[True])  
# group3= group3.sort_values(['Jenis Kelamin (Inisial)'],ascending=[True]) 
# group3= group3.sort_values(['Status Pekerjaan (Inisial)'],ascending=[True]) 
# group3= group3.sort_values(['Jumlah Data'],ascending=[False])  
group3= group3.sort_values(['(Inisial) Tingkat Depresi'],ascending=[False])  
group3.reset_index(drop=True, inplace=True)

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
group3= group3.sort_values(['Tingkat Depresi (Inisial)'],ascending=[False])  


nama = HasilDeteksi.objects.values('pengguna_id__nama')
df_nama = pd.DataFrame(nama)
df_nama.columns = ['Nama']
labeled.insert(0, 'Nama', df_nama)


df['Nama'] = df_nama[['Nama']]


from sklearn.metrics import silhouette_score
scoreDBI = [None] * 8
for i in range(2, 8):
    kmeans_test = KMeans(n_clusters=i, random_state=0).fit(features_normal)
    DBI = silhouette_score(features_normal, kmeans.labels_, metric='euclidean')
    scoreDBI[i] = DBI

del scoreDBI[0:2]
get_best_cluster = scoreDBI.index(min(scoreDBI)) + 2

score = silhouette_score(features_normal, kmeans.labels_, metric='euclidean')
#
# Print the score
#
print('Silhouetter Score: %.3f' % DBI)


plt.pie(labeled['bar_depresi'],labels=query_df_bar['tingkatdepresi_id__nama_depresi'],autopct='%1.2f%%')
plt.tight_layout()
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()
graphic_tingkatdepresi_pie = base64.b64encode(image_png)
graphic_tingkatdepresi_pie = graphic_tingkatdepresi_pie.decode('utf-8')
pylab.close()


 
from sklearn.decomposition import PCA
pca = PCA(4)
df2 = pca.fit_transform(df)




from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
 
#Load Data
data = load_digits().data
pca = PCA(2)
 
#Transform the data
df = pca.fit_transform(data)
 
#Import KMeans module
from sklearn.cluster import KMeans
 
#Initialize the class object
kmeans = KMeans(n_clusters= 10)
kmeans = KMeans(n_clusters=get_best_cluster, random_state=0)
 
#predict the labels of clusters.
label = kmeans.fit_predict(df)
labels = pd.DataFrame(kmeans.labels_)
label = kmeans.fit(features_normal)

 
#Getting unique labels
u_labels = np.unique(label)
 
#plotting the results:
for i in u_labels:
    plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i)
plt.legend()
plt.show()

#plotting the results:
for i in u_labels:
    plt.scatter(features_normal[label == i , 0] , features_normal[label == i , 1] , label = i)
plt.legend()
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
from sklearn.decomposition import PCA



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


pca = PCA(4)
 
#Transform the data

scaler = preprocessing.MinMaxScaler()
features_normal = scaler.fit_transform(df)
features_normal2 = pca.fit_transform(features_normal)



scoreDBI = [None] * 7
for i in range(2, 7):
    kmeans_test = KMeans(n_clusters=i, random_state=0).fit(features_normal2)
    DBI = davies_bouldin_score(features_normal2, kmeans_test.labels_)
    scoreDBI[i] = DBI

del scoreDBI[0:2]
get_best_cluster = scoreDBI.index(min(scoreDBI)) + 2

kmeans = KMeans(n_clusters=get_best_cluster, random_state=0).fit(features_normal2)

# label = kmeans.fit(features_normal2)
label = kmeans.fit_predict(features_normal2)


#Getting the Centroids
centroids = kmeans.cluster_centers_
u_labels = np.unique(label)
 
#plotting the results:
 
for i in u_labels:
    plt.scatter(features_normal2[label == i , 0] , features_normal2[label == i , 1] , label = i)

plt.scatter(centroids[:,0] , centroids[:,1] , s = 180, color = 'k)
plt.legend()
plt.show()
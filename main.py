import pandas as pd
import numpy as np
import statistics as st
from scipy.stats import norm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_excel('tellme_ST.xls')
miss = df.drop(
    columns=['adddate', 'Biography', 'u_name', 'u_family', 'insta_ExternalUrl'])
miss['Media_Count'] = miss['Media_Count'].fillna(np.nan)
miss['Following'] = miss['Following'].fillna(np.nan)
miss['Follower'] = miss['Follower'].fillna(np.nan)
miss = miss.dropna(subset=['Media_Count', 'Following', 'Follower'], how='all')
# print(miss,"\n","count=",len(miss.index))
# miss.to_excel(r'D:\ALI\Uni\Term6\data maining\projeh\1.xlsx', index = True)

outlier = miss.dropna(subset=['cat_id'], how='all')
# print("\n","count=",len(outlier.index))
outlier = outlier.reset_index()
# outlier.to_excel(r'D:\ALI\Uni\Term6\data maining\projeh\2.xlsx', index = False)

noisy = outlier
no = noisy
no1 = no.loc[:, ['Media_Count', 'Following']]
no1.fillna(0, inplace=True)
no['Media_Count'] = no1['Media_Count']
no['Following'] = no1['Following']
# print("count=",len(no.index))
# no.to_excel(r'D:\ALI\Uni\Term6\data maining\projeh\4.xlsx', index = False)

# drop_0
no = no[(no[['Media_Count', 'Following']] != 0).all(axis=1)]
# no.to_excel(r'D:\ALI\Uni\Term6\data maining\projeh\10.xlsx', index = False)
no = no.reset_index()
# print("count=",len(no.index))

f = no.loc[(no['Follower'] >= 500) & (no['Follower'] <= 100000000)]
f.sort_values(by='Follower', inplace=True)
# fng=f
# fng.sort_values(by='Following', inplace=True)
# media=f
# media.sort_values(by='Media_Count', inplace=True)
# print(f,"count=",len(f.index))
# f.to_excel(r'D:\ALI\Uni\Term6\data maining\projeh\Final.xlsx', index = False)

# t1=no.loc[(no['Follower'] >= 1000) & (no['Follower'] <= 1000000)]
# t1=t1.loc[:,['Follower']]
# # print(n1,"count=",len(n1.index))
# # plt.boxplot(n1,patch_artist=True)
# # plt.show()
# n,bins,_= plt.hist(t1, bins='auto' ,edgecolor='black')
# plt.xlabel('Follower')
# plt.ylabel('Number')
# plt.show()

zarib1 = f['Follower'].corr(f['Following'], method='pearson')
print(zarib1)
zarib2 = f['Follower'].corr(f['Media_Count'], method='pearson')
print(zarib2)
x_axis = f['Follower']
# x_axis =media['Media_Count']
# x_axis =fng['Following']

# Calculating mean and standard deviation
mean = st.mean(x_axis)
sd = st.stdev(x_axis)
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()

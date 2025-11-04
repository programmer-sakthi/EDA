import os 
import sys 
import pandas as pd


def get_file_path(file_name):
    return os.path.join(sys.path[0],file_name)



filename=get_file_path(input("Enter the CSV filename:"))
dp=pd.read_csv(filename)
print("\n--- Payments DataFrame Loaded ---")
print(dp.head())
print()
print("--- Service Ratings Series ---")
service=dp["service_rating"]
print(service.head())

print()
print("First 5 Ratings (using .iloc):")
print(dp["service_rating"].iloc[:5])
print()



providers = ['PRV002','PRV005','PRV010']
print("Ratings for providers ['PRV002', 'PRV005', 'PRV010'] (using .loc equivalent):")
filtered_ratings_mask=dp['provider_id'].isin(providers)
filtered_ratings=dp.loc[filtered_ratings_mask,['provider_id','service_rating']]
filtered_ratings=filtered_ratings.set_index('provider_id')['service_rating']
print(filtered_ratings)
print()


below_3_mask=filtered_ratings<3
print("Number of ratings below 3:",below_3_mask.sum())


print()
avg_ratings=dp[filtered_ratings_mask].groupby('provider_id')['service_rating'].mean()
print("Average Ratings by Provider:")
print(avg_ratings)
print()

print("Updated Ratings Set:")
print(filtered_ratings)
print()

print("--- Ratings DataFrame ---")
filtered_ratings=dp.loc[filtered_ratings_mask,['provider_id','service_rating']]
filtered_ratings=filtered_ratings.set_index('provider_id')['service_rating']
filtered_ratings=filtered_ratings.rename('provider_rating').reset_index()
# filtered_ratings = filtered_ratings.rename(columns={'service_rating':'provider_rating'}).reset_index()
print(filtered_ratings)







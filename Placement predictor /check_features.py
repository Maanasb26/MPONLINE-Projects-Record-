import pickle

with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)

print(feature_names)
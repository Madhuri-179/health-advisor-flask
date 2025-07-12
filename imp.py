import pickle

# Load the data from the .pkl file
with open('svc.pkl', 'rb') as file:
    data = pickle.load(file)
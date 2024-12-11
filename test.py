import pickle
import gzip

# Compress movie_list.pkl
with open('model/movie_list.pkl', 'rb') as f_in:
    with gzip.open('model/movie_list.pkl.gz', 'wb') as f_out:
        pickle.dump(pickle.load(f_in), f_out)

# Compress similarity.pkl
with open('model/similarity.pkl', 'rb') as f_in:
    with gzip.open('model/similarity.pkl.gz', 'wb') as f_out:
        pickle.dump(pickle.load(f_in), f_out)

print("Files compressed successfully!")

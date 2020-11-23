from numpy import *
import scipy.optimize
import pandas as pd

# Generate ratings randomly with 1000 songs and 40 users. Each uesr rates 10 songs.
SongID_list = [e for e in range(1000)]
Songs_list = random.randint(1, 1000, 400)
UserID_list = [e for e in range(40) for i in range(10)]
ratings_list = random.choice([1,2,3], size=400)
Songs_df = pd.DataFrame(SongID_list, columns=['SongID'])
ratings_df = pd.DataFrame({'UserID':UserID_list, 'SongID':Songs_list, 'Rating':ratings_list})

user_Group = ratings_df.groupby('UserID')
ratings = []

# For each user in the group
for userID, curUser in user_Group:

    # Create a temp that stores every song's rating
    temp = [0]*len(Songs_df)

    # For each song in curUser's song list
    for num, song in curUser.iterrows():

        # Divide the rating by 5 and store it
        temp[song['SongID']] = (song['Rating']+1)/2

    # Add the list of ratings into the training list
    ratings.append(temp)

ratings = array(ratings).T
did_rate = (ratings != 0) * 1

#My song ratings
my_ratings = zeros((1000,1))
random_songs = random.randint(low=0, high=1000, size=10)
for i in random_songs:
  my_ratings[i] = random.choice([1,2,3])


# Add my song ratings to the matrices
ratings = append(my_ratings, ratings, axis = 1)
did_rate = append(((my_ratings!=0) * 1), did_rate, axis = 1)


# Normalise ratings
ratings[ratings!=0] = (ratings[ratings!=0]-1)/2


# Cost function
def calculate_cost(X_and_theta, ratings, did_rate, num_users, num_songs, num_features, reg_param):
  # Retrieve the X and theta matrixes from X_and_theta, based on their dimensions (num_features, num_songs, num_songs)
  # --------------------------------------------------------------------------------------------------------------
  # Get the first 30 (10 * 3) rows in the 48 X 1 column vector
  first_30 = X_and_theta[:num_songs * num_features]
  # Reshape this column vector into a 10 X 3 matrix
  X = first_30.reshape((num_features, num_songs)).transpose()
  # Get the rest of the 18 the numbers, after the first 30
  last_18 = X_and_theta[num_songs * num_features:]
  # Reshape this column vector into a 6 X 3 matrix
  theta = last_18.reshape(num_features, num_users ).transpose()
  
  # we multiply by did_rate because we only want to consider observations for which a rating was given
  # we calculate the sum of squared errors here.  
  # in other words, we calculate the squared difference between our hypothesis (predictions) and ratings
  cost = sum( (X.dot( theta.T ) * did_rate - ratings) ** 2 ) / 2
  
  # we get the sum of the square of every element of X and theta
  regularization = (reg_param / 2) * (sum( theta**2 ) + sum(X**2))
  return cost + regularization


# Calculate gradients, i.e. derivatives
def calculate_gradient(X_and_theta, ratings, did_rate, num_users, num_songs, num_features, reg_param):
  # Retrieve the X and theta matrixes from X_and_theta, based on their dimensions (num_features, num_songs, num_songs)
  # --------------------------------------------------------------------------------------------------------------
  # Get the first 30 (10 * 3) rows in the 48 X 1 column vector
  first_30 = X_and_theta[:num_songs * num_features]
  # Reshape this column vector into a 10 X 3 matrix
  X = first_30.reshape((num_features, num_songs)).transpose()
  # Get the rest of the 18 the numbers, after the first 30
  last_18 = X_and_theta[num_songs * num_features:]
  # Reshape this column vector into a 6 X 3 matrix
  theta = last_18.reshape(num_features, num_users ).transpose()
  
  # we multiply by did_rate because we only want to consider observations for which a rating was given
  difference = X.dot( theta.T ) * did_rate - ratings
  
  # we calculate the gradients (derivatives) of the cost with respect to X and theta
  X_grad = difference.dot( theta ) + reg_param * X
  theta_grad = difference.T.dot( X ) + reg_param * theta
  
  # wrap the gradients back into a column vector 
  return r_[X_grad.T.flatten(), theta_grad.T.flatten()]
  
  # Generate sample data
num_songs, num_users = shape(ratings)
num_features = 3

# Initialize Parameters theta (user_prefs), X (song_features)

song_features = random.randn( num_songs, num_features )
user_prefs = random.randn( num_users, num_features )

# r_ is from numpy.r_ and creates an instance of a class which defines an array with the values in the squared brackets []
initial_X_and_theta = r_[song_features.T.flatten(), user_prefs.T.flatten()]

# Regularization paramater
reg_param = 100

# Calculate the minimum cost and params used to achieve it

# fprime simply refers to the derivative (gradient) of the calculate_cost function
# We iterate 100 times
minimized_cost_and_optimal_params = scipy.optimize.fmin_cg(calculate_cost, fprime=calculate_gradient, x0=initial_X_and_theta, \
                args=(ratings, did_rate, num_users, num_songs, num_features, reg_param), \
                maxiter=100, disp=True, full_output=True )


# Retrieve the minimized cost and the optimal values of the song_features (X) and user_prefs (theta) matrices
cost, optimal_song_features_and_user_prefs = minimized_cost_and_optimal_params[1], minimized_cost_and_optimal_params[0]


first_30 = optimal_song_features_and_user_prefs[:num_songs * num_features]
songs_features = first_30.reshape((num_features, num_songs)).transpose()
last_18 = optimal_song_features_and_user_prefs[num_songs * num_features:]
user_prefs = last_18.reshape(num_features, num_users ).transpose()

# Predictions for each user
all_predictions = songs_features.dot(user_prefs.T )

# My predictions
predictions_for_me = all_predictions[:, 0:1]


sorted_indexes = predictions_for_me.argsort(axis=0)[::-1]
predictions_for_me = predictions_for_me[sorted_indexes]
print('Top 20: Recommend songs ID:\n', sorted_indexes[:20] )

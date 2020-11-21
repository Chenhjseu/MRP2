import face_recognition
import update
import prediction
import feedback
import play_the_song

class recommendation_system(self):

if user is new:
  initialize()

while True:
  emotion_state = face_recognition(self)
  if emotion_state == 1:
    ratings = pd.read_csv(ratings_positive.csv)
  elif emotion_state == 2:
    ratings = pd.read_csv(ratings_negative.csv)
  else:
    ratings = pd.read_csv(ratings_nature.csv)

  recommend_playlist = prediction(ratings)

  play_the_song(recommend_playlist)

  new_rating = feedback

  update(new_rating) 

  emotion_state = face_recognition(self)

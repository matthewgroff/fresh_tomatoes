import media
import webbrowser
import fresh_tomatoes

#create instances of Movie

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
interstellar = media.Movie("Interstellar",
                        "A team of explorers travel through a wormhole"
                        "in space in an attempt to ensure humanity's survival.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA")
stepBrothers= media.Movie("Step Brothers",
                        "Two aimless middle-aged losers still"
                        "living at home are forced against their"
                        "will to become roommates when their parents marry.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcwNzUzMjU1OV5BMl5BanBnXkFtZTcwMTM0NDQ2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=ANjenc4W1_Q")
warOfArrows = media.Movie("War of the Arrows",
                        "Set during the second Manchu invasion of Korea,"
                        "Nam Yi, the best archer in Korea, goes up"
                        "against the Qing Dynasty to save his younger"
                        "sister Ja In - who was dragged away by Manchurian.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgwMjAyNzA0N15BMl5BanBnXkFtZTcwMTcxOTIwNw@@._V1_UY268_CR3,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=XDyIjb272kU")
darkKnight = media.Movie("The Dark Knight",
                        "When the menace known as the Joker wreaks"
                        "havoc and chaos on the people of Gotham,"
                        "the caped crusader must come to terms"
                        "with one of the greatest psychological"
                        "tests of his ability to fight injustice.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=kmJLuwP3MbY")
pulpFiction = media.Movie("Pulp Fiction",
                        "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=wZBfmBvvotE")

# list of movie objects to open with Fresh Tomatoes

movies = [toy_story, interstellar, stepBrothers,warOfArrows,darkKnight,pulpFiction]

# run fresh_tomatoes using the movies list. creates html page
fresh_tomatoes.open_movies_page(movies)

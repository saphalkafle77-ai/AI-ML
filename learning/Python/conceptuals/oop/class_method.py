# class method (only access class attribute)
class Anime:
    anime_type = "shounen"

    @classmethod
    def get_anime_type(cls):
        print(f"anime type is {cls.anime_type}")


Anime.get_anime_type()

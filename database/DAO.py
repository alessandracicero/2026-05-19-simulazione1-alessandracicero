from database import DB_connect
from database.DB_connect import DBConnect
from model.artisti import Artist
from model.genere import Genere


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getGeneri():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query = """select distinct Name
                from genre g """

        cursor.execute(query)

        for row in cursor:
            res.append(Genere(**row))

        cursor.close()
        cnx.close()

        return res
    @staticmethod
    def getAllArtist():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query = """select *
                        from Artist"""

        cursor.execute(query)

        for row in cursor:
            res.append(Artist(row["ArtistId"],row["Name"],0))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getArtistGenre(genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query = """"select a.ArtistId , count(i.TrackId) as popolarita 
                    from track t , album a , invoiceline i 
                     where t.GenreId =%s and t.AlbumId = a.AlbumId and t.TrackId = i.TrackId  
                    group by a.ArtistId t"""

        cursor.execute(query,(genere,))

        for row in cursor:
            res.append((row["a.ArtistId "],row["popolarita"]))

        cursor.close()
        cnx.close()

        return res

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

        query = """select *
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

        query = """select a.ArtistId 
                    from track t , album a
                    where t.GenreId = %s and t.AlbumId = a.AlbumId  
                    group by a.ArtistId """

        cursor.execute(query,(genere,))

        for row in cursor:
            res.append((row["ArtistId"]))

        cursor.close()
        cnx.close()

        return res
    @staticmethod
    def getPopolarita(genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res = []

        query = """ select a.ArtistId, count(i2.CustomerId) as popolarita 
                    from track t , invoiceline i , invoice i2 , album a 
                    where t.TrackId = i.TrackId  and i2.InvoiceId =i.InvoiceId and a.AlbumId =t.AlbumId and t.GenreId = %s
                    group by a.ArtistId """

        cursor.execute(query,(genere,))

        for row in cursor:
            res.append((row["ArtistId"],row["popolarita"]))

        cursor.close()
        cnx.close()

        return res
    @staticmethod
    def getArchi(genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res = []

        query = """ select a.ArtistId, i2.CustomerId 
                    from track t , invoiceline i , invoice i2 , album a 
                    where t.TrackId = i.TrackId  and i2.InvoiceId =i.InvoiceId and a.AlbumId =t.AlbumId and t.GenreId = %s
                    group by a.ArtistId, i2.CustomerId 
                    order by i2.CustomerId """

        cursor.execute(query,(genere,))
        for row in cursor:
            res.append((row["ArtistId"],row["CustomerId"]))


        cursor.close()
        cnx.close()

        return res




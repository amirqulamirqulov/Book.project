from abc import ABC, abstractmethod
from settings import db_path
import sqlite3

class Base_Model (ABC):
   def __init__(self, id = None) -> None:
       self.id = id
       self.isValid = True

   @property
   def isValid(self):
      return self.__isValid 

   @isValid.setter
   def isValid(self, isValid):
      self.__isValid = isValid

   @abstractmethod
   def print():
      pass

   @abstractmethod
   def save(self):
      pass

   @abstractmethod
   def delete(self):
      pass

   @classmethod
   @abstractmethod
   def objects():
      pass

   @classmethod
   @abstractmethod
   def get_by_id(id):
      pass


class Book_type(Base_Model):
   def __init__(self, Name, id=None) -> None:
       super().__init__(id)
       self.Name = Name

   @property
   def Name(self):
      return self.__Name

   @Name.setter
   def Name(self, Name):
      if isinstance(Name, str):
         self.__Name = Name
      else:
         self.__Name = ""
         self.isValid = False

   def print():
      with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(''' SELECT Name FROM Book_type''')
        for row in cursor:
           print("Name = ", row[0])

   def save(self):
      if self.isValid:
         try:
            with sqlite3.connect(db_path) as conn:
               cursor = conn.cursor()
               try:
                  if self.id == None:
                     cursor.execute(f'''INSERT INTO Book_type ("Name")
                     VALUES ('{self.Name}')''')
                     self.id = cursor.lastrowid
                  else:
                     conn.execute(f'''UPDATE Book_type set Name ="{self.Name}" WHERE id = "{self.id}"''')
                     conn.commit()
               except:
                  print("saqlashda xatolik")
                  conn.rollback()
            return True
         except:
            print("Bog\'lanishda xatolik")
      else:
         return False

   def delete(self):
       try:
          with sqlite3.connect(db_path) as conn:
             cursor = conn.cursor()
             cursor.execute(f''' DELETE FROM Book_type WHERE id = {self.id}''')
             conn.commit()
       except:
          print("Bog\'lanishda xatolik")

   def objects():
       try:
          with sqlite3.connect(db_path) as conn:
              cursor = conn.cursor()
              query = f''' SELECT  *FROM Book_type '''
              for row in cursor.execute(query):
                 yield Book_type(row[1], row[0])   
       except:
          print("Bog\'lanishda xatolik")

   def get_by_id(id):
      try:
         with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''SELECT *FROM Book_type WHERE id = {id}'''
            res = cursor.execute(query).fetchone()
            if res is not None:
               return Book_type(res[1], res[0])
            else:
               return None
      except:
         print("bog\'lanishda xatolik")

   def __str__(self) -> str:
       return f"{self.__Name}"

class Book_name(Base_Model):
   def __init__(self,Name, Bookid, id=None) -> None:
       super().__init__(id)
       self.Name = Name
       self.Bookid = Bookid

   @property
   def Name(self):
      return self.__Name

   @Name.setter
   def Name(self, Name):
      if isinstance(Name, str):
         self.__Name = Name
      else:
         self.__Name = ""
         self.isValid = False

   @property
   def Bookid(self):
      return self.__Bookid

   @Bookid.setter
   def Bookid(self, Bookid):
      if isinstance(Bookid, int):
         self.__Bookid = Bookid
      else:
         self.__Bookid = None
         self.isValid = False

   @property
   def Book_type(self):
      return Book_type.get_by_id(self.Bookid)

   def print():
      with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(''' SELECT Name, Bookid FROM Book_name''')
        for row in cursor:
           print("Name = ", row[0])
           print("Bookid = ", row[1])

   def save(self):
      if self.isValid:
         try:
            with sqlite3.connect(db_path) as conn:
               cursor = conn.cursor()
               try:
                  if self.id == None:
                     cursor.execute(f'''INSERT INTO Book_name ("Name", Bookid) 
                     VALUES ("{self.Name}", {self.Bookid})''')
                     self.id = cursor.lastrowid
                  else:
                     conn.execute(f'''UPDATE Book_name set Name ="{self.Name}",\
                         Bookid = {self.Bookid} WHERE id = "{self.id}"''')
                     conn.commit()
               except:
                  print("saqlashda xatolik")
                  conn.rollback()
            return True
         except:
            print("Bog\'lanishda xatolik")
      else:
         return False
         
   def delete(self):
       try:
          with sqlite3.connect(db_path) as conn:
             cursor = conn.cursor()
             cursor.execute(f''' DELETE FROM Book_name WHERE id = {self.id}''')
             conn.commit()
       except:
          print("Bog\'lanishda xatolik")

   def objects():
       try:
          with sqlite3.connect(db_path) as conn:
              cursor = conn.cursor()
              query = (f''' SELECT  *FROM Book_name ''')
              for row in cursor.execute(query):
                 yield Book_name(row[1], row[2], row[0])   
       except:
          print("Bog\'lanishda xatolik")

   def get_by_id(id):
      try:
         with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''SELECT *FROM Book_name WHERE id = {id}'''
            res = cursor.execute(query).fetchone()
            if res is not None:
               return Book_name(res[1], res[2], res[0])
            else:
               return None
      except:
         print("bog\'lanishda xatolik")

   def __str__(self) -> str:
       return f"{self.Book_type} \t | {self.Name}"


class Book(Base_Model):
   def __init__(self, Year, Count_page, Price, Author, Bookid, id=None) -> None:
       super().__init__(id)
       self.Year = Year
       self.Count_page = Count_page
       self.Price = Price
       self.Author = Author
       self.Bookid = Bookid

   @property
   def Year(self):
      return self.__Year

   @Year.setter
   def Year(self, Year):
      if isinstance(Year, int):
         self.__Year = Year
      else:
         self.__Year = None
         self.isValid = False   

   @property
   def Count_page(self):
      return self.__Count_page

   @Count_page.setter
   def Count_page(self, Count_page):
      if isinstance(Count_page, int):
         self.__Count_page = Count_page
      else:
         self.__Count_page = None
         self.isValid = False  
   
   @property
   def Price(self):
      return self.__Price

   @Price.setter
   def Price(self, Price):
      if isinstance(Price, int):
         self.__Price = Price
      else:
         self.__Price = None
         self.isValid = False  
   
   @property
   def Author(self):
      return self.__Author

   @Author.setter
   def Author(self, Author):
      if isinstance(Author, str):
         self.__Author = Author
      else:
         self.__Author = ""
         self.isValid = False 

   @property
   def Bookid(self):
      return self.__Bookid

   @Bookid.setter
   def Bookid(self, Bookid):
      if isinstance(Bookid, int) and Book_name.get_by_id(Bookid) is not None:
         self.__Bookid = Bookid
      else:
         self.__Bookid = None
         self.isValid = False

   @property
   def Book_name(self):
      return Book_name.get_by_id(self.Bookid)

   def print():
      with sqlite3.connect(db_path) as conn:
         cursor = conn.execute(''' SELECT Year, Count_page, Price, Author,  Bookid FROM Book''')
         for row in cursor:
            print("Year = ", row[0])
            print("Count_page = ", row[1])
            print("Price = ", row[2])
            print("Author = ", row[3])
            print("Bookid = ", row[4])
            
   def save(self):
      if self.isValid:
         try:
            with sqlite3.connect(db_path) as conn:
               cursor = conn.cursor()
               try:
                  if self.id == None:
                     cursor.execute(f'''INSERT INTO Book (Year, Count_page, Price,"Author", Bookid) 
                     VALUES ({self.Year}, {self.Count_page}, {self.Price}, "{self.Author}", {self.Bookid})''')
                     self.id = cursor.lastrowid
                  else:
                     conn.execute(f'''UPDATE Book set Year ="{self.Year}", Count_page = {self.Count_page}, Price = {self.Price},
                         Author = "{self.Author}", Bookid = {self.Bookid} WHERE id = "{self.id}"''')
                     conn.commit()
               except:
                  print("saqlashda xatolik")
                  conn.rollback()
            return True
         except:
            print("Bog\'lanishda xatolik")
      else:
         return False

   def delete(self):
       try:
          with sqlite3.connect(db_path) as conn:
             cursor = conn.cursor()
             cursor.execute(f''' DELETE FROM Book WHERE id = {self.id}''')
             conn.commit()
       except:
          print("Bog\'lanishda xatolik")

   def objects():
       try:
          with sqlite3.connect(db_path) as conn:
              cursor = conn.cursor()
              query = (f''' SELECT  *FROM Book ''')
              for row in cursor.execute(query):
                 yield Book(row[1], row[2], row[3], row[4], row[5], row[0])   
       except:
          print("Bog\'lanishda xatolik")


   def get_by_id(id):
      try:
         with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''SELECT *FROM Book WHERE id = {id}'''
            res = cursor.execute(query).fetchone()
            if res is not None:
               return Book(res[0], res[1], res[2], res[3], res[4], res[5])
            else:
               return None
      except:
         print("bog\'lanishda xatolik")

   def __str__(self) -> str:
       return f"{self.Book_name}, {self.Year}, {self.Count_page}, {self.Price}, {self.Author}"





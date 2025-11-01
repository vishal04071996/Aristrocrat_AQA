import configparser


config = configparser.RawConfigParser()
config.read(".//configurations/config.ini")




class Read_Config:
   @staticmethod
   def get_username():
       username = config.get('admin login info', 'username')
       return username


   @staticmethod
   def get_Password():
       Password = config.get('admin login info', 'Password')
       return Password


   @staticmethod
   def get_wrong_username():
       wrong_username = config.get('admin login info', 'wrong_username')
       return wrong_username


   @staticmethod
   def get_wrong_password():
       wrong_password = config.get('admin login info', 'wrong_password')
       return wrong_password


   @staticmethod
   def get_URL():
       URL = config.get('admin login info', 'URL')
       return URL


   @staticmethod
   def get_actual_text():
       actual_text = config.get('admin login info', 'actual_text')
       return actual_text

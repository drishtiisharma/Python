# import sys
# the output will be a list of directory paths where python looks for whenever we use the import statement
# print(sys.path) # shows the module search paths
# print(sys.version) # shows python version available
# print(sys.argv)  
# print(sys.modules) # contains modules alr loaded
# print(sys.exit())
# ------------------------------------- #
# # USING DOTENV
# from dotenv import load_dotenv
# import os
# load_dotenv()

# print(os.getenv("API_KEY"))
# print(type(os.getenv("PORT"))) # prints 'str'
# x = int(os.getenv("PORT"))
# print(type(x))
# print(os.environ["API_KEY"]) 
# print(os.environ["DATABASE_URL"]) # throws KeyError 
# print(os.getenv("DATABASE_URL")) # returns None

# port = int(os.getenv("PORT"))
# debug = os.getenv("DEBUG") == "True"
# print(type(port))
# print(type(debug))
# ------------------------------------- #
# USING DECOUPLER
# from decouple import config

# api_key = config("API_KEY")
# port = config("PORT", cast=int)
# debug = config("DEBUG", cast=bool)

# print(type(api_key))
# print(type(port))
# print(type(debug))
# ------------------------------------- #

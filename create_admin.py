from config.database import add_admin, init_database

# create database tables if not created
init_database()

# create admin account
add_admin("manigoud8885@gmail.com", "mani@123")

print("Admin created successfully")
#Python code to fill vehicles model with random data

import os
import django

# Set up Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "register.settings")
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from vehicle.models import Vehicle  # Import your Vehicle model

# Rest of your script...

import random
from faker import Faker
from django.contrib.auth.models import User 

fake = Faker()

# Function to get a random image file path from a folder
def get_random_image_path():
    image_folder = 'images'  # Change this to your image folder path
    images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return random.choice(images)

# Function to create fake data and fill the database
def fill_database(num_records):
    for _ in range(num_records):
        # Generate fake data
        name = fake.name()
        number_plate = fake.random_int(min=1000, max=9999)
        distance_travelled = fake.random_int(min=1000, max=100000)
        mileage = fake.random_int(min=10, max=50)
        cost = fake.random_int(min=1000, max=50000)
        available_status = random.choice(['B', 'NB'])
        insurance_status = random.choice(['U', 'NU'])
        fuel = random.choice(['P', 'D'])

        # Get a random user
        owner = User.objects.order_by('?').first()

        # Create a vehicle instance
        vehicle = Vehicle.objects.create(
            owner=owner,
            name=name,
            number_plate=number_plate,
            distance_travelled=distance_travelled,
            images=get_random_image_path(),
            mileage=mileage,
            cost=cost,
            available_status=available_status,
            insurance_status=insurance_status,
            fuel=fuel,
            customer=owner
        )
        print(f"Vehicle created: {vehicle}")

# Call the function to fill the database with 100 records
#fill_database(100)
print("Done")

from vehicle.models import Vehicle

def approve_all_vehicles():
    # Get all vehicles with pending approval status
    pending_vehicles = Vehicle.objects.filter(approval_status='pending')

    # Approve all pending vehicles
    for vehicle in pending_vehicles:
        vehicle.approval_status = 'approved'
        vehicle.save()

    print(f"All vehicles have been approved.")

# Call the function to approve all vehicles
approve_all_vehicles()
print("DOne")
from smartphones import ContentCreationPhone, BusinessPhone, GamingPhone
from vehicles import Car, Helicopter, Boat

if __name__ == "__main__":
    # ✅ Create Different Smartphone Models
    content_phone = ContentCreationPhone("Huawei", "Pura 70 Pro", 90, "4K 60FPS + AI Stabilization")
    business_phone = BusinessPhone("Apple", "iPhone 15 Pro Max", 95, "End-to-End Encryption")
    gaming_phone = GamingPhone("Asus", "ROG Phone 8", 85, "Liquid Cooling + AI Optimization")

    # ✅ Test Smartphone Functions
    content_phone.get_status()
    content_phone.record_video()

    business_phone.get_status()
    business_phone.schedule_meeting()

    gaming_phone.get_status()
    gaming_phone.play_game()

    # ✅ Execute Polymorphism with Vehicles
    vehicles = [Car(), Helicopter(2000), Boat()]

    for vehicle in vehicles:
        vehicle.move()
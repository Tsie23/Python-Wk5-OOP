class Smartphone:
    """Base class for different types of smartphones."""
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
    
    def get_status(self):
        """Display smartphone details."""
        print(f"📱 {self.brand} {self.model} - Battery: {self.battery_level}%")

class ContentCreationPhone(Smartphone):
    """Phone designed for photography and filmmaking."""
    def __init__(self, brand, model, battery_level, camera_quality):
        super().__init__(brand, model, battery_level)
        self.camera_quality = camera_quality  # Example: "4K 60FPS + AI Stabilization"
    
    def record_video(self):
        """Simulates recording a video."""
        print(f"{self.model} is recording in {self.camera_quality}!")

class BusinessPhone(Smartphone):
    """Phone designed for productivity and business tasks."""
    def __init__(self, brand, model, battery_level, security_features):
        super().__init__(brand, model, battery_level)
        self.security_features = security_features  # Example: "End-to-End Encryption"
    
    def schedule_meeting(self):
        """Simulates scheduling a business meeting."""
        print(f"{self.model} is scheduling a secure business meeting.")

class GamingPhone(Smartphone):
    """Phone designed for high-performance gaming."""
    def __init__(self, brand, model, battery_level, cooling_system):
        super().__init__(brand, model, battery_level)
        self.cooling_system = cooling_system  # Example: "Liquid Cooling + AI Optimization"
    
    def play_game(self):
        """Simulates playing a game."""
        self.battery_level = max(0, self.battery_level - 30)
        print(f"{self.model} is playing a game! Cooling system: {self.cooling_system}")
        print(f"Battery now at {self.battery_level}%")
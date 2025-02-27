class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def copy(self):
        return Enemy(self.name, self.health, self.attack)  # skapa ny fiende
    
# Lista över fiender i spelet
enemies = {
    "zenith_drone": Enemy("Zenith Drone", 20, 5),
    "cyber_bandit": Enemy("Cyber Bandit", 25, 6),
    "security_mech": Enemy("Security Mech", 40, 8),
    "cyber_brute": Enemy("Cyber Brute", 35, 4)
}

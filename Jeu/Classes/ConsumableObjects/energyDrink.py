class EnergyDrink(Consumable):
    def consume(self, player):
        # Comportement spécifique lorsque le joueur consomme une boisson énergisante
        player.restore_energy(30)  # Par exemple, restaurer 30 points d'énergie au joueur

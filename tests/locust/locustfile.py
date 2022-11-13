"""Locust scenario"""
from locust import HttpUser, task


class User(HttpUser):
    """Locust configuration"""

    @task
    def get_pokemons_trainers(self):
        """request to simulate fight prepartation
        """
        self.client.get("/trainers/1")
        self.client.get("/trainers/2")

    @task
    def get_battle(self):
        """make a battle"""
        self.client.get("/pokemons/battle/1/3")

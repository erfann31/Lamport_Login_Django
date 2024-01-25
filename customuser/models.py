# Changes to the CustomUser model
import hashlib

from django.db import models


class CustomUser(models.Model):
    username = models.CharField(unique=True,max_length=31)
    hashed_password = models.CharField(max_length=128)
    iterations = models.IntegerField(default=100)  # Number of iterations for hashing

    def __str__(self):
        return self.username

    def set_password(self, password):
        # Hash the password multiple times before saving it to the database
        hashed_password = self._hash_password(password, self.iterations)
        self.hashed_password = hashed_password

    def check_password(self, password):
        # Check the hashed password against the provided password
        hashed_password = self._hash_password(password, 1)  # Hash once for comparison
        return hashed_password == self.hashed_password

    def _hash_password(self, password, iterations):
        # Hash the password multiple times using a simple hash function
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        for _ in range(iterations - 1):
            hashed_password = hashlib.sha256(hashed_password.encode('utf-8')).hexdigest()
        return hashed_password
    def save(self, *args, **kwargs):
        # Ensure iterations is not negative
        self.iterations = max(self.iterations, 0)
        super().save(*args, **kwargs)

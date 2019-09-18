from django.db import models
import bcrypt


class UserManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if len(postData["first"]) < 2:
            errors["first"] = "We're dubious that your first name is less than two letters!"
        if len(postData['last']) < 2:
            errors["last"] = "Unless you are Prince, Madonna, or Liberace, you'll need a last name, that's at least 2 letters!"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters, what were you thinking?"
        if postData["password"]!=postData["c_password"]:
            errors["password"] = "Your passwords (much like your socks) don't match!"
        # if postData["email"] = User.object.filter(email):
        #     errors["email"] = "You already exist here!"
        return errors
    
    def loginValidator(self, postData):   
        errors = {}
        if len(postData["email"]) < 2:
            errors["email"] = "Email can't be nonexistent!"
        if len(postData["password"]) < 2:
            errors["password"] = "What's the secret password?"
            return errors

        user = User.objects.get(email = postData['email'])
        if not user:
            if postData["email"] != user.email:
                errors["user"] = "Username and password are invalid"
            return errors
        if postData['password'] != user.password:
            errors["password"] = "Password invalid."
        else:
            return errors
  
class User(models.Model):
    first = models.CharField(max_length=45)
    last = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    conf_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.first


from myapp.models import UserData

data = UserData.objects.all()

for user in data:
    print(user)
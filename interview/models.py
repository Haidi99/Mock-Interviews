from django.db import models


class Job(models.Model):
    jid = models.IntegerField(null =False, primary_key=True)


class Subscribe(models.Model):
    id = models.IntegerField( null =False, primary_key=True)
    email = models.EmailField(max_length=50)


class User(models.Model):
    userid = models.IntegerField( null =False, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.TextField( null =False)
    image = models.ImageField(height_field=None, width_field=None)
    role = models.BooleanField(default= 0)
    phone = models.IntegerField(unique=True)
    jobid = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)


class FeedBack(models.Model):
    fbid = models.IntegerField(null =False, primary_key=True)
    template = models.TextField(max_length=10000)
    uid = models.OneToOneField(User, on_delete = models.CASCADE)


class Interview(models.Model):
    ivid = models.IntegerField( null =False, primary_key=True)
    date = models.DateField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    fid = models.OneToOneField(FeedBack, on_delete = models.CASCADE)


class Stage(models.Model):
    sid = models.IntegerField(null =False, primary_key=True)
    question = models.TextField(max_length=1000)
    comparefile = models.TextField(max_length=20)
    time = models.TimeField()
    title = models.TextField(max_length=20)
    fid = models.OneToOneField(FeedBack, on_delete = models.CASCADE)
    interviews = models.ManyToManyField(Interview)


class Dreamjob(models.Model):
    job_title = models.TextField(max_length=50)
    skills_text = models.TextField(max_length=1000 ,blank = True )
    #skills_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True)
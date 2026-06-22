from django.db import models




class Home(models.Model):
    image = models.ImageField(upload_to='banner_images/')
    image2 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image7 = models.ImageField(upload_to='banner_images/', null=True, blank=True)

class Academic_Program(models.Model):
    image = models.ImageField(upload_to='academic_program_images/')
    description = models.TextField()

class Principal_desk(models.Model):
    image = models.ImageField(upload_to='principal_desk_images/')
    name=models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Courses(models.Model):
    image = models.ImageField(upload_to='course_images/')
    course=models.CharField(max_length=200)
    description = models.TextField()
    duration=models.CharField(max_length=200)
    about=models.TextField()
    

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Management_desk(models.Model):
    image = models.ImageField(upload_to='management_desk_images/')
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    phone=models.CharField(max_length=200,null=True, blank=True)


class Administrator_desk(models.Model):
    image = models.ImageField(upload_to='administration_desk_images/')
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return str(self.image)
    

class ArtdayGallery(models.Model):
    image = models.ImageField(upload_to='artday_gallery_images/')

    def __str__(self):
        return str(self.image)
    

class Co_curricularGallery(models.Model):
    image = models.ImageField(upload_to='co_curricular_images/')
    
    def __str__(self):
        return str(self.image)


class Faculty(models.Model):
    image = models.ImageField(upload_to='faculty_desk_images/')
    name=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)


class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name="Notice Title")
    description = models.TextField(verbose_name="Notice Description")
    date = models.DateField(verbose_name="Event Date")
    time = models.TimeField(verbose_name="Event Time", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"
        ordering = ["-date", "-time"] 

    def __str__(self):
        return self.title
    

class UpComingEvents(models.Model):
    title = models.CharField(max_length=200, verbose_name="Event Title")
    description = models.TextField(verbose_name="Event Description")
    date = models.DateField(verbose_name="Event Date")
    time = models.TimeField(verbose_name="Event Time", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"
        ordering = ["-date", "-time"] 

    def __str__(self):
        return self.title









from django.db import models


class College(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length = 100)
    quota = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length = 100)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.firstName + self.lastName

class StudentApplication(models.Model):
    birthDate = models.DateField()
    birthPlace = models.CharField(max_length = 100)
    highSchoolName = models.CharField(max_length = 100)
    coverLetter = models.CharField(max_length = 100)
    highSchoolDocument = models.FileField(upload_to="uploads/")
    highSchoolGPA = models.DecimalField(max_digits = 3, decimal_places=2)
    maturaGrade = models.DecimalField(max_digits = 3, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True)

class Administrator(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.email
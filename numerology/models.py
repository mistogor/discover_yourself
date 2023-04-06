from django.db import models
from customuser.models import CustomUser

class NumerologyCategory(models.Model):
     title = models.CharField(max_length=64)
     description = models.TextField()
    
     def __str__(self):
        return self.title

# Простая нумерология...

class DestinyNumber(models.Model):
    category = models.ForeignKey(NumerologyCategory, on_delete=models.CASCADE)
    condition = models.PositiveIntegerField()
    text_result = models.TextField()
    
    def __str__(self):
        return self.category.title

class SoulNumber(models.Model):
    category = models.ForeignKey(NumerologyCategory, on_delete=models.CASCADE)
    condition = models.PositiveIntegerField()
    text_result = models.TextField()

    def __str__(self):
        return self.category.title


# Психоматрица Пифагора. Строки...

class PithagorFirstLine(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorSecondLine(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorThirdLine(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


# Психоматрица Пифагора. Столбцы...

class PithagorFirstColumn(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorSecondColumn(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result

class PithagorThirdColumn(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorAscendingDiagonal(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result

class PithagorDescendingDiagonal(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result

# Психоматрица Пифагора. Информация о цифрах...

class PithagorOnes(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result
    

class PithagorTwos(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorThrees(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result
    

class PithagorFours(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result
    

class PithagorFives(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorSixes(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result
    

class PithagorSevens(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result
    

class PithagorEights(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result


class PithagorNines(models.Model):
    condition = models.PositiveIntegerField(default= 0)
    text_result = models.TextField()
    
    def __str__(self):
        return self.text_result




# Результаты пользователей:

class PersonalResultNumerology(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    result = models.ForeignKey(DestinyNumber, on_delete = models.CASCADE)


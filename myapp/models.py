from django.db import models


CATEGORY = (('language', '言語'), ('other', 'その他'))
    
class Books(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    thumbnail = models.ImageField()
    user = models.ForeignKey('accounts.Customuser', on_delete=models.CASCADE)
    about = models.TextField()
    b_created_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Chapters(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='chapters' )
    chapter_id = models.IntegerField()
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name
    
class Contents(models.Model):
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE, related_name='contents')
    content_id = models.IntegerField()
    content_name = models.CharField(max_length=100)

    def __str__(self):
        return self.content_name
    
class Pages(models.Model):
    contents = models.ForeignKey(Contents, on_delete=models.CASCADE, related_name='pages')
    page_name = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True)
    page_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.page_name
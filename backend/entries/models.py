from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

# 詞條
class Entry(models.Model):
    cmn = models.CharField(max_length=100)  # 華語
    en = models.CharField(max_length=100, blank=True)  # 英語
    hak_hon = models.CharField(max_length=100)  # 客語-漢字
    hak_pin_a = models.CharField(max_length=100, blank=True)  # 客語-拼音-四縣（可選）
    hak_pin_b = models.CharField(max_length=100, blank=True)  # 客語-拼音-海陸（可選）
    hak_pin_c = models.CharField(max_length=100, blank=True)  # 客語-拼音-大埔（可選）
    hak_pin_d = models.CharField(max_length=100, blank=True)  # 客語-拼音-饒平（可選）
    hak_pin_e = models.CharField(max_length=100, blank=True)  # 客語-拼音-詔安（可選）
    hak_pin_f = models.CharField(max_length=100, blank=True)  # 客語-拼音-南四縣（可選）
    hak_lo = models.CharField(max_length=100, blank=True)  # 客語-羅馬字（可選）
    source = models.CharField(max_length=100)  # 資料來源
    approved = models.BooleanField(default=False)  # 是否審核通過
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    updated_at = models.DateTimeField(auto_now=True)  # 更新時間

    def __str__(self):
        return f"{self.cmn}－{self.hak_hon}({self.hak_pin_a})" #回傳 華語－客語漢字(客語羅馬字)

# 評分
class Rating(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)  # 評分對應的詞條
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 評分者
    score = models.FloatField()  # 分數
    updated_at = models.DateTimeField(auto_now=True)  # 評分時間

    class Meta:
        pass  # 允許重新評分

    def __str__(self):
        return f"{self.user.username}：{self.entry.cmn}－{self.entry.hak_hon}({self.entry.hak_pin_a}) {self.score}"

# 提交
class Submission(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)  # 相關詞條
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 提交者
    content = models.TextField()  # 提交內容
    created_at = models.DateTimeField(auto_now_add=True)  # 提交時間

    def __str__(self):
        return f"{self.user.username}：{self.entry.cmn}－{self.entry.hak_hon}({self.entry.hak_pin_a})"
from django import forms

from .models import Comment, PostReport, Post, Twit, TwitComment, TwitReport

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','image']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']

class ReportPostForm(forms.ModelForm):
	class Meta:
		model = PostReport
		fields = ['reason']

# Twit Features 

class TwitForm(forms.ModelForm):
	class Meta:
		model = Twit
		fields = ['title','content']


class TwitCommentForm(forms.ModelForm):
	class Meta:
		model = TwitComment
		fields = ['comment']

class TwitReportForm(forms.ModelForm):
	class Meta:
		model = TwitReport
		fields = ['reason']

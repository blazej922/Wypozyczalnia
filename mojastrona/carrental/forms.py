from django import forms
from .models import Comment, Car, PositionInOrder, Order

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'body', 'active']

		
class PositionInOrderForm(forms.ModelForm):
	class Meta:
		model = PositionInOrder
		fields = ['user', 'car', 'quantityrc', 'sincew', 'untilw', 'piosum']


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['user', 'nr_doc', 'osum', 'pio']
		
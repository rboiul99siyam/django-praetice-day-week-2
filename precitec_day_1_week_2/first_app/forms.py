from django import forms

# Create your forms here.

class StudentData(forms.Form):
	name = forms.CharField(label='Student Name ',min_length=10, widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'}))
	father_name = forms.CharField(min_length=10,widget=forms.TextInput(attrs={'placeholder' : 'Enter your father name here '}))
	mother_name = forms.CharField(min_length=10,widget=forms.TextInput(attrs={'placeholder':'Enter your mother name here'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your address name here'}))
	birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
	re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))
	arree = forms.BooleanField()
	color = [
		('blue','Blue'),
		('red','Red'),
		('green','Green'),
	]
	need_dress = [
		('T-shirt','T-shirt'),
		('paint','paint'),
		('traojar','traojar'),
	]
	dress_choice = forms.MultipleChoiceField(choices=need_dress,widget=forms.CheckboxSelectMultiple)
	favarite_color = forms.ChoiceField(choices=color,widget=forms.RadioSelect)
	
	def clean(self):
		cleaned_data = super().clean()
		val_pass = self.cleaned_data['password']
		val_rePass = self.cleaned_data["re_password"]
		if val_pass != val_rePass:
			raise forms.ValidationError('Password do not match ')   

   
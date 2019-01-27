from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,label="Email",
     widget=forms.TextInput(attrs={'placeholder': 'Emaill'}))
    nome = forms.CharField(required=True, label="Nome",
     widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    subject = forms.CharField(required=True, label="Assunto",
     widget=forms.TextInput(attrs={'placeholder': 'Assunto'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensagem','cols':'60'}), required=True, label="Mensagem")